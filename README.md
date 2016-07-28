TTHBB MEM code
==============

Setup on SLC6 in a clean directory (no CMSSW)
Please use *bash*
~~~
mkdir -p ~/choose/a/directory/
cd ~/choose/a/directory/
wget --no-check-certificate https://raw.githubusercontent.com/silviodonato/tthbb13/ttH80X/setup.sh
source setup.sh
scram b -j16
~~~
This will download CMSSW, the tthbb code and all the dependencies.



Step1: VHBB code
----------------
This will start with MiniAOD and produce a VHBB ntuple.

~~~
cd $CMSSW_BASE/src/TTH
#edit nEvents in  $CMSSW_BASE/src/VHbbAnalysis/Heppy/test/vhbb_combined.py 
#edit files in  $CMSSW_BASE/src/VHbbAnalysis/Heppy/test/vhbb.py (eg. /store/mc/RunIISpring16MiniAODv2/ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext3-v2/70000/001C3ACD-2C31-E611-A7EE-003048F5ADF6.root or  root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ttHTobb_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/40000/0089CC67-6338-E611-947D-0025904C4E2A.root)
make test_VHBB >& logTestVHbb &
#this will call VHbbAnalysis/Heppy/test/vhbb_combined.py
~~~

Step2: tthbb code
--------------------
Using the VHBB ntuple, we will run the ttH(bb) and matrix element code

~~~
cd $CMSSW_BASE/src/TTH
#edit testfile_vhbb_tthbb in CMSSW_BASE/src/TTH/Makefile
#eg. file:///scratch/sdonato/ttH/test/CMSSW/src/TTH/tests_out/VHBB.root
#in $CMSSW_BASE/src/TTH/MEAnalysis/python/samples_local.py, replace 'vhbb/tree' with 'tree'
make test_MEAnalysis >& logTestME &
#this will call TTH/MEAnalysis/python/MEAnalysis_heppy.py
~~~

Step1+2: VHBB & tthbb13 with CRAB
---------------------------------

To submit a few test workflows with crab do:

~~~
cd $CMSSW_BASE/src/TTH/MEAnalysis/crab_vhbb
## adding "ttbar-spring16-80X.weights.xml" among input files in multicrab.py
## remove missing datasets
python multicrab.py --workflow testing_withme --tag my_test1
~~~

To produce all the SL/DL samples, do
~~~
cd $CMSSW_BASE/src/TTH/MEAnalysis/crab_vhbb
python multicrab.py --workflow leptonic --tag May13
~~~


Step3: skim with `projectSkim.sh`
------------------
When some of the samples are done, you can produce small (<5GB) skims of the files using

~~~
cd $CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets
#produce the dataset folder
python ../python/MakeDatasetFiles.py --datasetfile datasets/ttHDaniel/datasetList.txt --version myDatasetFolder --instance prod/phys03
cd $CMSSW_BASE/src/TTH/MEAnalysis/gc
source makeEnv.sh
#edit confs/projectSkim.conf
#eg. find datasets/ttHDaniel/ | grep tth

./grid-control/go.py confs/projectSkim.conf -cG
...
./hadd.py /path/to/output/GC1234/
~~~

The total processed yields can be extracted with
~~~
cd TTH/MEAnalysis/gc
./grid-control/go.py confs/count.conf
...
./hadd.py /path/to/output/GC1234/
python ../python/getCounts.py /path/to/output/GC1234/
~~~


Step3: Sparse histograms with `sparsinator.py`
------------------
In order to industrially produce all variated histograms, we create an intermediate file containing ROOT THnSparse histograms of the samples.

First test the `sparsinator.py` locally:
~~~
source $CMSSW_BASE/src/TTH/setenv_psi.sh
cd $CMSSW_BASE/src/TTH
make test_sparsinator
~~~
Then launch the jobs:
~~~
cd $CMSSW_BASE/src/TTH/MEAnalysis/gc
./grid-control/go.py confs/sparse.conf -cG
~~~
Once the jobs are done:
~~~
hadd ControlPlotsSparse.root `find /path/to/output/GC1234/ -name "*.root"`
~~~
This creates a histogram file `ControlPlotsSparse.root`


Step4: Categories with `makecategories.sh`
-----------------

Configure the input file in `TTH/Plotting/python/Datacards/AnalysisSpecificationSL.py`, then call

~~~
cd $CMSSW_BASE/src/TTH/MEAnalysis/gc
#generate the parameter csv files: analysis_groups.csv, analysis_specs.csv
#edit $CMSSW_BASE/src/TTH/Plotting/python/Datacards/AnalysisSpecificationSL.py
#change at least "input_file"
python $CMSSW_BASE/src/TTH/Plotting/python/Datacards/AnalysisSpecification.py
./grid-control/go.py confs/makecategory.conf
~~~

Step5: Limits with `makelimits.sh`
-----------------

Configure the path to the category output in `confs/makelimits.conf` by setting `datacardbase` to the output of step 4.

~~~
cd TTH/MEAnalysis/gc
cp local-example.conf local.conf 
## edit makelimits and change datacards (eg. ~/tth/gc/makecategory/GC46066f85f573/)
vi confs/makelimits.conf
./grid-control/go.py confs/makelimits.conf
~~~


######### OLD #####################
Step3: Sparse histograms with `Plotting/bin/MELooper.cc`
------------------
In order to industrially produce all variated histograms, we create an intermediate file containing ROOT THnSparse histograms of the samples.

First make the `melooper` exe:
~~~
cd TTH
make melooper
~~~

Then submit the jobs
~~~
cd TTH/MEAnalysis/gc
./grid-control/go.py confs/plots.conf
~~~

Once the jobs are done:
~~~
hadd ControlPlotsSparse.root `find /path/to/output/GC1234/ -name "*.root"`
~~~
This creates a histogram file `ControlPlotsSparse.root`
