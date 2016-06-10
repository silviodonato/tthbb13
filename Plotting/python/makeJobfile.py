#!/usr/bin/env python
#Produces a job.json file which configures the MELooper
#it will configure MELooper to run over a set of files which belong to a
#certain sample, producing a sparse histogram with the axes defined in
#the configuration.
#This script reads the environment variables
#FILE_NAMES="file1.root file2.root"
#DATASETPATH="name of dataset"
import json, sys, os
from TTH.MEAnalysis.samples_base import getSitePrefix, xsec

filenames = map(getSitePrefix, os.environ["FILE_NAMES"].split())
sample = os.environ["DATASETPATH"]
prefix = "" 

#for event-based splitting
#firstEvent = int(os.environ.get("SKIP_EVENTS", 0))
#nEvents = int(os.environ.get("MAX_EVENTS", -1))

#for file-based splitting
firstEvent = 0
nEvents = -1

nbins_mem = 36
nbins_bdt = 40

sample_repl = {
    "ttHToNonbb_M125_13TeV_powheg_pythia8": "ttH_nonhbb",
    "ttHTobb_M125_13TeV_powheg_pythia8": "ttH_hbb",
    "TT_TuneCUETP8M1_13TeV-powheg-pythia8": "ttbarUnsplit",
    "TT_TuneEE5C_13TeV-powheg-herwigpp": "ttbarUnsplit",
    "TTTo2L2Nu_13TeV-powheg": "ttbarUnsplit",
    "TTToSemiLeptonic_13TeV-powheg": "ttbarUnsplit",
}

ret = {
    "filenames": filenames,
    "lumi": 1.0,
    "process": sample_repl.get(sample, sample),
    "xsweight": 1.0,
    "prefix": sample,
    "outputFile": "ControlPlotsSparse.root",
    "firstEntry": firstEvent,
    "numEntries": nEvents,
    "printEvery": 0,
    "sparseAxes": [
        {
            "func": "counting",
            "xMin": 0,
            "xMax": 1,
            "nBins": 1 
        },
        {
            "func": "leptonFlavour",
            "xMin": 0,
            "xMax": 6,
            "nBins": 6 
        },
        {
            "func": "eventParity",
            "xMin": 0,
            "xMax": 2,
            "nBins": 2 
        },
        {
            "func": "mem_SL_2w2h2t",
            "xMin": 0,
            "xMax": 1,
            "nBins": nbins_mem 
        },
        {
            "func": "mem_SL_2w2h2t_sj",
            "xMin": 0,
            "xMax": 1,
            "nBins": nbins_mem
        },
        {
            "func": "mem_SL_0w2h2t",
            "xMin": 0,
            "xMax": 1,
            "nBins": nbins_mem
        },
        {
            "func": "mem_SL_1w2h2t",
            "xMin": 0,
            "xMax": 1,
            "nBins": nbins_mem
        },
        {
            "func": "mem_DL_0w2h2t",
            "xMin": 0,
            "xMax": 1,
            "nBins": nbins_mem
        },
        {
            "func": "common_bdt",
            "xMin": -1,
            "xMax": 1,
            "nBins": nbins_bdt
        },
        {
            "func": "numJets",
            "xMin": 3,
            "xMax": 7,
            "nBins": 4
        },
        {
            "func": "nBCSVM",
            "xMin": 1,
            "xMax": 5,
            "nBins": 4
        },
        {
            "func": "btag_LR_4b_2b_logit",
            "xMin": -20,
            "xMax": 20,
            "nBins": 50
        },
    ]
}
of = open("job.json", "w")
of.write(json.dumps(ret, indent=2))
of.close()
