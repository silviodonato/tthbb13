import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("FAKE")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	#"file:///shome/sdonato/QCD_HT2000toInf_MINIAODSIM.root" #file for local test
),
)
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('tree.root')
)

#maxEvents is used only for local test
#process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(30)
#)

process.out = cms.EndPath(process.output)


