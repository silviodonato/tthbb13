#!/bin/bash

source common.sh
#export DATASETPATH=ttHTobb_M125_13TeV_powheg_pythia8_dsalerno-VHBBHeppyV21_tthbbV9_v3_3
#export FILE_NAMES=/store/user/dsalerno/tth/VHBBHeppyV21_tthbbV9_v3_3/ttHTobb_M125_13TeV_powheg_pythia8/VHBBHeppyV21_tthbbV9_v3_3/160518_110721/0000/tree_10.root = 1634
#export GC_SCRATCH=/scratch/sdonato

#go to work directory
cd $GC_SCRATCH

#python ${CMSSW_BASE}/src/TTH/MEAnalysis/python/MakeTaggingNtuple.py taggingNtuple.root $FILE_NAMES
python ${CMSSW_BASE}/src/TTH/MEAnalysis/python/projectSkim.py skim.root $FILE_NAMES
python ${CMSSW_BASE}/src/TTH/Plotting/python/joosep/btag/hists.py btag.root $FILE_NAMES
python ${CMSSW_BASE}/src/TTH/MEAnalysis/python/counts.py count.root $FILE_NAMES
hadd out.root skim.root btag.root count.root
