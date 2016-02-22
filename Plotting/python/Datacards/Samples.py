import os, glob

hostname = os.environ.get("HOSTNAME", "")
#PSI
if "t3ui12" in hostname:
    path = "/scratch/gregor/jpata/tth/Oct5_bdt_022sj_V13_47cdf50/"
#Jooseps laptop
elif "pata-slc6" in hostname:
    path = "/home/joosep/joosep-mac/Documents/tth/data/ntp/v14/me/"
elif "pata-macbook" in hostname:
    path = "/Users/joosep/Documents/tth/data/ntp/v16/me/"
#Tallinn
elif "quasar" in hostname:
    path = "/hdfs/local/joosep/tth/Feb4_dl/"
elif "hep.kbfi.ee" in hostname:
    path = "/home/joosep/tth/gc/"
else:
    raise Exception("Sample path not defined for hostname={0}!".format(hostname))

class Sample:
    def __init__(self, name, filenames, prefix, cut):
        self.name = name
        self.filenames = filenames
        self.prefix = prefix 
        self.cut = cut
samples_dict = {
#    "SingleMuon": Sample(
#        "SingleMuon",
#        [path + "cfg_withME/SingleMuon.root"],
#        ""
#    ),
#    "SingleElectron": Sample(
#        "SingleElectron",
#        [path + "cfg_withME/SingleElectron.root"],
#        ""
#    ),
#    "DoubleMuon": Sample(
#        "DoubleMuon",
#        [path + "cfg_withME/DoubleMuon.root"],
#        ""
#    ),
#    "DoubleEG": Sample(
#        "DoubleEG",
#        [path + "cfg_withME/DoubleEG.root"],
#        ""
#    ),
#    "MuonEG": Sample(
#        "MuonEG",
#        [path + "cfg_withME/MuonEG.root"],
#        ""
#    ),
    "ttH_hbb": Sample(
        "ttH_hbb",
        glob.glob("/hdfs/cms/store/user/jpata/tthbb13/VHBBHeppyV16pre/Feb10_15fedbd/ttHTobb_M125_13TeV_powheg_pythia8_10000/crab_ttHTobb_M125_13TeV_powheg_pythia8_10000/160210_184953/0000/*.root"),
        ""
    ),
#    "ttbarPlus2B": Sample(
#        "ttbarPlus2B", 
#        [path + "TT_TuneCUETP8M1_13TeV-powheg-pythia8_tt2b.root"],
#        "",
#    ),
#    "ttbarPlusB": Sample(
#        "ttbarPlusB", 
#        [path + "TT_TuneCUETP8M1_13TeV-powheg-pythia8_ttb.root"],
#        "",
#    ),
#    "ttbarPlusBBbar": Sample(
#        "ttbarPlusBBbar", 
#        [path + "TT_TuneCUETP8M1_13TeV-powheg-pythia8_ttbb.root"],
#        "",
#    ),
#    "ttbarPlusCCbar": Sample(
#        "ttbarPlusCCbar", 
#        [path + "TT_TuneCUETP8M1_13TeV-powheg-pythia8_ttcc.root"],
#        "",
#    ),
#    "ttbarOther": Sample(
#        "ttbarOther", 
#        [path + "TT_TuneCUETP8M1_13TeV-powheg-pythia8_ttll.root"],
#        "",
#    ),
}
