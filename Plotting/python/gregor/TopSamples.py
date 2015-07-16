import socket # to get the hostname

if socket.gethostname() == "t3ui12":
    basepath = '/scratch/gregor/'
else:
    basepath = '/Users/gregor/'

files = {}

#files["zprime_m1000_low"] = "ntop_v45_zprime_m1000_low_1p_13tev_phys14_20bx25-tagging"     
#files["zprime_m1000_old"]     = "ntop_v45_zprime_m1000_1p_13tev_phys14_20bx25-tagging"     
#files["zprime_m2000_low"] = "ntop_v45_zprime_m2000_low_1p_13tev_phys14_20bx25-tagging"     
#files["zprime_m2000"]     = "ntop_v45_zprime_m2000_1p_13tev_phys14_20bx25-tagging"     
#files["qcd_170_300"]      = "ntop_v45_qcd_170_300_pythia8_13tev_phys14_20bx25-tagging"
#files["qcd_300_470_old"]      = "ntop_v45_qcd_300_470_pythia8_13tev_phys14_20bx25-tagging"
#files["qcd_600_800"]      = "ntop_v45_qcd_600_800_pythia8_13tev_phys14_20bx25-tagging"
#files["qcd_800_1000"]     = "ntop_v45_qcd_800_1000_pythia8_13tev_phys14_20bx25-tagging"
#files["wjets_lnu_ht_600_inf_200_300"] = "ntop_v45c_wjets_lnu_ht_600_inf_200_300_13tev_phys14_20bx25-tagging"
#files["wjets_lnu_ht_600_inf_300_470"] = "ntop_v45c_wjets_lnu_ht_600_inf_300_470_13tev_phys14_20bx25-tagging"
#files["wjets_lnu_ht_600_inf_600_800"] = "ntop_v45c_wjets_lnu_ht_600_inf_600_800_13tev_phys14_20bx25-tagging"

#files["zprime_m1000"]     = "ntop_v50c_zprime_m1000_1p_13tev_spring15dr74_asympt50ns-tagging"     
#files["qcd_300_470"]      = "ntop_v50_qcd_300_470_13tev_spring15dr74_asympt50ns-tagging"

#files["zprime_m1000_phys14"]     = "ntop_v54b_zprime_m1000_1p_13tev_phys14_20bx25-tagging"     
#files["qcd_300_470_phys14"]      = "ntop_v54b_qcd_300_470_pythia8_13tev_phys14_20bx25-tagging"
#files["qcd_1000_1400_phys14"]      = "ntop_v54c_qcd_1000_1400_pythia8_13tev_phys14_20bx25-tagging"

#files["zprime_m1000"]     = "ntop_v54_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"     
#files["qcd_300_470"]      = "ntop_v54_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging"

#files["zprime_m1000_v1"]     = "ntop_v54_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"     

#files["zprime_m2000"]     = "ntop_v54_zprime_m2000_1p_13tev_spring15dr74_asympt50ns-tagging"     

#files["zprime_m750"]      = "ntop_v55a_zprime_m750_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1000"]     = "ntop_v55a_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1250"]     = "ntop_v55_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000"]     = "ntop_v55_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000_low"] = "ntop_v55_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m3000"]     = "ntop_v55_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"  

#files["qcd_170_300"]   = "ntop_v55a_qcd_170_300_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_300_470"]   = "ntop_v55a_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_470_600"]   = "ntop_v55_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_600_800"]   = "ntop_v55_qcd_600_800_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_800_1000"]  = "ntop_v55_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_1000_1400"] = "ntop_v55_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"


#
#files["zprime_m1250"]     = "ntop_v56_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000"]     = "ntop_v56_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000_low"] = "ntop_v56_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m3000"]     = "ntop_v56_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"  
#
#files["qcd_470_600"]   = "ntop_v56_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_600_800"]   = "ntop_v56_qcd_600_800_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_800_1000"]  = "ntop_v56_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_1000_1400"] = "ntop_v56_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"
#

#
#files["zprime_m750"]      = "ntop_v57b_zprime_m750_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1000"]     = "ntop_v57b_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000"]     = "ntop_v57b_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1250"]     = "ntop_v57b_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000_low"] = "ntop_v57b_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m3000"]     = "ntop_v57b_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"  
#
#files["qcd_170_300"]   = "ntop_v57b_qcd_170_300_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_300_470"]   = "ntop_v57b_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_470_600"]   = "ntop_v57b_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_600_800"]   = "ntop_v57b_qcd_600_800_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_800_1000"]  = "ntop_v57b_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_1000_1400"] = "ntop_v57b_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"
#
#files["zprime_m1000"]  = "ntop_v57b_zprime_m1000_1p_13tev_spring15dr74_asympt50ns-tagging"	
#files["zprime_m2000"]  = "ntop_v57b_zprime_m2000_1p_13tev_spring15dr74_asympt50ns-tagging"	
#files["qcd_300_470"]   = "ntop_v57b_qcd_300_470_13tev_spring15dr74_asympt50ns-tagging" 
#files["qcd_800_1000"]  = "ntop_v57b_qcd_800_1000_13tev_spring15dr74_asympt50ns-tagging" 

# 58 (and previous) had wrong matching at low pT
# 58a fixes this

#files["zprime_m750"]      = "ntop_v58a_zprime_m750_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1000"]     = "ntop_v58a_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m1250"]     = "ntop_v58_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000_low"] = "ntop_v58_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m2000"]     = "ntop_v58_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["zprime_m3000"]     = "ntop_v58_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"  
#files["qcd_170_300"]   = "ntop_v58a_qcd_170_300_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_300_470"]   = "ntop_v58a_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_470_600"]   = "ntop_v58_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"	 
#files["qcd_600_800"]   = "ntop_v57b_qcd_600_800_13tev_spring15dr74_asympt25ns-tagging"	 # !!!! Still waiting for new MC iteration
#files["qcd_800_1000"]  = "ntop_v58_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["qcd_1000_1400"] = "ntop_v58_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"

# PUPPI
files["qcd_300_470_puppi"]   = "ntop_v59b_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging" 
files["zprime_m1000_puppi"]  = "ntop_v59c_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"
	
# Shower Decon Tuning
#files["zprime_m2000_60"]  = "ntop_v60_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["qcd_800_1000_60"]  = "ntop_v60_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["zprime_m2000_60a"] = "ntop_v60a_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["qcd_800_1000_60a"] = "ntop_v60a_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["zprime_m2000_60b"] = "ntop_v60b_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["qcd_800_1000_60b"] = "ntop_v60b_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["zprime_m2000_60c"] = "ntop_v60c_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["qcd_800_1000_60c"] = "ntop_v60c_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
#files["zprime_m2000_60d"] = "ntop_v60d_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
#files["qcd_800_1000_60d"] = "ntop_v60d_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 

# 61
files["zprime_m750"]      = "ntop_v61_zprime_m750_1p_13tev_spring15dr74_asympt25ns-tagging"	
files["zprime_m1000"]     = "ntop_v61_zprime_m1000_1p_13tev_spring15dr74_asympt25ns-tagging"	
files["zprime_m1250"]     = "ntop_v61_zprime_m1250_1p_13tev_spring15dr74_asympt25ns-tagging"	
files["zprime_m2000_low"] = "ntop_v61_zprime_m2000_low_1p_13tev_spring15dr74_asympt25ns-tagging"	
files["zprime_m2000"]     = "ntop_v61_zprime_m2000_1p_13tev_spring15dr74_asympt25ns-tagging"	
files["zprime_m3000"]     = "ntop_v61_zprime_m3000_1p_13tev_spring15dr74_asympt25ns-tagging"  

files["qcd_170_300"]      = "ntop_v61_qcd_170_300_13tev_spring15dr74_asympt25ns-tagging" 
files["qcd_300_470"]      = "ntop_v61_qcd_300_470_13tev_spring15dr74_asympt25ns-tagging" 
files["qcd_470_600"]      = "ntop_v61_qcd_470_600_13tev_spring15dr74_asympt25ns-tagging"	 
files["qcd_800_1000"]     = "ntop_v61_qcd_800_1000_13tev_spring15dr74_asympt25ns-tagging" 
files["qcd_1000_1400"]    = "ntop_v61_qcd_1000_1400_13tev_spring15dr74_asympt25ns-tagging"


weighted_files = {}
for k,v in files.iteritems():
    weighted_files[k] = basepath + v + "-weighted.root"

pairs = { 
#    "pt-200-to-300" : ["zprime_m1000_low", "qcd_170_300"],
#    "pt-300-to-470" : ["zprime_m1000", "qcd_300_470"],
#   "pt-470-to-600" : ["zprime_m1250", "qcd_470_600"],
#    "pt-600-to-800" : ["zprime_m2000_low", "qcd_600_800"],
    "pt-800-to-1000" : ["zprime_m2000", "qcd_800_1000"],
}

# [Minimal pT, Maximal pT, |eta|]
ranges = {
    "zprime_m750"      : [201, 299,   2.4, 0.8, "ca15"],
    "zprime_m1000_low" : [201, 299,   2.4, 0.8, "ca15"],
    "zprime_m1000"     : [301, 469,   2.4, 0.8, "ca15"],
    "zprime_m1000_puppi": [301, 469,   2.4, 0.8, "ca15"],
    "zprime_m1000_phys14" : [301, 469,   2.4, 0.8, "ca15"],
    "zprime_m1000_v1" : [301, 469,   2.4, 0.8, "ca15"],
    "zprime_m1250"     : [471, 599,   2.1, 0.6, "ak08"], 
    "zprime_m2000_low" : [601, 799,   2.1, 0.6, "ak08"],
    "zprime_m2000"     : [801, 999,   1.5, 0.6, "ak08"],
    "zprime_m3000"     : [1001, 1399, 1.5, 0.6, "ak08"], 
    "zprime_m4000"     : [1401, 1799, 1.3, 0.6, "ak08"],
    
    "qcd_170_300"      : [201, 299, 2.4, 0.8, "ca15"],
    "qcd_300_470"      : [301, 469, 2.4, 0.8, "ca15"],
    "qcd_300_470_puppi": [301, 469, 2.4, 0.8, "ca15"],
    "qcd_300_470_phys14"  : [301, 469, 2.4, 0.8, "ca15"],
    "qcd_470_600"      : [471, 599, 2.1, 0.6, "ak08"],
    "qcd_600_800"      : [601, 799, 2.1, 0.6, "ak08"],
    "qcd_800_1000"     : [801, 999, 1.5, 0.6, "ak08"],
    "qcd_1000_1400"     : [1001, 1399, 1.3, 0.6, "ak08"],
    "qcd_1000_1400_phys14"     : [1001, 1399, 1.3, 0.6, "ak08"],

    "wjets_lnu_ht_600_inf_200_300" : [201, 299, 2.4, 0.8, "ca15"],
    "wjets_lnu_ht_600_inf_300_470" : [301, 469, 2.4, 0.8, "ca15"],   
    "wjets_lnu_ht_600_inf_600_800" : [601, 799, 2.1, 0.6, "ak08"],
}

sample_names = {"zprime_m750"      : "Top, 200..300",
                "zprime_m1000"     : "Top, 300..470",
                "zprime_m1000_phys14" : "Phys14, Top, 300..470",
                "zprime_m1000_v1" : "Spring15 (v1), Top, 300..470",
                "zprime_m1250"     : "Top, 470..600", 
                "zprime_m2000_low" : "Top, 600..800",
                "zprime_m2000"     : "Top, 800..1000",
                "zprime_m3000"     : "Top, 1000..1400", 
                "zprime_m4000"     : "Top, 1400..2000",
                
                "qcd_170_300"      : "QCD, 200..300",
                "qcd_300_470"      : "QCD, 300..470",
                "qcd_300_470_phys14"  : "Phys14, QCD, 300..470",
                "qcd_470_600"      : "QCD, 470..600",
                "qcd_600_800"      : "QCD, 600..800",
                "qcd_800_1000"     : "QCD, 800..1000",
                "qcd_1000_1400"     : "QCD, 1000..1400",
                "qcd_1000_1400_phys14"     : "QCD, 1000..1400",
                
                "wjets_lnu_ht_600_inf_200_300" : "W+Jets, 200..300",
                "wjets_lnu_ht_600_inf_300_470" : "W+Jets, 300..470",
                "wjets_lnu_ht_600_inf_600_800" : "W+Jets, 600..800",
}

other_sample_names = {
    "zprime_m750"     : "Spring15, Signal (200..300 GeV)",                      
    "zprime_m1000_low" : "Signal (200..300 GeV)",                      
    "zprime_m1000"     : "Spring15, Signal (300..470 GeV)",                      
    "zprime_m1000_phys14"  : "Phys14, Signal (300..470 GeV)",                      
    "zprime_m1000_v1"  : "Spring15 (v1), Signal (300..470 GeV)",                 
    "zprime_m1250"     : "Spring15, Signal (470..600 GeV)",                      
    "zprime_m2000_low" : "Spring15, Signal (600..800 GeV)",                      
    "zprime_m2000"     : "Spring15, Signal (800..1000 GeV)",                      
    "zprime_m3000"     : "Spring15, Signal (1000..1400 GeV)",                      
    "qcd_170_300"      : "BG (200..300 GeV)",
    "qcd_300_470"      : "Spring15, BG (300..470 GeV)",
    "qcd_300_470_phys14"  : "Phys14, BG (300..470 GeV)",
    "qcd_600_800"      : "BG (600..800 GeV)",
    "qcd_800_1000"     : "BG (800..1000 GeV)",
    "qcd_1000_1400"     : "BG (1000..1400 GeV)",
    "qcd_1000_1400_phys14"     : "BG (1000..1400 GeV)",
    "wjets_lnu_ht_600_inf_200_300" : "BG-W (200..300 GeV)", 
    "wjets_lnu_ht_600_inf_300_470" : "BG-W (300..470 GeV)", 
    "wjets_lnu_ht_600_inf_600_800" : "BG-W (600..800 GeV)",   
            }

other2_sample_names = {
    "zprime_m750"      : "Top, 200<p_{T}<300",                      
    "zprime_m1000"     : "Top, 300<p_{T}<470",                      
    "zprime_m1000_puppi": "PUPPI, Top, 300< p_{T} < 470",                      
    "zprime_m1250"     : "Top, 470<p_{T}<600",                      
    "zprime_m2000_low" : "Top, 600<p_{T}<800",                      
    "zprime_m2000"     : "Top, 800<p_{T}<1000",                      
    "zprime_m3000"     : "Top, 1000<p_{T}<1400",                      

    "qcd_170_300"      : "QCD, 200<p_{T}<300",
    "qcd_300_470"      : "QCD, 300<p_{T}<470",
    "qcd_300_470_puppi": "PUPPI, QCD, 300 <p_{T} < 470",
    "qcd_470_600"      : "QCD, 470<p_{T}<600",
    "qcd_600_800"      : "QCD, 600<p_{T}<800",
    "qcd_800_1000"     : "QCD, 800<p_{T}<1000",
    "qcd_1000_1400"    : "QCD, 1000<p_{T}<1400",

}

other3_sample_names = {
    "zprime_m750"      : "Signal, 200-300 GeV",                      
    "zprime_m1000"     : "Signal, 300-470 GeV",                      
    "zprime_m1250"     : "Signal, 470-600 GeV",                      
    "zprime_m2000_low" : "Signal, 600-800 GeV",                      
    "zprime_m2000"     : "Signal, 0.8-1.0 TeV",                      
    "zprime_m3000"     : "Signal, 1.0-1.4 TeV",                      

    "qcd_170_300"      : "BG, 200-300 GeV",
    "qcd_300_470"      : "BG, 300-470 GeV",
    "qcd_470_600"      : "BG, 470-600 GeV",
    "qcd_600_800"      : "BG, 600-800 GeV",
    "qcd_800_1000"     : "BG, 0.8-1.0 TeV",
    "qcd_1000_1400"    : "BG, 1.0-1.4 TeV",
}



fiducial_cuts = {}
pretty_fiducial_cuts = {}
nosize_fiducial_cuts = {}
for k,v in ranges.iteritems():
    fiducial_cuts[k] = "((pt>{0})&&(pt<{1})&&(fabs(eta)<{2})&&(top_size<{3}))".format(v[0], v[1], v[2], v[3])
    nosize_fiducial_cuts[k] = "((pt>{0})&&(pt<{1})&&(fabs(eta)<{2}))".format(v[0], v[1], v[2])
    pretty_fiducial_cuts[k] = "{0} < p_{{T}} < {1}, |#eta| < {2}".format(v[0]-1, v[1]+1, v[2])


