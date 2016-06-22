from TTH.MEAnalysis.samples_base import *
import FWCore.ParameterSet.Config as cms
import os

version = "Jun17_leptonic_nome"
datasetpath = os.environ["CMSSW_BASE"] + "/src/TTH/MEAnalysis/gc/datasets/" + version

samples = {
    "DoubleEG": {
        "isMC": False,
    },
    "DoubleMuon": {
        "isMC": False,
    },
    "MuonEG": {
        "isMC": False,
    },
    "SingleElectron": {
        "isMC": False,
    },
    "SingleMuon": {
        "isMC": False,
    },

    "TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": {
        "isMC": True,
    },
    "TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": {
        "isMC": True,
    },
    "TTTo2L2Nu_13TeV-powheg": {
        "isMC": True,
    },
    "TT_TuneEE5C_13TeV-powheg-herwigpp": {
        "isMC": True,
    },
}
