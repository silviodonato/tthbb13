# THIS IS AN AUTOGENERATED FILE
# Made by prepareSamples.py
# do NOT modify (except to skip individual samples)


import FWCore.ParameterSet.Config as cms
from TTH.MEAnalysis.samples_base import *

version = "Jul8_pilot_v2"
samples_dict = {
 
        "ttHTobb_M125_13TeV_powheg_pythia8": cms.PSet(
            name     = cms.string("ttHTobb_M125_13TeV_powheg_pythia8"),
            nickname = cms.string("ttHTobb_M125_13TeV_powheg_pythia8"),
            isMC     = cms.bool(True),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files("$CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets/Jul15_leptonic_v1/ttHTobb_M125_13TeV_powheg_pythia8.txt")),
        ),
     
        "TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": cms.PSet(
            name     = cms.string("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"),
            nickname = cms.string("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"),
            isMC     = cms.bool(False),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files("$CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets/Jul15_leptonic_v1/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt")),
        ),
     
        "TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": cms.PSet(
            name     = cms.string("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"),
            nickname = cms.string("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"),
            isMC     = cms.bool(False),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files("$CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets/Jul15_leptonic_v1/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.txt")),
        ),
     
        "TTTo2L2Nu_13TeV-powheg": cms.PSet(
            name     = cms.string("TTTo2L2Nu_13TeV-powheg"),
            nickname = cms.string("TTTo2L2Nu_13TeV-powheg"),
            isMC     = cms.bool(True),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files("$CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets/Jul15_leptonic_v1/TTTo2L2Nu_13TeV-powheg.txt")),
        ),
     
        "TT_TuneCUETP8M1_13TeV-powheg-pythia8": cms.PSet(
            name     = cms.string("TT_TuneCUETP8M1_13TeV-powheg-pythia8"),
            nickname = cms.string("TT_TuneCUETP8M1_13TeV-powheg-pythia8"),
            isMC     = cms.bool(True),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files("$CMSSW_BASE/src/TTH/MEAnalysis/gc/datasets/Jul15_leptonic_v1/TT_TuneCUETP8M1_13TeV-powheg-pythia8.txt")),
        ),
    }
