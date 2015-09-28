#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)
#ROOT.gErrorIgnoreLevel = ROOT.kError
import sys, imp, os, copy
from Samples import samples_dict

def PrintDatacard(event_counts, datacard, dcof):

    number_of_bins = len(datacard.categories)    
    number_of_backgrounds = len(datacard.processes) - 1 
    analysis_categories = list(datacard.categories.keys())

    dcof.write("imax {0}\n".format(number_of_bins))
    dcof.write("jmax {0}\n".format(number_of_backgrounds))
    dcof.write("kmax *\n")
    dcof.write("---------------\n")

    for cat, analysis_var in datacard.categories.items():                
        dcof.write("shapes * {0} {1} $PROCESS/$CHANNEL/{2} $PROCESS/$CHANNEL/{2}_$SYSTEMATIC\n".format(cat, datacard.histfilename, analysis_var))

    #dcof.write("shapes data_obs sl_jge6_tge4 /shome/jpata/tth/datacards/Sep7_ref2_spring15/fakeData.root $PROCESS/$CHANNEL/mem_d_nomatch_0 $PROCESS/$CHANNEL/mem_d_nomatch_0_$SYSTEMATIC\n")
        
    dcof.write("---------------\n")

    dcof.write("bin\t" +  "\t".join(analysis_categories) + "\n")
    dcof.write("observation\t" + "\t".join("-1" for _ in analysis_categories) + "\n")
    dcof.write("---------------\n")

    bins        = []
    processes_0 = []
    processes_1 = []
    rates       = []

    # Conversion: 
    # Example: ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_hbb -> ttH_hbb

    for cat in datacard.categories:
        for i_sample, sample in enumerate(datacard.processes):
            bins.append(cat)
            processes_0.append(sample)
            if sample in datacard.signal_processes:
                i_sample = -i_sample
            processes_1.append(str(i_sample))
            rates.append(str(event_counts[sample][cat]))

    dcof.write("bin\t"+"\t".join(bins)+"\n")
    dcof.write("process\t"+"\t".join(processes_0)+"\n")
    dcof.write("process\t"+"\t".join(processes_1)+"\n")
    dcof.write("rate\t"+"\t".join(rates)+"\n")
    dcof.write("---------------\n")

    # Gather all scale uncerainties
    all_scale_uncerts = []
    for k,v in datacard.scale_uncertainties.iteritems():
        for kk, vv in v.iteritems():
            all_scale_uncerts.extend(vv.keys())
    # Uniquify
    all_scale_uncerts = list(set(all_scale_uncerts))
            
    for scale in all_scale_uncerts:
        dcof.write(scale + "\t lnN \t")
        for cat in analysis_categories:
            for sample in datacard.processes:
                if (cat in datacard.scale_uncertainties.keys() and 
                    sample in datacard.scale_uncertainties[cat].keys() and 
                    scale in datacard.scale_uncertainties[cat][sample].keys()):
                    dcof.write(str(datacard.scale_uncertainties[cat][sample][scale]))
                else:
                    dcof.write("-")
                dcof.write("\t")
        dcof.write("\n")

    # Gather all shape uncerainties
    all_shape_uncerts = []
    for k,v in datacard.shape_uncertainties.iteritems():
        for kk, vv in v.iteritems():
            all_shape_uncerts.extend(vv.keys())
    # Uniquify
    all_shape_uncerts = list(set(all_shape_uncerts))


    for shape in all_shape_uncerts:
        dcof.write(shape + "\t shape \t")
        for cat in analysis_categories:
            for sample in datacard.processes:
                if (cat in datacard.shape_uncertainties.keys() and 
                    sample in datacard.shape_uncertainties[cat].keys() and 
                    shape in datacard.shape_uncertainties[cat][sample].keys()):
                    dcof.write(str(datacard.shape_uncertainties[cat][sample][shape]))
                else:
                    dcof.write("-")
                dcof.write("\t")
        dcof.write("\n")
            
    dcof.write("# Execute with:\n")
    dcof.write("# combine -M Asymptotic -t -1 {0} \n".format(datacard.output_datacardname))
    
# end of PrintDataCard
def MakeDatacard(histfile, dcard):
    """
    Reads histograms from histfile and prints out a datacard.txt according
    to the configuration given in dcard
    histfile (TFile): file with histograms for fit
    dcad (Datacard): Datacard configuration
    """
    dcof = open(dcard.output_datacardname, "w")

    # dict of dicts. First key: sample Second key: cut
    # Content: events at given lumi
    event_counts = {}
    
    for sample in dcard.processes:
        #print " sample", sample
        sampled = histfile.Get(sample)
        assert(sampled != None)
        sampled.cd()
        event_counts[sample] = {}
        for cutname, analysis_var in dcard.categories.items():
            #print "  cutname={0} var={1}".format(cutname, analysis_var)
            jetd = sampled.Get(cutname)
            if jetd != None:
                h = jetd.Get(analysis_var)
                I = 0
                if h != None:
                    I = h.Integral()
                event_counts[sample][cutname] = I
            else:
                event_counts[sample][cutname] = 0

    PrintDatacard(event_counts, dcard, dcof)
# end of MakeDatacard

def ConfigureDatacard(dcard, categories, ofname):
    """
    Configures a Datacard object to use the specified categories.
    dcard (Datacard): input datacard
    categories (list of strings): categories to combine in fit
    ofname (string): output filename for the datacard.txt
    """

    dcard_new = copy.deepcopy(dcard)
    dcard_new.categories = categories
    dcard_new.shape_uncertainties = {}
    dcard_new.scale_uncertainties = {}
    for cat in dcard_new.categories:
        dcard_new.shape_uncertainties[cat] = dcard_new.total_shape_uncert
        dcard_new.scale_uncertainties[cat] = dcard_new.common_scale_uncertainties
    dcard_new.output_datacardname = ofname
    return dcard_new
# end of ConfigureDatacard

if __name__ == "__main__":
    # Get the input proto-datacard
    datacard_path = sys.argv[1]
    dcard = imp.load_source("dcard", datacard_path)

    #path to datacard directory
    full_path = sys.argv[2]
    of_name = os.path.join(full_path, dcard.Datacard.histfilename)
    histfile = ROOT.TFile.Open(of_name)
    
    #Loop over individual categories
    for cat in [x[0] for x in dcard.Datacard.categories]:
        print cat
        # output datacard text file
        dcof_name = os.path.join(full_path, "shapes_{0}.txt".format(cat))
        dcard_new = ConfigureDatacard(dcard.Datacard, [cat], dcof_name)
        MakeDatacard(histfile, dcard_new)
    #FIXME: add loop over combined categories here
    
