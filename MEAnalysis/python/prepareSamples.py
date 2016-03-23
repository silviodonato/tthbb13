import os
import glob
import FWCore.ParameterSet.Config as cms
from TTH.MEAnalysis.samples_base import *
import ROOT

cmssw_base = os.environ["CMSSW_BASE"]

datasetpath = "src/TTH/MEAnalysis/gc/datasets/VHBBHeppyV21_tthbbV6/"
getSize = False

path1 = os.path.join(cmssw_base, datasetpath)
samples = [ os.path.splitext(os.path.basename(s))[0] for s in glob.glob(os.path.join(path1,"*.txt"))]
print samples

sampfiles = {}
samples_dict = {}

samp_py = open("samples.py", "w")

samp_py.write("# THIS IS AN AUTOGENERATED FILE\n")
samp_py.write("# Made by prepareSamples.py\n")
samp_py.write("# do NOT modify (except to skip individual samples)\n\n\n")

samp_py.write('from TTH.MEAnalysis.samples_base import *\n\n')

samp_py.write('datasetpath = "' + datasetpath + '"\n')

samp_py.write("samples_dict = {\n")
for sample in samples:

    samplepath = os.path.join(path1, sample)
    sampfiles = []
    for (dirpath, dirnames, filenames) in os.walk(samplepath):
        if "failed" in dirpath:
            continue
        filenames = filter(lambda x: ".root" in x, filenames)
        sampfiles += map(lambda x: os.path.join(dirpath, x), filenames)
    sampfiles = map(lambda x: x.replace("/hdfs/cms", ""), sampfiles)
    isMC = True
    
    nGenEff = 0

    # outfile = open(sample+".txt", "w")
    # outfile.write("[{0}]\n".format(sample))
    # 
    # for f in sampfiles:
    #     if len(f) > 240:
    #         #we can't submit crab jobs on filenames that are too long, need to catch them early
    #         #https://github.com/dmwm/CRABServer/issues/5146
    #         #raise Exception("sample {0} has long filename {1}".format(sample, f))
    #         pass
    #     if not getSize:
    #         outfile.write("{0} = 1\n".format(f))
    #     else:
    #         pfn = lfn_to_pfn("file://" + f)
    #         tf = ROOT.TFile.Open(pfn)
    #         if (tf == None or tf is None or tf.IsZombie()):
    #             print "could not read file {0}, {1}, {2}".format(pfn, tf)
    #         else:
    #             tt = tf.Get("tree")
    #             if (tt == None):
    #                 print "could not read tree"
    #             else:
    #                 outfile.write("{0} = {1}\n".format(f, int(tt.GetEntries())))
    #                 hcn = tf.Get("CountNegWeight")
    #                 hcp = tf.Get("CountPosWeight")
    #                 if hcn == None or hcp == None:
    #                     continue
    #                 nGenEff += hcp.GetBinContent(1) - hcn.GetBinContent(1)
    #         tf.Close()
    # outfile.close()

    if "Single" in sample or "Double" in sample or "MuonEG" in sample:
        isMC = False
    
    dfi = open("{0}.txt".format(sample), "w")
    for sf in sampfiles:
        dfi.write(sf + "\n")
    dfi.close()
    nick = samples_nick.get(sample, sample)
    x = """    
        "{0}": cms.PSet(
            name     = cms.string("{0}"),
            nickname = cms.string("{2}"),
            xSec     = cms.double("{4}"),
            nGen     = cms.int64({3}),
            skip     = cms.bool(False),
            isMC     = cms.bool({1}),
            treeName = cms.string("vhbb/tree"),
            subFiles = cms.vstring(get_files(datasetpath + "{0}.txt")),
        ),
    """.format(sample, isMC, nick, int(nGenEff), xsec_sample.get(sample, 1))
    samp_py.write(x)

samp_py.write("}\n")
samp_py.close()
