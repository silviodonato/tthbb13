from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = True
config.General.workArea = 'crab_projects/VHBBHeppyV21pre_tthbbV4pre_nome'
config.General.requestName = 'tth_VHBBHeppyV21pre_tthbbV4pre_nome_TT_TuneCUETP8M1_13TeV-powheg-Py8__fall15MAv2-pu25ns15v12_ext3-v1'
config.section_('JobType')
config.JobType.psetName = 'heppy_crab_fake_pset.py'
config.JobType.pluginName = 'Analysis'
config.JobType.maxJobRuntimeMin = 1200
config.JobType.inputFiles = ['heppy_config.py', 'heppy_crab_script.py', 'addTreeFiles.py', 'python.tar.gz', 'data.tar.gz', 'MEAnalysis_heppy.py', 'MVAJetTags_620SLHCX_Phase1And2Upgrade.db', 'combined_cmssw.py', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/vhbb.py', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/vhbb_combined.py', 'TMVAClassification_BDT.weights.xml', 'puData.root', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/puDataMinus.root', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/puDataPlus.root', 'puMC.root', 'json.txt', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/Zll-spring15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/Wln-spring15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/Znn-spring15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/VBF-spring15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/ttbar-spring15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/ttbar-fall15.weights.xml', '/shome/jpata/tth/sw-76/CMSSW/src/VHbbAnalysis/Heppy/test/TMVA_blikelihood_vbf_cmssw76.weights.xml']
config.JobType.scriptExe = 'heppy_crab_script.sh'
config.section_('Data')
config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/MINIAODSIM'
config.Data.outputDatasetTag = 'VHBBHeppyV21pre_tthbbV4pre_nome_TT_TuneCUETP8M1_13TeV-powheg-Py8__fall15MAv2-pu25ns15v1_76r2as_v12_ext3-v1'
config.Data.totalUnits = -1
config.Data.unitsPerJob = 200
config.Data.ignoreLocality = False
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.outLFNDirBase = '/store/user/jpata/tth/VHBBHeppyV21pre_tthbbV4pre_nome'
config.Data.publication = True
config.section_('Site')
config.Site.storageSite = 'T2_CH_CSCS'

