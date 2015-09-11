
#https://twiki.cern.ch/twiki/bin/view/CMS/TTbarHbbRun2ReferenceAnalysis
# Proposed selection steps for dilepton analyses
# Step1a: Apply dilepton triggers
# Step1: Check if the first primary vertex is of good quality
# Step2: >=2 OS leptons (pT>20, |eta|<2.4)
# Step3: mll>20
# Step4: Exclude Z window for ee and mumu
# Step5: >=2 jets (pT>30, |eta|<2.4) and the rest pT>20 GeV
# Step6: MET>=40 for ee and mumu
# Step7: >=1 medium WP b-tagged jet

#dl_cuts = "is_dl==1 && passPV==1 && (abs(leps_pdgId[0])==abs(leps_pdgId[1]) ? met_pt>40 : 1) && sign(leps_pdgId[0])!=sign(leps_pdgId[1])"
sl_cuts = "is_sl==1 && passPV==1"
dl_cuts = "is_dl==1 && passPV==1 && ll_mass>20 && passPV==1 && abs(ll_mass-91.2)>8 && (abs(leps_pdgId[0])==abs(leps_pdgId[1]) ? met_pt>40 : 1) && sign(leps_pdgId[0])!=sign(leps_pdgId[1])"

class Datacard:
    #draw in these categories
    # (name, cut-string, decision variable to use)
    categories = [
        ("dl_j3_t2",        dl_cuts + " && numJets==3 && nBCSVM==2",    "mem_DL_0w2h2t"),
        ("dl_jge3_tge3",    dl_cuts + " && numJets>=3 && nBCSVM==3",    "mem_DL_0w2h2t"),
        ("dl_jge4_t2",      dl_cuts + " && numJets>=4 && nBCSVM==2",    "mem_DL_0w2h2t"),
        ("dl_jge4_tge4",    dl_cuts + " && numJets>=4 && nBCSVM>=4",    "mem_DL_0w2h2t"),

        ("sl_j4_t3",        sl_cuts + " && numJets==4 && nBCSVM==3",    "mem_SL_0w2h2t"),
        ("sl_j4_t4",        sl_cuts + " && numJets==4 && nBCSVM==4",    "mem_SL_0w2h2t"),

        ("sl_j5_t3",        sl_cuts + " && numJets==5 && nBCSVM==3",    "mem_SL_0w2h2t"),
        ("sl_j5_tge4",      sl_cuts + " && numJets==5 && nBCSVM>=4",    "mem_SL_0w2h2t"),


        ("sl_jge6_t2",      sl_cuts + " && numJets>=6 && nBCSVM==2",    "mem_SL_0w2h2t"),
        ("sl_jge6_t3",      sl_cuts + " && numJets>=6 && nBCSVM==3",    "mem_SL_0w2h2t"),
        ("sl_jge6_tge4",    sl_cuts + " && numJets>=6 && nBCSVM>=4",    "mem_SL_0w2h2t"),
    ]

    # Subset of categories we want to use for limit setting
    analysis_categories = [
        #"sl_jge6_t2",
        #"sl_jge6_t3",
        "sl_jge6_tge4"
    ]

    #Draw histograms with these systematic weights
    #The list consists of all systematic weight scenarios that will be evaluated
    #(NAME, WEIGHT) -> will create hist_NAME with weight str (WEIGHT * (cut))
    weights = [
            #Nominal weights
            ("",                    "bTagWeight"),

            #no weights applied
            #("unweighted",          "1.0"),
            
            #only b weight applied
            #("bw",                  "bTagWeight"),
            
            
                        
            #JES, needs variated per-event bTagWeight as well
            ("CMS_scale_jUp",       "bTagWeight_JESUp"),
            ("CMS_scale_jDown",     "bTagWeight_JESDown"),
            
            #CSV variations
            #("CMS_ttH_CSVLFUp",         "bTagWeight_LFUp"),
            #("CMS_ttH_CSVLFDown",       "bTagWeight_LFDown"),
            ("CMS_ttH_CSVHFUp",         "bTagWeight_HFUp"),
            ("CMS_ttH_CSVHFDown",       "bTagWeight_HFDown"),
            #("CMS_ttH_CSVStats1Up",     "bTagWeight_Stats1Up"),
            #("CMS_ttH_CSVStats1Down",   "bTagWeight_Stats1Down"),
            #("CMS_ttH_CSVStats2Up",     "bTagWeight_Stats2Up"),
            #("CMS_ttH_CSVStats2Down",   "bTagWeight_Stats2Down"),
    ]

    # Subset of the reweighted distributions we want to use as syst. shape uncertainties    
    # To avoid copy paste
    common_shape_uncertainties = {
        "CMS_scale_j"       : 1,
        "CMS_ttH_CSVLF"       : 1,
        "CMS_ttH_CSVHF"       : 1,        
        "CMS_ttH_CSVStats1"   : 1,    
        "CMS_ttH_CSVStats2"   : 1,    
    }        
    # nested dictionaries: category/sample/uncertainty/scale
    shape_uncertainties = {
        "sl_jge6_tge4" : {
            "ttH_hbb" : common_shape_uncertainties,
            "ttbarPlus2B" : common_shape_uncertainties,
            "ttbarPlusB" : common_shape_uncertainties,
            "ttbarPlusBBbar" : common_shape_uncertainties,
            "ttbarPlusCCbar" : common_shape_uncertainties,
            "ttbarOther" : common_shape_uncertainties,
        }
    }


    # value: normalization uncertainty
    scale_uncertainties = {
        "sl_jge6_tge4" : {
            "ttH_hbb" : {
                "lumi" : 1.05
            },
            "ttbarPlus2B" : {
                "bgnorm_ttbarPlus2B" : 1.5
            },
            "ttbarPlusB" : {
                "bgnorm_ttbarPlusB" : 1.3
            },
            "ttbarPlusBBbar" : {
                "bgnorm_ttbarPlusBBbar" : 1.3
            },
            "ttbarPlusCCbar" : {
                "bgnorm_ttbarPlusCCbar" : 1.3
            },
            "ttbarOther" : {
                "bgnorm_ttbarOther" : 1.3
            },
    }}


    #Enable the plotting of these samples
    # !!!Important: Signal has to be the first one!!!!
    samples = [
        "ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_hbb",
        #"tth_13tev_amcatnlo_pu20bx25_hbb",
        #"tth_13tev_amcatnlo_pu20bx25_hX",
        "TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_tt2b",
        "TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ttb",
        "TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ttbb",
        "TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ttcc",
        "TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ttll",
        #"ttw_13tev_madgraph_pu20bx25_phys14",
        #"ttz_13tev_madgraph_pu20bx25_phys14"
    ]

    output_filename = "ControlPlots.root"
    output_datacardname = "shapes.txt"

    output_basepath = "./"

    # luminosity we're interested in (measure in pb-1)
    lumi = 10000. # 10fb-1
