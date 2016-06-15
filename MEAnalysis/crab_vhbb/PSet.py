import FWCore.ParameterSet.Config as cms

process = cms.Process("FAKE")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd-cms.infn.it////store/mc/RunIIFall15MiniAODv2/ttHToNonbb_M125_13TeV_powheg_pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/021B993B-4DBB-E511-BBA6-008CFA1111B4.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange("1:4599")
)
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('tree.root')
)


process.out = cms.EndPath(process.output)


