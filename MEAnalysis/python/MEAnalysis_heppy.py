#!/usr/bin/env python
import os
import PhysicsTools.HeppyCore.framework.config as cfg
import ROOT
import imp

import itertools

from TTH.MEAnalysis.samples_vhbb import samples, sample_version, lfn_to_pfn
from TTH.MEAnalysis.samples_local import samples_dict

#Create configuration object
if os.environ.has_key("ME_CONF"):
    print "Loading ME config from", os.environ["ME_CONF"]
    meconf = imp.load_source("meconf", os.environ["ME_CONF"])
    from meconf import Conf
else:
    print "Loading ME config from TTH.MEAnalysis.MEAnalysis_heppy_cfg"
    from TTH.MEAnalysis.MEAnalysis_cfg_heppy import Conf
conf = Conf()

print "loading samples from", conf.general["sampleFile"]
samplefile = imp.load_source("samplefile", conf.general["sampleFile"])
from samplefile import samples_dict

# input component
# several input components can be declared,
# and added to the list of selected components
inputSamples = []
for s in samples_dict.values():
    inputSample = cfg.Component(
        'tth',
        files = map(lfn_to_pfn, s.subFiles.value()),
        tree_name = "tree"
    )
    inputSample.isMC = s.isMC.value()
    if s.skip.value() == False and len(s.subFiles.value())>0:
        inputSamples.append(inputSample)

#Event contents are defined here
from TTH.MEAnalysis.VHbbTree import *
evs = cfg.Analyzer(
    EventAnalyzer,
    'events',
)

import TTH.MEAnalysis.MECoreAnalyzers as MECoreAnalyzers

leps = cfg.Analyzer(
    MECoreAnalyzers.LeptonAnalyzer,
    'leptons',
    _conf = conf
)

jets = cfg.Analyzer(
    MECoreAnalyzers.JetAnalyzer,
    'jets',
    _conf = conf
)

genrad = cfg.Analyzer(
    MECoreAnalyzers.GenRadiationModeAnalyzer,
    'genrad',
    _conf = conf
)
btaglr = cfg.Analyzer(
    MECoreAnalyzers.BTagLRAnalyzer,
    'btaglr',
    _conf = conf
)

mecat = cfg.Analyzer(
    MECoreAnalyzers.MECategoryAnalyzer,
    'mecat',
    _conf = conf
)

wtag = cfg.Analyzer(
    MECoreAnalyzers.WTagAnalyzer,
    'wtag',
    _conf = conf
)

mem_analyzer = cfg.Analyzer(
    MECoreAnalyzers.MEAnalyzer,
    'mem',
    _conf = conf
)

from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import *

jetType = NTupleObjectType("jetType", variables = [
    NTupleVariable("pt", lambda x : x.pt),
    NTupleVariable("eta", lambda x : x.eta),
    NTupleVariable("phi", lambda x : x.phi),
    NTupleVariable("mass", lambda x : x.mass),
    NTupleVariable("id", lambda x : x.id),
    NTupleVariable("btagCSV", lambda x : x.btagCSV),
    NTupleVariable("mcFlavour", lambda x : x.mcFlavour, type=int),
    NTupleVariable("mcMatchId", lambda x : x.mcMatchId, type=int),
    NTupleVariable("hadronFlavour", lambda x : x.hadronFlavour, type=int),
    NTupleVariable("mcPt", lambda x : x.mcPt),
    NTupleVariable("mcEta", lambda x : x.mcEta),
    NTupleVariable("mcPhi", lambda x : x.mcPhi),
])


treeProducer = cfg.Analyzer(
    class_object = AutoFillTreeProducer,
    verbose = False,
    vectorTree = True,
    globalVariables = [
        NTupleVariable(
            "Wmass", lambda ev: ev.Wmass,
            help="best W boson mass from untagged pair (untagged by CSVM)"
        ),
        NTupleVariable(
            "is_sl", lambda ev: ev.is_sl,
            help="event is single-lepton"
        ),
        NTupleVariable(
            "is_dl", lambda ev: ev.is_dl,
            help="event is di-lepton"
        ),
        NTupleVariable(
            "Wmass2", lambda ev: ev.Wmass2,
            help="best W boson mass from untagged pair (untagged by LR)"
        ),
        NTupleVariable(
            "cat", lambda ev: ev.catn,
            type=int,
            help="ME category"
        ),
        NTupleVariable(
            "btag_LR_4b_2b", lambda ev: ev.btag_LR_4b_2b,
            help="B-tagging likelihood ratio: 4b vs 2b"
        ),
        NTupleVariable(
            "nMatchSimB", lambda ev: ev.nMatchSimB if hasattr(ev, "nMatchSimB") else 0,
            type=int,
            help=""
        ),
        NTupleVariable(
            "nMatchSimC", lambda ev: ev.nMatchSimC if hasattr(ev, "nMatchSimC") else 0,
            type=int,
            help=""
        ),
        NTupleVariable(
            "p_hypo_tth", lambda ev: ev.p_hypo_tth if hasattr(ev, "p_hypo_tth") else 0.0,
            type=float,
            help=""
        ),
        NTupleVariable(
            "p_hypo_ttbb", lambda ev: ev.p_hypo_ttbb if hasattr(ev, "p_hypo_ttbb") else 0.0,
            type=float,
            help=""
        ),
    ],
    globalObjects = {},
    collections = {
    #standard dumping of objects
        "good_jets" : NTupleCollection("good_jets", jetType, 8, help="FIXME"),
    }
)

#Override the default fillCoreVariables function, which
#by default looks for FWLite variables
def fillCoreVariables(self, tr, event, isMC):
    for x in ["run", "lumi", "evt", "xsec", "nTrueInt", "puWeight", "genWeight"]:
        tr.fill(x, getattr(event.input, x))
AutoFillTreeProducer.fillCoreVariables = fillCoreVariables

# definition of a sequence of analyzers,
# the analyzers will process each event in this order
sequence = cfg.Sequence( [
    evs,
    leps,
    jets,
    #genrad,
    btaglr,
    mecat,
    wtag,
    mem_analyzer,
    treeProducer
])

from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='tree.root',
    option='recreate'
)

#finalization of the configuration object.
from PhysicsTools.HeppyCore.framework.chain import Chain as Events
config = cfg.Config(
    #Run across these inputs
    components = inputSamples,

    #Using this sequence
    sequence = sequence,

    #save output to these services
    services = [output_service],

    #This defines how events are loaded
    events_class = Events
)

print config.components
if __name__ == "__main__":
    print "Running MEAnalysis heppy main loop"
    from PhysicsTools.HeppyCore.framework.looper import Looper
    looper = Looper( 'Loop', config, nPrint = 0, nEvents = 10000)

    looper.loop()
    looper.write()

    for analyzer in looper.analyzers:
        print analyzer.name, "counters = {\n", analyzer.counters, "}"
