class GenBQuarkFromHafterISR:
    def __init__(self, tree, n):
        self.pdgId = tree.GenBQuarkFromHafterISR_pdgId[n];
        self.pt = tree.GenBQuarkFromHafterISR_pt[n];
        self.eta = tree.GenBQuarkFromHafterISR_eta[n];
        self.phi = tree.GenBQuarkFromHafterISR_phi[n];
        self.mass = tree.GenBQuarkFromHafterISR_mass[n];
        self.charge = tree.GenBQuarkFromHafterISR_charge[n];
        self.status = tree.GenBQuarkFromHafterISR_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenBQuarkFromHafterISR(tree, i) for i in range(tree.nGenBQuarkFromHafterISR)]
class pileUpVertex_ptHat:
    def __init__(self, tree, n):
        self.pileUpVertex_ptHat = tree.pileUpVertex_ptHat[n];
        pass
    @staticmethod
    def make_array(tree):
        return [pileUpVertex_ptHat(tree, i) for i in range(tree.npileUpVertex_ptHat)]
class trgObjects_hltMET70:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltMET70(tree, i) for i in range(tree.ntrgObjects_hltMET70)]
class trgObjects_hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet(tree, i) for i in range(tree.ntrgObjects_hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet)]
class trgObjects_hltBTagPFCSVp11DoubleWithMatching:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagPFCSVp11DoubleWithMatching(tree, i) for i in range(tree.ntrgObjects_hltBTagPFCSVp11DoubleWithMatching)]
class GenLepFromTop:
    def __init__(self, tree, n):
        self.pdgId = tree.GenLepFromTop_pdgId[n];
        self.pt = tree.GenLepFromTop_pt[n];
        self.eta = tree.GenLepFromTop_eta[n];
        self.phi = tree.GenLepFromTop_phi[n];
        self.mass = tree.GenLepFromTop_mass[n];
        self.charge = tree.GenLepFromTop_charge[n];
        self.status = tree.GenLepFromTop_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenLepFromTop(tree, i) for i in range(tree.nGenLepFromTop)]
class ajidxaddJetsdR08:
    def __init__(self, tree, n):
        self.ajidxaddJetsdR08 = tree.ajidxaddJetsdR08[n];
        pass
    @staticmethod
    def make_array(tree):
        return [ajidxaddJetsdR08(tree, i) for i in range(tree.najidxaddJetsdR08)]
class SubjetCA15softdrop:
    def __init__(self, tree, n):
        self.pt = tree.SubjetCA15softdrop_pt[n];
        self.eta = tree.SubjetCA15softdrop_eta[n];
        self.phi = tree.SubjetCA15softdrop_phi[n];
        self.mass = tree.SubjetCA15softdrop_mass[n];
        self.btag = tree.SubjetCA15softdrop_btag[n];
        self.fromFJ = tree.SubjetCA15softdrop_fromFJ[n];
        pass
    @staticmethod
    def make_array(tree):
        return [SubjetCA15softdrop(tree, i) for i in range(tree.nSubjetCA15softdrop)]
class trgObjects_hltIsoMu20:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltIsoMu20_pt[n];
        self.eta = tree.trgObjects_hltIsoMu20_eta[n];
        self.phi = tree.trgObjects_hltIsoMu20_phi[n];
        self.mass = tree.trgObjects_hltIsoMu20_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltIsoMu20(tree, i) for i in range(tree.ntrgObjects_hltIsoMu20)]
class trgObjects_hltQuadCentralJet30:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltQuadCentralJet30(tree, i) for i in range(tree.ntrgObjects_hltQuadCentralJet30)]
class GenVbosonsRecovered:
    def __init__(self, tree, n):
        self.pdgId = tree.GenVbosonsRecovered_pdgId[n];
        self.pt = tree.GenVbosonsRecovered_pt[n];
        self.eta = tree.GenVbosonsRecovered_eta[n];
        self.phi = tree.GenVbosonsRecovered_phi[n];
        self.mass = tree.GenVbosonsRecovered_mass[n];
        self.charge = tree.GenVbosonsRecovered_charge[n];
        self.status = tree.GenVbosonsRecovered_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenVbosonsRecovered(tree, i) for i in range(tree.nGenVbosonsRecovered)]
class hJidx_sortcsv:
    def __init__(self, tree, n):
        self.hJidx_sortcsv = tree.hJidx_sortcsv[n];
        pass
    @staticmethod
    def make_array(tree):
        return [hJidx_sortcsv(tree, i) for i in range(tree.nhJidx_sortcsv)]
class trgObjects_hltL1sQuadJetCIorTripleJetVBFIorHTT:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltL1sQuadJetCIorTripleJetVBFIorHTT(tree, i) for i in range(tree.ntrgObjects_hltL1sQuadJetCIorTripleJetVBFIorHTT)]
class GenTausRecovered:
    def __init__(self, tree, n):
        self.pdgId = tree.GenTausRecovered_pdgId[n];
        self.pt = tree.GenTausRecovered_pt[n];
        self.eta = tree.GenTausRecovered_eta[n];
        self.phi = tree.GenTausRecovered_phi[n];
        self.mass = tree.GenTausRecovered_mass[n];
        self.charge = tree.GenTausRecovered_charge[n];
        self.status = tree.GenTausRecovered_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenTausRecovered(tree, i) for i in range(tree.nGenTausRecovered)]
class SubjetCA15softdropz2b1:
    def __init__(self, tree, n):
        self.pt = tree.SubjetCA15softdropz2b1_pt[n];
        self.eta = tree.SubjetCA15softdropz2b1_eta[n];
        self.phi = tree.SubjetCA15softdropz2b1_phi[n];
        self.mass = tree.SubjetCA15softdropz2b1_mass[n];
        self.btag = tree.SubjetCA15softdropz2b1_btag[n];
        self.fromFJ = tree.SubjetCA15softdropz2b1_fromFJ[n];
        pass
    @staticmethod
    def make_array(tree):
        return [SubjetCA15softdropz2b1(tree, i) for i in range(tree.nSubjetCA15softdropz2b1)]
class hJCidx:
    def __init__(self, tree, n):
        self.hJCidx = tree.hJCidx[n];
        pass
    @staticmethod
    def make_array(tree):
        return [hJCidx(tree, i) for i in range(tree.nhJCidx)]
class GenTop:
    def __init__(self, tree, n):
        self.charge = tree.GenTop_charge[n];
        self.status = tree.GenTop_status[n];
        self.pdgId = tree.GenTop_pdgId[n];
        self.pt = tree.GenTop_pt[n];
        self.eta = tree.GenTop_eta[n];
        self.phi = tree.GenTop_phi[n];
        self.mass = tree.GenTop_mass[n];
        self.decayMode = tree.GenTop_decayMode[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenTop(tree, i) for i in range(tree.nGenTop)]
class aJidx:
    def __init__(self, tree, n):
        self.aJidx = tree.aJidx[n];
        pass
    @staticmethod
    def make_array(tree):
        return [aJidx(tree, i) for i in range(tree.naJidx)]
class GenLepFromTau:
    def __init__(self, tree, n):
        self.pdgId = tree.GenLepFromTau_pdgId[n];
        self.pt = tree.GenLepFromTau_pt[n];
        self.eta = tree.GenLepFromTau_eta[n];
        self.phi = tree.GenLepFromTau_phi[n];
        self.mass = tree.GenLepFromTau_mass[n];
        self.charge = tree.GenLepFromTau_charge[n];
        self.status = tree.GenLepFromTau_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenLepFromTau(tree, i) for i in range(tree.nGenLepFromTau)]
class GenNuFromTop:
    def __init__(self, tree, n):
        self.pdgId = tree.GenNuFromTop_pdgId[n];
        self.pt = tree.GenNuFromTop_pt[n];
        self.eta = tree.GenNuFromTop_eta[n];
        self.phi = tree.GenNuFromTop_phi[n];
        self.mass = tree.GenNuFromTop_mass[n];
        self.charge = tree.GenNuFromTop_charge[n];
        self.status = tree.GenNuFromTop_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenNuFromTop(tree, i) for i in range(tree.nGenNuFromTop)]
class trgObjects_hltPFDoubleJetLooseID76:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFDoubleJetLooseID76(tree, i) for i in range(tree.ntrgObjects_hltPFDoubleJetLooseID76)]
class trgObjects_hltBTagPFCSVp016SingleWithMatching:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagPFCSVp016SingleWithMatching(tree, i) for i in range(tree.ntrgObjects_hltBTagPFCSVp016SingleWithMatching)]
class GenVbosons:
    def __init__(self, tree, n):
        self.pdgId = tree.GenVbosons_pdgId[n];
        self.pt = tree.GenVbosons_pt[n];
        self.eta = tree.GenVbosons_eta[n];
        self.phi = tree.GenVbosons_phi[n];
        self.mass = tree.GenVbosons_mass[n];
        self.charge = tree.GenVbosons_charge[n];
        self.status = tree.GenVbosons_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenVbosons(tree, i) for i in range(tree.nGenVbosons)]
class softActivityVHJets:
    def __init__(self, tree, n):
        self.pt = tree.softActivityVHJets_pt[n];
        self.eta = tree.softActivityVHJets_eta[n];
        self.phi = tree.softActivityVHJets_phi[n];
        self.mass = tree.softActivityVHJets_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [softActivityVHJets(tree, i) for i in range(tree.nsoftActivityVHJets)]
class trgObjects_hltQuadPFCentralJetLooseID30:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltQuadPFCentralJetLooseID30(tree, i) for i in range(tree.ntrgObjects_hltQuadPFCentralJetLooseID30)]
class trgObjects_caloMhtNoPU:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_caloMhtNoPU_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_caloMhtNoPU(tree, i) for i in range(tree.ntrgObjects_caloMhtNoPU)]
class trgObjects_hltEle25eta2p1WPLoose:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltEle25eta2p1WPLoose_pt[n];
        self.eta = tree.trgObjects_hltEle25eta2p1WPLoose_eta[n];
        self.phi = tree.trgObjects_hltEle25eta2p1WPLoose_phi[n];
        self.mass = tree.trgObjects_hltEle25eta2p1WPLoose_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltEle25eta2p1WPLoose(tree, i) for i in range(tree.ntrgObjects_hltEle25eta2p1WPLoose)]
class SubjetAK08softdrop:
    def __init__(self, tree, n):
        self.pt = tree.SubjetAK08softdrop_pt[n];
        self.eta = tree.SubjetAK08softdrop_eta[n];
        self.phi = tree.SubjetAK08softdrop_phi[n];
        self.mass = tree.SubjetAK08softdrop_mass[n];
        self.btag = tree.SubjetAK08softdrop_btag[n];
        pass
    @staticmethod
    def make_array(tree):
        return [SubjetAK08softdrop(tree, i) for i in range(tree.nSubjetAK08softdrop)]
class trgObjects_hltDoublePFCentralJetLooseID90:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltDoublePFCentralJetLooseID90(tree, i) for i in range(tree.ntrgObjects_hltDoublePFCentralJetLooseID90)]
class GenLep:
    def __init__(self, tree, n):
        self.pdgId = tree.GenLep_pdgId[n];
        self.pt = tree.GenLep_pt[n];
        self.eta = tree.GenLep_eta[n];
        self.phi = tree.GenLep_phi[n];
        self.mass = tree.GenLep_mass[n];
        self.charge = tree.GenLep_charge[n];
        self.status = tree.GenLep_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenLep(tree, i) for i in range(tree.nGenLep)]
class trgObjects_caloJets:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_caloJets_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_caloJets(tree, i) for i in range(tree.ntrgObjects_caloJets)]
class trgObjects_hltPFSingleJetLooseID92:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFSingleJetLooseID92(tree, i) for i in range(tree.ntrgObjects_hltPFSingleJetLooseID92)]
class GenHadTaus:
    def __init__(self, tree, n):
        self.charge = tree.GenHadTaus_charge[n];
        self.status = tree.GenHadTaus_status[n];
        self.pdgId = tree.GenHadTaus_pdgId[n];
        self.pt = tree.GenHadTaus_pt[n];
        self.eta = tree.GenHadTaus_eta[n];
        self.phi = tree.GenHadTaus_phi[n];
        self.mass = tree.GenHadTaus_mass[n];
        self.decayMode = tree.GenHadTaus_decayMode[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenHadTaus(tree, i) for i in range(tree.nGenHadTaus)]
class trgObjects_hltL1sETM50ToETM100IorETM60Jet60dPhiMin0p4IorDoubleJetC60ETM60:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltL1sETM50ToETM100IorETM60Jet60dPhiMin0p4IorDoubleJetC60ETM60(tree, i) for i in range(tree.ntrgObjects_hltL1sETM50ToETM100IorETM60Jet60dPhiMin0p4IorDoubleJetC60ETM60)]
class trgObjects_hltEle25WPTight:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltEle25WPTight_pt[n];
        self.eta = tree.trgObjects_hltEle25WPTight_eta[n];
        self.phi = tree.trgObjects_hltEle25WPTight_phi[n];
        self.mass = tree.trgObjects_hltEle25WPTight_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltEle25WPTight(tree, i) for i in range(tree.ntrgObjects_hltEle25WPTight)]
class trgObjects_pfJets:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_pfJets_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_pfJets(tree, i) for i in range(tree.ntrgObjects_pfJets)]
class SubjetCA15subjetfiltered:
    def __init__(self, tree, n):
        self.pt = tree.SubjetCA15subjetfiltered_pt[n];
        self.eta = tree.SubjetCA15subjetfiltered_eta[n];
        self.phi = tree.SubjetCA15subjetfiltered_phi[n];
        self.mass = tree.SubjetCA15subjetfiltered_mass[n];
        self.btag = tree.SubjetCA15subjetfiltered_btag[n];
        self.fromFJ = tree.SubjetCA15subjetfiltered_fromFJ[n];
        pass
    @staticmethod
    def make_array(tree):
        return [SubjetCA15subjetfiltered(tree, i) for i in range(tree.nSubjetCA15subjetfiltered)]
class vLeptons:
    def __init__(self, tree, n):
        self.charge = tree.vLeptons_charge[n];
        self.tightId = tree.vLeptons_tightId[n];
        self.eleCutIdCSA14_25ns_v1 = tree.vLeptons_eleCutIdCSA14_25ns_v1[n];
        self.eleCutIdCSA14_50ns_v1 = tree.vLeptons_eleCutIdCSA14_50ns_v1[n];
        self.eleCutIdSpring15_25ns_v1 = tree.vLeptons_eleCutIdSpring15_25ns_v1[n];
        self.dxy = tree.vLeptons_dxy[n];
        self.dz = tree.vLeptons_dz[n];
        self.edxy = tree.vLeptons_edxy[n];
        self.edz = tree.vLeptons_edz[n];
        self.ip3d = tree.vLeptons_ip3d[n];
        self.sip3d = tree.vLeptons_sip3d[n];
        self.convVeto = tree.vLeptons_convVeto[n];
        self.lostHits = tree.vLeptons_lostHits[n];
        self.relIso03 = tree.vLeptons_relIso03[n];
        self.relIso04 = tree.vLeptons_relIso04[n];
        self.miniRelIso = tree.vLeptons_miniRelIso[n];
        self.relIsoAn04 = tree.vLeptons_relIsoAn04[n];
        self.tightCharge = tree.vLeptons_tightCharge[n];
        self.mcMatchId = tree.vLeptons_mcMatchId[n];
        self.mcMatchAny = tree.vLeptons_mcMatchAny[n];
        self.mcMatchTau = tree.vLeptons_mcMatchTau[n];
        self.mcPt = tree.vLeptons_mcPt[n];
        self.mediumMuonId = tree.vLeptons_mediumMuonId[n];
        self.pdgId = tree.vLeptons_pdgId[n];
        self.pt = tree.vLeptons_pt[n];
        self.eta = tree.vLeptons_eta[n];
        self.phi = tree.vLeptons_phi[n];
        self.mass = tree.vLeptons_mass[n];
        self.looseIdSusy = tree.vLeptons_looseIdSusy[n];
        self.looseIdPOG = tree.vLeptons_looseIdPOG[n];
        self.chargedHadRelIso03 = tree.vLeptons_chargedHadRelIso03[n];
        self.chargedHadRelIso04 = tree.vLeptons_chargedHadRelIso04[n];
        self.eleSieie = tree.vLeptons_eleSieie[n];
        self.eleDEta = tree.vLeptons_eleDEta[n];
        self.eleDPhi = tree.vLeptons_eleDPhi[n];
        self.eleHoE = tree.vLeptons_eleHoE[n];
        self.eleMissingHits = tree.vLeptons_eleMissingHits[n];
        self.eleChi2 = tree.vLeptons_eleChi2[n];
        self.convVetoFull = tree.vLeptons_convVetoFull[n];
        self.eleMVArawSpring15Trig = tree.vLeptons_eleMVArawSpring15Trig[n];
        self.eleMVAIdSpring15Trig = tree.vLeptons_eleMVAIdSpring15Trig[n];
        self.eleMVArawSpring15NonTrig = tree.vLeptons_eleMVArawSpring15NonTrig[n];
        self.eleMVAIdSpring15NonTrig = tree.vLeptons_eleMVAIdSpring15NonTrig[n];
        self.nStations = tree.vLeptons_nStations[n];
        self.trkKink = tree.vLeptons_trkKink[n];
        self.segmentCompatibility = tree.vLeptons_segmentCompatibility[n];
        self.caloCompatibility = tree.vLeptons_caloCompatibility[n];
        self.globalTrackChi2 = tree.vLeptons_globalTrackChi2[n];
        self.nChamberHits = tree.vLeptons_nChamberHits[n];
        self.isPFMuon = tree.vLeptons_isPFMuon[n];
        self.isGlobalMuon = tree.vLeptons_isGlobalMuon[n];
        self.isTrackerMuon = tree.vLeptons_isTrackerMuon[n];
        self.pixelHits = tree.vLeptons_pixelHits[n];
        self.trackerLayers = tree.vLeptons_trackerLayers[n];
        self.pixelLayers = tree.vLeptons_pixelLayers[n];
        self.mvaTTH = tree.vLeptons_mvaTTH[n];
        self.jetOverlapIdx = tree.vLeptons_jetOverlapIdx[n];
        self.jetPtRatio = tree.vLeptons_jetPtRatio[n];
        self.jetBTagCSV = tree.vLeptons_jetBTagCSV[n];
        self.jetDR = tree.vLeptons_jetDR[n];
        self.mvaTTHjetPtRatio = tree.vLeptons_mvaTTHjetPtRatio[n];
        self.mvaTTHjetBTagCSV = tree.vLeptons_mvaTTHjetBTagCSV[n];
        self.mvaTTHjetDR = tree.vLeptons_mvaTTHjetDR[n];
        self.pfRelIso03 = tree.vLeptons_pfRelIso03[n];
        self.pfRelIso04 = tree.vLeptons_pfRelIso04[n];
        self.etaSc = tree.vLeptons_etaSc[n];
        self.eleExpMissingInnerHits = tree.vLeptons_eleExpMissingInnerHits[n];
        self.eleooEmooP = tree.vLeptons_eleooEmooP[n];
        self.dr03TkSumPt = tree.vLeptons_dr03TkSumPt[n];
        self.eleEcalClusterIso = tree.vLeptons_eleEcalClusterIso[n];
        self.eleHcalClusterIso = tree.vLeptons_eleHcalClusterIso[n];
        self.miniIsoCharged = tree.vLeptons_miniIsoCharged[n];
        self.miniIsoNeutral = tree.vLeptons_miniIsoNeutral[n];
        self.mvaTTHjetPtRel = tree.vLeptons_mvaTTHjetPtRel[n];
        self.mvaTTHjetNDauChargedMVASel = tree.vLeptons_mvaTTHjetNDauChargedMVASel[n];
        self.uncalibratedPt = tree.vLeptons_uncalibratedPt[n];
        self.SF_IsoLoose = tree.vLeptons_SF_IsoLoose[n];
        self.SFerr_IsoLoose = tree.vLeptons_SFerr_IsoLoose[n];
        self.SF_IsoTight = tree.vLeptons_SF_IsoTight[n];
        self.SFerr_IsoTight = tree.vLeptons_SFerr_IsoTight[n];
        self.SF_IdCutLoose = tree.vLeptons_SF_IdCutLoose[n];
        self.SFerr_IdCutLoose = tree.vLeptons_SFerr_IdCutLoose[n];
        self.SF_IdCutTight = tree.vLeptons_SF_IdCutTight[n];
        self.SFerr_IdCutTight = tree.vLeptons_SFerr_IdCutTight[n];
        self.SF_IdMVALoose = tree.vLeptons_SF_IdMVALoose[n];
        self.SFerr_IdMVALoose = tree.vLeptons_SFerr_IdMVALoose[n];
        self.SF_IdMVATight = tree.vLeptons_SF_IdMVATight[n];
        self.SFerr_IdMVATight = tree.vLeptons_SFerr_IdMVATight[n];
        self.SF_HLT_RunD4p3 = tree.vLeptons_SF_HLT_RunD4p3[n];
        self.SFerr_HLT_RunD4p3 = tree.vLeptons_SFerr_HLT_RunD4p3[n];
        self.SF_HLT_RunD4p2 = tree.vLeptons_SF_HLT_RunD4p2[n];
        self.SFerr_HLT_RunD4p2 = tree.vLeptons_SFerr_HLT_RunD4p2[n];
        self.SF_HLT_RunC = tree.vLeptons_SF_HLT_RunC[n];
        self.SFerr_HLT_RunC = tree.vLeptons_SFerr_HLT_RunC[n];
        self.Eff_HLT_RunD4p3 = tree.vLeptons_Eff_HLT_RunD4p3[n];
        self.Efferr_HLT_RunD4p3 = tree.vLeptons_Efferr_HLT_RunD4p3[n];
        self.Eff_HLT_RunD4p2 = tree.vLeptons_Eff_HLT_RunD4p2[n];
        self.Efferr_HLT_RunD4p2 = tree.vLeptons_Efferr_HLT_RunD4p2[n];
        self.Eff_HLT_RunC = tree.vLeptons_Eff_HLT_RunC[n];
        self.Efferr_HLT_RunC = tree.vLeptons_Efferr_HLT_RunC[n];
        pass
    @staticmethod
    def make_array(tree):
        return [vLeptons(tree, i) for i in range(tree.nvLeptons)]
class trgObjects_hltBTagCaloCSVp014DoubleWithMatching:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltBTagCaloCSVp014DoubleWithMatching_pt[n];
        self.eta = tree.trgObjects_hltBTagCaloCSVp014DoubleWithMatching_eta[n];
        self.phi = tree.trgObjects_hltBTagCaloCSVp014DoubleWithMatching_phi[n];
        self.mass = tree.trgObjects_hltBTagCaloCSVp014DoubleWithMatching_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagCaloCSVp014DoubleWithMatching(tree, i) for i in range(tree.ntrgObjects_hltBTagCaloCSVp014DoubleWithMatching)]
class pileUpVertex_z:
    def __init__(self, tree, n):
        self.pileUpVertex_z = tree.pileUpVertex_z[n];
        pass
    @staticmethod
    def make_array(tree):
        return [pileUpVertex_z(tree, i) for i in range(tree.npileUpVertex_z)]
class trgObjects_pfMht:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_pfMht_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_pfMht(tree, i) for i in range(tree.ntrgObjects_pfMht)]
class GenBQuarkFromTop:
    def __init__(self, tree, n):
        self.pdgId = tree.GenBQuarkFromTop_pdgId[n];
        self.pt = tree.GenBQuarkFromTop_pt[n];
        self.eta = tree.GenBQuarkFromTop_eta[n];
        self.phi = tree.GenBQuarkFromTop_phi[n];
        self.mass = tree.GenBQuarkFromTop_mass[n];
        self.charge = tree.GenBQuarkFromTop_charge[n];
        self.status = tree.GenBQuarkFromTop_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenBQuarkFromTop(tree, i) for i in range(tree.nGenBQuarkFromTop)]
class GenHiggsBoson:
    def __init__(self, tree, n):
        self.pdgId = tree.GenHiggsBoson_pdgId[n];
        self.pt = tree.GenHiggsBoson_pt[n];
        self.eta = tree.GenHiggsBoson_eta[n];
        self.phi = tree.GenHiggsBoson_phi[n];
        self.mass = tree.GenHiggsBoson_mass[n];
        self.charge = tree.GenHiggsBoson_charge[n];
        self.status = tree.GenHiggsBoson_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenHiggsBoson(tree, i) for i in range(tree.nGenHiggsBoson)]
class LHE_weights_scale:
    def __init__(self, tree, n):
        self.id = tree.LHE_weights_scale_id[n];
        self.wgt = tree.LHE_weights_scale_wgt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [LHE_weights_scale(tree, i) for i in range(tree.nLHE_weights_scale)]
class GenLepFromTauRecovered:
    def __init__(self, tree, n):
        self.pdgId = tree.GenLepFromTauRecovered_pdgId[n];
        self.pt = tree.GenLepFromTauRecovered_pt[n];
        self.eta = tree.GenLepFromTauRecovered_eta[n];
        self.phi = tree.GenLepFromTauRecovered_phi[n];
        self.mass = tree.GenLepFromTauRecovered_mass[n];
        self.charge = tree.GenLepFromTauRecovered_charge[n];
        self.status = tree.GenLepFromTauRecovered_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenLepFromTauRecovered(tree, i) for i in range(tree.nGenLepFromTauRecovered)]
class FatjetCA15pruned:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15pruned_pt[n];
        self.eta = tree.FatjetCA15pruned_eta[n];
        self.phi = tree.FatjetCA15pruned_phi[n];
        self.mass = tree.FatjetCA15pruned_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15pruned(tree, i) for i in range(tree.nFatjetCA15pruned)]
class trgObjects_hltVBFCaloJetEtaSortedMqq150Deta1p5:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltVBFCaloJetEtaSortedMqq150Deta1p5(tree, i) for i in range(tree.ntrgObjects_hltVBFCaloJetEtaSortedMqq150Deta1p5)]
class trgObjects_caloMht:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_caloMht_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_caloMht(tree, i) for i in range(tree.ntrgObjects_caloMht)]
class trgObjects_hltDoubleCentralJet90:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltDoubleCentralJet90(tree, i) for i in range(tree.ntrgObjects_hltDoubleCentralJet90)]
class GenJet:
    def __init__(self, tree, n):
        self.charge = tree.GenJet_charge[n];
        self.status = tree.GenJet_status[n];
        self.pdgId = tree.GenJet_pdgId[n];
        self.pt = tree.GenJet_pt[n];
        self.eta = tree.GenJet_eta[n];
        self.phi = tree.GenJet_phi[n];
        self.mass = tree.GenJet_mass[n];
        self.numBHadrons = tree.GenJet_numBHadrons[n];
        self.numCHadrons = tree.GenJet_numCHadrons[n];
        self.numBHadronsFromTop = tree.GenJet_numBHadronsFromTop[n];
        self.numCHadronsFromTop = tree.GenJet_numCHadronsFromTop[n];
        self.numBHadronsAfterTop = tree.GenJet_numBHadronsAfterTop[n];
        self.numCHadronsAfterTop = tree.GenJet_numCHadronsAfterTop[n];
        self.wNuPt = tree.GenJet_wNuPt[n];
        self.wNuEta = tree.GenJet_wNuEta[n];
        self.wNuPhi = tree.GenJet_wNuPhi[n];
        self.wNuM = tree.GenJet_wNuM[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenJet(tree, i) for i in range(tree.nGenJet)]
class trgObjects_hltDoublePFJetsC100:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltDoublePFJetsC100_pt[n];
        self.eta = tree.trgObjects_hltDoublePFJetsC100_eta[n];
        self.phi = tree.trgObjects_hltDoublePFJetsC100_phi[n];
        self.mass = tree.trgObjects_hltDoublePFJetsC100_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltDoublePFJetsC100(tree, i) for i in range(tree.ntrgObjects_hltDoublePFJetsC100)]
class SubjetCA15pruned:
    def __init__(self, tree, n):
        self.pt = tree.SubjetCA15pruned_pt[n];
        self.eta = tree.SubjetCA15pruned_eta[n];
        self.phi = tree.SubjetCA15pruned_phi[n];
        self.mass = tree.SubjetCA15pruned_mass[n];
        self.btag = tree.SubjetCA15pruned_btag[n];
        self.fromFJ = tree.SubjetCA15pruned_fromFJ[n];
        pass
    @staticmethod
    def make_array(tree):
        return [SubjetCA15pruned(tree, i) for i in range(tree.nSubjetCA15pruned)]
class trgObjects_caloMet:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_caloMet_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_caloMet(tree, i) for i in range(tree.ntrgObjects_caloMet)]
class FatjetCA15ungroomed:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15ungroomed_pt[n];
        self.eta = tree.FatjetCA15ungroomed_eta[n];
        self.phi = tree.FatjetCA15ungroomed_phi[n];
        self.mass = tree.FatjetCA15ungroomed_mass[n];
        self.tau1 = tree.FatjetCA15ungroomed_tau1[n];
        self.tau2 = tree.FatjetCA15ungroomed_tau2[n];
        self.tau3 = tree.FatjetCA15ungroomed_tau3[n];
        self.bbtag = tree.FatjetCA15ungroomed_bbtag[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15ungroomed(tree, i) for i in range(tree.nFatjetCA15ungroomed)]
class trgObjects_pfMet:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_pfMet_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_pfMet(tree, i) for i in range(tree.ntrgObjects_pfMet)]
class trgObjects_pfHt:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_pfHt_pt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_pfHt(tree, i) for i in range(tree.ntrgObjects_pfHt)]
class dRaddJetsdR08:
    def __init__(self, tree, n):
        self.dRaddJetsdR08 = tree.dRaddJetsdR08[n];
        pass
    @staticmethod
    def make_array(tree):
        return [dRaddJetsdR08(tree, i) for i in range(tree.ndRaddJetsdR08)]
class GenBQuarkFromH:
    def __init__(self, tree, n):
        self.pdgId = tree.GenBQuarkFromH_pdgId[n];
        self.pt = tree.GenBQuarkFromH_pt[n];
        self.eta = tree.GenBQuarkFromH_eta[n];
        self.phi = tree.GenBQuarkFromH_phi[n];
        self.mass = tree.GenBQuarkFromH_mass[n];
        self.charge = tree.GenBQuarkFromH_charge[n];
        self.status = tree.GenBQuarkFromH_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenBQuarkFromH(tree, i) for i in range(tree.nGenBQuarkFromH)]
class trgObjects_hltDoubleJet65:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltDoubleJet65(tree, i) for i in range(tree.ntrgObjects_hltDoubleJet65)]
class FatjetCA15trimmed:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15trimmed_pt[n];
        self.eta = tree.FatjetCA15trimmed_eta[n];
        self.phi = tree.FatjetCA15trimmed_phi[n];
        self.mass = tree.FatjetCA15trimmed_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15trimmed(tree, i) for i in range(tree.nFatjetCA15trimmed)]
class GenHiggsSisters:
    def __init__(self, tree, n):
        self.pdgId = tree.GenHiggsSisters_pdgId[n];
        self.pt = tree.GenHiggsSisters_pt[n];
        self.eta = tree.GenHiggsSisters_eta[n];
        self.phi = tree.GenHiggsSisters_phi[n];
        self.mass = tree.GenHiggsSisters_mass[n];
        self.charge = tree.GenHiggsSisters_charge[n];
        self.status = tree.GenHiggsSisters_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenHiggsSisters(tree, i) for i in range(tree.nGenHiggsSisters)]
class trgObjects_hltBTagCaloCSVp026DoubleWithMatching:
    def __init__(self, tree, n):
        self.pt = tree.trgObjects_hltBTagCaloCSVp026DoubleWithMatching_pt[n];
        self.eta = tree.trgObjects_hltBTagCaloCSVp026DoubleWithMatching_eta[n];
        self.phi = tree.trgObjects_hltBTagCaloCSVp026DoubleWithMatching_phi[n];
        self.mass = tree.trgObjects_hltBTagCaloCSVp026DoubleWithMatching_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagCaloCSVp026DoubleWithMatching(tree, i) for i in range(tree.ntrgObjects_hltBTagCaloCSVp026DoubleWithMatching)]
class aLeptons:
    def __init__(self, tree, n):
        self.charge = tree.aLeptons_charge[n];
        self.tightId = tree.aLeptons_tightId[n];
        self.eleCutIdCSA14_25ns_v1 = tree.aLeptons_eleCutIdCSA14_25ns_v1[n];
        self.eleCutIdCSA14_50ns_v1 = tree.aLeptons_eleCutIdCSA14_50ns_v1[n];
        self.eleCutIdSpring15_25ns_v1 = tree.aLeptons_eleCutIdSpring15_25ns_v1[n];
        self.dxy = tree.aLeptons_dxy[n];
        self.dz = tree.aLeptons_dz[n];
        self.edxy = tree.aLeptons_edxy[n];
        self.edz = tree.aLeptons_edz[n];
        self.ip3d = tree.aLeptons_ip3d[n];
        self.sip3d = tree.aLeptons_sip3d[n];
        self.convVeto = tree.aLeptons_convVeto[n];
        self.lostHits = tree.aLeptons_lostHits[n];
        self.relIso03 = tree.aLeptons_relIso03[n];
        self.relIso04 = tree.aLeptons_relIso04[n];
        self.miniRelIso = tree.aLeptons_miniRelIso[n];
        self.relIsoAn04 = tree.aLeptons_relIsoAn04[n];
        self.tightCharge = tree.aLeptons_tightCharge[n];
        self.mcMatchId = tree.aLeptons_mcMatchId[n];
        self.mcMatchAny = tree.aLeptons_mcMatchAny[n];
        self.mcMatchTau = tree.aLeptons_mcMatchTau[n];
        self.mcPt = tree.aLeptons_mcPt[n];
        self.mediumMuonId = tree.aLeptons_mediumMuonId[n];
        self.pdgId = tree.aLeptons_pdgId[n];
        self.pt = tree.aLeptons_pt[n];
        self.eta = tree.aLeptons_eta[n];
        self.phi = tree.aLeptons_phi[n];
        self.mass = tree.aLeptons_mass[n];
        self.looseIdSusy = tree.aLeptons_looseIdSusy[n];
        self.looseIdPOG = tree.aLeptons_looseIdPOG[n];
        self.chargedHadRelIso03 = tree.aLeptons_chargedHadRelIso03[n];
        self.chargedHadRelIso04 = tree.aLeptons_chargedHadRelIso04[n];
        self.eleSieie = tree.aLeptons_eleSieie[n];
        self.eleDEta = tree.aLeptons_eleDEta[n];
        self.eleDPhi = tree.aLeptons_eleDPhi[n];
        self.eleHoE = tree.aLeptons_eleHoE[n];
        self.eleMissingHits = tree.aLeptons_eleMissingHits[n];
        self.eleChi2 = tree.aLeptons_eleChi2[n];
        self.convVetoFull = tree.aLeptons_convVetoFull[n];
        self.eleMVArawSpring15Trig = tree.aLeptons_eleMVArawSpring15Trig[n];
        self.eleMVAIdSpring15Trig = tree.aLeptons_eleMVAIdSpring15Trig[n];
        self.eleMVArawSpring15NonTrig = tree.aLeptons_eleMVArawSpring15NonTrig[n];
        self.eleMVAIdSpring15NonTrig = tree.aLeptons_eleMVAIdSpring15NonTrig[n];
        self.nStations = tree.aLeptons_nStations[n];
        self.trkKink = tree.aLeptons_trkKink[n];
        self.segmentCompatibility = tree.aLeptons_segmentCompatibility[n];
        self.caloCompatibility = tree.aLeptons_caloCompatibility[n];
        self.globalTrackChi2 = tree.aLeptons_globalTrackChi2[n];
        self.nChamberHits = tree.aLeptons_nChamberHits[n];
        self.isPFMuon = tree.aLeptons_isPFMuon[n];
        self.isGlobalMuon = tree.aLeptons_isGlobalMuon[n];
        self.isTrackerMuon = tree.aLeptons_isTrackerMuon[n];
        self.pixelHits = tree.aLeptons_pixelHits[n];
        self.trackerLayers = tree.aLeptons_trackerLayers[n];
        self.pixelLayers = tree.aLeptons_pixelLayers[n];
        self.mvaTTH = tree.aLeptons_mvaTTH[n];
        self.jetOverlapIdx = tree.aLeptons_jetOverlapIdx[n];
        self.jetPtRatio = tree.aLeptons_jetPtRatio[n];
        self.jetBTagCSV = tree.aLeptons_jetBTagCSV[n];
        self.jetDR = tree.aLeptons_jetDR[n];
        self.mvaTTHjetPtRatio = tree.aLeptons_mvaTTHjetPtRatio[n];
        self.mvaTTHjetBTagCSV = tree.aLeptons_mvaTTHjetBTagCSV[n];
        self.mvaTTHjetDR = tree.aLeptons_mvaTTHjetDR[n];
        self.pfRelIso03 = tree.aLeptons_pfRelIso03[n];
        self.pfRelIso04 = tree.aLeptons_pfRelIso04[n];
        self.etaSc = tree.aLeptons_etaSc[n];
        self.eleExpMissingInnerHits = tree.aLeptons_eleExpMissingInnerHits[n];
        self.eleooEmooP = tree.aLeptons_eleooEmooP[n];
        self.dr03TkSumPt = tree.aLeptons_dr03TkSumPt[n];
        self.eleEcalClusterIso = tree.aLeptons_eleEcalClusterIso[n];
        self.eleHcalClusterIso = tree.aLeptons_eleHcalClusterIso[n];
        self.miniIsoCharged = tree.aLeptons_miniIsoCharged[n];
        self.miniIsoNeutral = tree.aLeptons_miniIsoNeutral[n];
        self.mvaTTHjetPtRel = tree.aLeptons_mvaTTHjetPtRel[n];
        self.mvaTTHjetNDauChargedMVASel = tree.aLeptons_mvaTTHjetNDauChargedMVASel[n];
        self.uncalibratedPt = tree.aLeptons_uncalibratedPt[n];
        self.SF_IsoLoose = tree.aLeptons_SF_IsoLoose[n];
        self.SFerr_IsoLoose = tree.aLeptons_SFerr_IsoLoose[n];
        self.SF_IsoTight = tree.aLeptons_SF_IsoTight[n];
        self.SFerr_IsoTight = tree.aLeptons_SFerr_IsoTight[n];
        self.SF_IdCutLoose = tree.aLeptons_SF_IdCutLoose[n];
        self.SFerr_IdCutLoose = tree.aLeptons_SFerr_IdCutLoose[n];
        self.SF_IdCutTight = tree.aLeptons_SF_IdCutTight[n];
        self.SFerr_IdCutTight = tree.aLeptons_SFerr_IdCutTight[n];
        self.SF_IdMVALoose = tree.aLeptons_SF_IdMVALoose[n];
        self.SFerr_IdMVALoose = tree.aLeptons_SFerr_IdMVALoose[n];
        self.SF_IdMVATight = tree.aLeptons_SF_IdMVATight[n];
        self.SFerr_IdMVATight = tree.aLeptons_SFerr_IdMVATight[n];
        self.SF_HLT_RunD4p3 = tree.aLeptons_SF_HLT_RunD4p3[n];
        self.SFerr_HLT_RunD4p3 = tree.aLeptons_SFerr_HLT_RunD4p3[n];
        self.SF_HLT_RunD4p2 = tree.aLeptons_SF_HLT_RunD4p2[n];
        self.SFerr_HLT_RunD4p2 = tree.aLeptons_SFerr_HLT_RunD4p2[n];
        self.SF_HLT_RunC = tree.aLeptons_SF_HLT_RunC[n];
        self.SFerr_HLT_RunC = tree.aLeptons_SFerr_HLT_RunC[n];
        self.Eff_HLT_RunD4p3 = tree.aLeptons_Eff_HLT_RunD4p3[n];
        self.Efferr_HLT_RunD4p3 = tree.aLeptons_Efferr_HLT_RunD4p3[n];
        self.Eff_HLT_RunD4p2 = tree.aLeptons_Eff_HLT_RunD4p2[n];
        self.Efferr_HLT_RunD4p2 = tree.aLeptons_Efferr_HLT_RunD4p2[n];
        self.Eff_HLT_RunC = tree.aLeptons_Eff_HLT_RunC[n];
        self.Efferr_HLT_RunC = tree.aLeptons_Efferr_HLT_RunC[n];
        pass
    @staticmethod
    def make_array(tree):
        return [aLeptons(tree, i) for i in range(tree.naLeptons)]
class trgObjects_hltPFQuadJetLooseID15:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFQuadJetLooseID15(tree, i) for i in range(tree.ntrgObjects_hltPFQuadJetLooseID15)]
class trgObjects_hltQuadPFCentralJetLooseID45:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltQuadPFCentralJetLooseID45(tree, i) for i in range(tree.ntrgObjects_hltQuadPFCentralJetLooseID45)]
class trgObjects_hltBTagCaloCSVp067Single:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagCaloCSVp067Single(tree, i) for i in range(tree.ntrgObjects_hltBTagCaloCSVp067Single)]
class trgObjects_hltVBFPFJetCSVSortedMqq200Detaqq1p2:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltVBFPFJetCSVSortedMqq200Detaqq1p2(tree, i) for i in range(tree.ntrgObjects_hltVBFPFJetCSVSortedMqq200Detaqq1p2)]
class hjidxaddJetsdR08:
    def __init__(self, tree, n):
        self.hjidxaddJetsdR08 = tree.hjidxaddJetsdR08[n];
        pass
    @staticmethod
    def make_array(tree):
        return [hjidxaddJetsdR08(tree, i) for i in range(tree.nhjidxaddJetsdR08)]
class trgObjects_hltMHTNoPU90:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltMHTNoPU90(tree, i) for i in range(tree.ntrgObjects_hltMHTNoPU90)]
class FatjetAK08ungroomed:
    def __init__(self, tree, n):
        self.pt = tree.FatjetAK08ungroomed_pt[n];
        self.eta = tree.FatjetAK08ungroomed_eta[n];
        self.phi = tree.FatjetAK08ungroomed_phi[n];
        self.mass = tree.FatjetAK08ungroomed_mass[n];
        self.tau1 = tree.FatjetAK08ungroomed_tau1[n];
        self.tau2 = tree.FatjetAK08ungroomed_tau2[n];
        self.tau3 = tree.FatjetAK08ungroomed_tau3[n];
        self.msoftdrop = tree.FatjetAK08ungroomed_msoftdrop[n];
        self.mpruned = tree.FatjetAK08ungroomed_mpruned[n];
        self.mprunedcorr = tree.FatjetAK08ungroomed_mprunedcorr[n];
        self.JEC_L2L3 = tree.FatjetAK08ungroomed_JEC_L2L3[n];
        self.JEC_L1L2L3 = tree.FatjetAK08ungroomed_JEC_L1L2L3[n];
        self.bbtag = tree.FatjetAK08ungroomed_bbtag[n];
        self.id_Tight = tree.FatjetAK08ungroomed_id_Tight[n];
        self.numberOfDaughters = tree.FatjetAK08ungroomed_numberOfDaughters[n];
        self.neutralEmEnergyFraction = tree.FatjetAK08ungroomed_neutralEmEnergyFraction[n];
        self.neutralHadronEnergyFraction = tree.FatjetAK08ungroomed_neutralHadronEnergyFraction[n];
        self.muonEnergyFraction = tree.FatjetAK08ungroomed_muonEnergyFraction[n];
        self.chargedEmEnergyFraction = tree.FatjetAK08ungroomed_chargedEmEnergyFraction[n];
        self.chargedHadronEnergyFraction = tree.FatjetAK08ungroomed_chargedHadronEnergyFraction[n];
        self.chargedMultiplicity = tree.FatjetAK08ungroomed_chargedMultiplicity[n];
        self.Flavour = tree.FatjetAK08ungroomed_Flavour[n];
        self.BhadronFlavour = tree.FatjetAK08ungroomed_BhadronFlavour[n];
        self.ChadronFlavour = tree.FatjetAK08ungroomed_ChadronFlavour[n];
        self.GenPt = tree.FatjetAK08ungroomed_GenPt[n];
        self.PFLepton_ptrel = tree.FatjetAK08ungroomed_PFLepton_ptrel[n];
        self.z_ratio = tree.FatjetAK08ungroomed_z_ratio[n];
        self.PFLepton_IP2D = tree.FatjetAK08ungroomed_PFLepton_IP2D[n];
        self.nSL = tree.FatjetAK08ungroomed_nSL[n];
        self.tau1_trackEtaRel_0 = tree.FatjetAK08ungroomed_tau1_trackEtaRel_0[n];
        self.tau1_trackEtaRel_1 = tree.FatjetAK08ungroomed_tau1_trackEtaRel_1[n];
        self.tau1_trackEtaRel_2 = tree.FatjetAK08ungroomed_tau1_trackEtaRel_2[n];
        self.tau0_trackEtaRel_0 = tree.FatjetAK08ungroomed_tau0_trackEtaRel_0[n];
        self.tau0_trackEtaRel_1 = tree.FatjetAK08ungroomed_tau0_trackEtaRel_1[n];
        self.tau0_trackEtaRel_2 = tree.FatjetAK08ungroomed_tau0_trackEtaRel_2[n];
        self.tau_vertexMass_0 = tree.FatjetAK08ungroomed_tau_vertexMass_0[n];
        self.tau_vertexEnergyRatio_0 = tree.FatjetAK08ungroomed_tau_vertexEnergyRatio_0[n];
        self.tau_vertexDeltaR_0 = tree.FatjetAK08ungroomed_tau_vertexDeltaR_0[n];
        self.tau_flightDistance2dSig_0 = tree.FatjetAK08ungroomed_tau_flightDistance2dSig_0[n];
        self.tau_vertexMass_1 = tree.FatjetAK08ungroomed_tau_vertexMass_1[n];
        self.tau_vertexEnergyRatio_1 = tree.FatjetAK08ungroomed_tau_vertexEnergyRatio_1[n];
        self.tau_flightDistance2dSig_1 = tree.FatjetAK08ungroomed_tau_flightDistance2dSig_1[n];
        self.nSV = tree.FatjetAK08ungroomed_nSV[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetAK08ungroomed(tree, i) for i in range(tree.nFatjetAK08ungroomed)]
class trgObjects_hltPFMHTTightID90:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFMHTTightID90(tree, i) for i in range(tree.ntrgObjects_hltPFMHTTightID90)]
class trgObjects_hltQuadCentralJet45:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltQuadCentralJet45(tree, i) for i in range(tree.ntrgObjects_hltQuadCentralJet45)]
class trgObjects_hltBTagCaloCSVp022Single:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagCaloCSVp022Single(tree, i) for i in range(tree.ntrgObjects_hltBTagCaloCSVp022Single)]
class aJCidx:
    def __init__(self, tree, n):
        self.aJCidx = tree.aJCidx[n];
        pass
    @staticmethod
    def make_array(tree):
        return [aJCidx(tree, i) for i in range(tree.naJCidx)]
class selLeptons:
    def __init__(self, tree, n):
        self.charge = tree.selLeptons_charge[n];
        self.tightId = tree.selLeptons_tightId[n];
        self.eleCutIdCSA14_25ns_v1 = tree.selLeptons_eleCutIdCSA14_25ns_v1[n];
        self.eleCutIdCSA14_50ns_v1 = tree.selLeptons_eleCutIdCSA14_50ns_v1[n];
        self.eleCutIdSpring15_25ns_v1 = tree.selLeptons_eleCutIdSpring15_25ns_v1[n];
        self.dxy = tree.selLeptons_dxy[n];
        self.dz = tree.selLeptons_dz[n];
        self.edxy = tree.selLeptons_edxy[n];
        self.edz = tree.selLeptons_edz[n];
        self.ip3d = tree.selLeptons_ip3d[n];
        self.sip3d = tree.selLeptons_sip3d[n];
        self.convVeto = tree.selLeptons_convVeto[n];
        self.lostHits = tree.selLeptons_lostHits[n];
        self.relIso03 = tree.selLeptons_relIso03[n];
        self.relIso04 = tree.selLeptons_relIso04[n];
        self.miniRelIso = tree.selLeptons_miniRelIso[n];
        self.relIsoAn04 = tree.selLeptons_relIsoAn04[n];
        self.tightCharge = tree.selLeptons_tightCharge[n];
        self.mcMatchId = tree.selLeptons_mcMatchId[n];
        self.mcMatchAny = tree.selLeptons_mcMatchAny[n];
        self.mcMatchTau = tree.selLeptons_mcMatchTau[n];
        self.mcPt = tree.selLeptons_mcPt[n];
        self.mediumMuonId = tree.selLeptons_mediumMuonId[n];
        self.pdgId = tree.selLeptons_pdgId[n];
        self.pt = tree.selLeptons_pt[n];
        self.eta = tree.selLeptons_eta[n];
        self.phi = tree.selLeptons_phi[n];
        self.mass = tree.selLeptons_mass[n];
        self.looseIdSusy = tree.selLeptons_looseIdSusy[n];
        self.looseIdPOG = tree.selLeptons_looseIdPOG[n];
        self.chargedHadRelIso03 = tree.selLeptons_chargedHadRelIso03[n];
        self.chargedHadRelIso04 = tree.selLeptons_chargedHadRelIso04[n];
        self.eleSieie = tree.selLeptons_eleSieie[n];
        self.eleDEta = tree.selLeptons_eleDEta[n];
        self.eleDPhi = tree.selLeptons_eleDPhi[n];
        self.eleHoE = tree.selLeptons_eleHoE[n];
        self.eleMissingHits = tree.selLeptons_eleMissingHits[n];
        self.eleChi2 = tree.selLeptons_eleChi2[n];
        self.convVetoFull = tree.selLeptons_convVetoFull[n];
        self.eleMVArawSpring15Trig = tree.selLeptons_eleMVArawSpring15Trig[n];
        self.eleMVAIdSpring15Trig = tree.selLeptons_eleMVAIdSpring15Trig[n];
        self.eleMVArawSpring15NonTrig = tree.selLeptons_eleMVArawSpring15NonTrig[n];
        self.eleMVAIdSpring15NonTrig = tree.selLeptons_eleMVAIdSpring15NonTrig[n];
        self.nStations = tree.selLeptons_nStations[n];
        self.trkKink = tree.selLeptons_trkKink[n];
        self.segmentCompatibility = tree.selLeptons_segmentCompatibility[n];
        self.caloCompatibility = tree.selLeptons_caloCompatibility[n];
        self.globalTrackChi2 = tree.selLeptons_globalTrackChi2[n];
        self.nChamberHits = tree.selLeptons_nChamberHits[n];
        self.isPFMuon = tree.selLeptons_isPFMuon[n];
        self.isGlobalMuon = tree.selLeptons_isGlobalMuon[n];
        self.isTrackerMuon = tree.selLeptons_isTrackerMuon[n];
        self.pixelHits = tree.selLeptons_pixelHits[n];
        self.trackerLayers = tree.selLeptons_trackerLayers[n];
        self.pixelLayers = tree.selLeptons_pixelLayers[n];
        self.mvaTTH = tree.selLeptons_mvaTTH[n];
        self.jetOverlapIdx = tree.selLeptons_jetOverlapIdx[n];
        self.jetPtRatio = tree.selLeptons_jetPtRatio[n];
        self.jetBTagCSV = tree.selLeptons_jetBTagCSV[n];
        self.jetDR = tree.selLeptons_jetDR[n];
        self.mvaTTHjetPtRatio = tree.selLeptons_mvaTTHjetPtRatio[n];
        self.mvaTTHjetBTagCSV = tree.selLeptons_mvaTTHjetBTagCSV[n];
        self.mvaTTHjetDR = tree.selLeptons_mvaTTHjetDR[n];
        self.pfRelIso03 = tree.selLeptons_pfRelIso03[n];
        self.pfRelIso04 = tree.selLeptons_pfRelIso04[n];
        self.etaSc = tree.selLeptons_etaSc[n];
        self.eleExpMissingInnerHits = tree.selLeptons_eleExpMissingInnerHits[n];
        self.eleooEmooP = tree.selLeptons_eleooEmooP[n];
        self.dr03TkSumPt = tree.selLeptons_dr03TkSumPt[n];
        self.eleEcalClusterIso = tree.selLeptons_eleEcalClusterIso[n];
        self.eleHcalClusterIso = tree.selLeptons_eleHcalClusterIso[n];
        self.miniIsoCharged = tree.selLeptons_miniIsoCharged[n];
        self.miniIsoNeutral = tree.selLeptons_miniIsoNeutral[n];
        self.mvaTTHjetPtRel = tree.selLeptons_mvaTTHjetPtRel[n];
        self.mvaTTHjetNDauChargedMVASel = tree.selLeptons_mvaTTHjetNDauChargedMVASel[n];
        self.uncalibratedPt = tree.selLeptons_uncalibratedPt[n];
        self.SF_IsoLoose = tree.selLeptons_SF_IsoLoose[n];
        self.SFerr_IsoLoose = tree.selLeptons_SFerr_IsoLoose[n];
        self.SF_IsoTight = tree.selLeptons_SF_IsoTight[n];
        self.SFerr_IsoTight = tree.selLeptons_SFerr_IsoTight[n];
        self.SF_IdCutLoose = tree.selLeptons_SF_IdCutLoose[n];
        self.SFerr_IdCutLoose = tree.selLeptons_SFerr_IdCutLoose[n];
        self.SF_IdCutTight = tree.selLeptons_SF_IdCutTight[n];
        self.SFerr_IdCutTight = tree.selLeptons_SFerr_IdCutTight[n];
        self.SF_IdMVALoose = tree.selLeptons_SF_IdMVALoose[n];
        self.SFerr_IdMVALoose = tree.selLeptons_SFerr_IdMVALoose[n];
        self.SF_IdMVATight = tree.selLeptons_SF_IdMVATight[n];
        self.SFerr_IdMVATight = tree.selLeptons_SFerr_IdMVATight[n];
        self.SF_HLT_RunD4p3 = tree.selLeptons_SF_HLT_RunD4p3[n];
        self.SFerr_HLT_RunD4p3 = tree.selLeptons_SFerr_HLT_RunD4p3[n];
        self.SF_HLT_RunD4p2 = tree.selLeptons_SF_HLT_RunD4p2[n];
        self.SFerr_HLT_RunD4p2 = tree.selLeptons_SFerr_HLT_RunD4p2[n];
        self.SF_HLT_RunC = tree.selLeptons_SF_HLT_RunC[n];
        self.SFerr_HLT_RunC = tree.selLeptons_SFerr_HLT_RunC[n];
        self.Eff_HLT_RunD4p3 = tree.selLeptons_Eff_HLT_RunD4p3[n];
        self.Efferr_HLT_RunD4p3 = tree.selLeptons_Efferr_HLT_RunD4p3[n];
        self.Eff_HLT_RunD4p2 = tree.selLeptons_Eff_HLT_RunD4p2[n];
        self.Efferr_HLT_RunD4p2 = tree.selLeptons_Efferr_HLT_RunD4p2[n];
        self.Eff_HLT_RunC = tree.selLeptons_Eff_HLT_RunC[n];
        self.Efferr_HLT_RunC = tree.selLeptons_Efferr_HLT_RunC[n];
        pass
    @staticmethod
    def make_array(tree):
        return [selLeptons(tree, i) for i in range(tree.nselLeptons)]
class trgObjects_hltPFMET90:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFMET90(tree, i) for i in range(tree.ntrgObjects_hltPFMET90)]
class trgObjects_hltQuadJet15:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltQuadJet15(tree, i) for i in range(tree.ntrgObjects_hltQuadJet15)]
class TauGood:
    def __init__(self, tree, n):
        self.charge = tree.TauGood_charge[n];
        self.decayMode = tree.TauGood_decayMode[n];
        self.idDecayMode = tree.TauGood_idDecayMode[n];
        self.idDecayModeNewDMs = tree.TauGood_idDecayModeNewDMs[n];
        self.dxy = tree.TauGood_dxy[n];
        self.dz = tree.TauGood_dz[n];
        self.idMVArun2 = tree.TauGood_idMVArun2[n];
        self.rawMVArun2 = tree.TauGood_rawMVArun2[n];
        self.idMVArun2dR03 = tree.TauGood_idMVArun2dR03[n];
        self.rawMVArun2dR03 = tree.TauGood_rawMVArun2dR03[n];
        self.idMVArun2NewDM = tree.TauGood_idMVArun2NewDM[n];
        self.rawMVArun2NewDM = tree.TauGood_rawMVArun2NewDM[n];
        self.idCI3hit = tree.TauGood_idCI3hit[n];
        self.idAntiMu = tree.TauGood_idAntiMu[n];
        self.idAntiErun2 = tree.TauGood_idAntiErun2[n];
        self.isoCI3hit = tree.TauGood_isoCI3hit[n];
        self.photonOutsideSigCone = tree.TauGood_photonOutsideSigCone[n];
        self.mcMatchId = tree.TauGood_mcMatchId[n];
        self.pdgId = tree.TauGood_pdgId[n];
        self.pt = tree.TauGood_pt[n];
        self.eta = tree.TauGood_eta[n];
        self.phi = tree.TauGood_phi[n];
        self.mass = tree.TauGood_mass[n];
        self.idxJetMatch = tree.TauGood_idxJetMatch[n];
        self.genMatchType = tree.TauGood_genMatchType[n];
        pass
    @staticmethod
    def make_array(tree):
        return [TauGood(tree, i) for i in range(tree.nTauGood)]
class hJidx:
    def __init__(self, tree, n):
        self.hJidx = tree.hJidx[n];
        pass
    @staticmethod
    def make_array(tree):
        return [hJidx(tree, i) for i in range(tree.nhJidx)]
class GenLepRecovered:
    def __init__(self, tree, n):
        self.pdgId = tree.GenLepRecovered_pdgId[n];
        self.pt = tree.GenLepRecovered_pt[n];
        self.eta = tree.GenLepRecovered_eta[n];
        self.phi = tree.GenLepRecovered_phi[n];
        self.mass = tree.GenLepRecovered_mass[n];
        self.charge = tree.GenLepRecovered_charge[n];
        self.status = tree.GenLepRecovered_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenLepRecovered(tree, i) for i in range(tree.nGenLepRecovered)]
class FatjetCA15softdropz2b1:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15softdropz2b1_pt[n];
        self.eta = tree.FatjetCA15softdropz2b1_eta[n];
        self.phi = tree.FatjetCA15softdropz2b1_phi[n];
        self.mass = tree.FatjetCA15softdropz2b1_mass[n];
        self.tau1 = tree.FatjetCA15softdropz2b1_tau1[n];
        self.tau2 = tree.FatjetCA15softdropz2b1_tau2[n];
        self.tau3 = tree.FatjetCA15softdropz2b1_tau3[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15softdropz2b1(tree, i) for i in range(tree.nFatjetCA15softdropz2b1)]
class GenStatus2bHad:
    def __init__(self, tree, n):
        self.pdgId = tree.GenStatus2bHad_pdgId[n];
        self.pt = tree.GenStatus2bHad_pt[n];
        self.eta = tree.GenStatus2bHad_eta[n];
        self.phi = tree.GenStatus2bHad_phi[n];
        self.mass = tree.GenStatus2bHad_mass[n];
        self.charge = tree.GenStatus2bHad_charge[n];
        self.status = tree.GenStatus2bHad_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenStatus2bHad(tree, i) for i in range(tree.nGenStatus2bHad)]
class trgObjects_hltTripleJet50:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltTripleJet50(tree, i) for i in range(tree.ntrgObjects_hltTripleJet50)]
class trgObjects_hltVBFPFJetCSVSortedMqq460Detaqq4p1:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltVBFPFJetCSVSortedMqq460Detaqq4p1(tree, i) for i in range(tree.ntrgObjects_hltVBFPFJetCSVSortedMqq460Detaqq4p1)]
class httCandidates:
    def __init__(self, tree, n):
        self.pt = tree.httCandidates_pt[n];
        self.eta = tree.httCandidates_eta[n];
        self.phi = tree.httCandidates_phi[n];
        self.mass = tree.httCandidates_mass[n];
        self.ptcal = tree.httCandidates_ptcal[n];
        self.etacal = tree.httCandidates_etacal[n];
        self.phical = tree.httCandidates_phical[n];
        self.masscal = tree.httCandidates_masscal[n];
        self.fRec = tree.httCandidates_fRec[n];
        self.Ropt = tree.httCandidates_Ropt[n];
        self.RoptCalc = tree.httCandidates_RoptCalc[n];
        self.ptForRoptCalc = tree.httCandidates_ptForRoptCalc[n];
        self.sjW1ptcal = tree.httCandidates_sjW1ptcal[n];
        self.sjW1pt = tree.httCandidates_sjW1pt[n];
        self.sjW1eta = tree.httCandidates_sjW1eta[n];
        self.sjW1phi = tree.httCandidates_sjW1phi[n];
        self.sjW1masscal = tree.httCandidates_sjW1masscal[n];
        self.sjW1mass = tree.httCandidates_sjW1mass[n];
        self.sjW1btag = tree.httCandidates_sjW1btag[n];
        self.sjW2ptcal = tree.httCandidates_sjW2ptcal[n];
        self.sjW2pt = tree.httCandidates_sjW2pt[n];
        self.sjW2eta = tree.httCandidates_sjW2eta[n];
        self.sjW2phi = tree.httCandidates_sjW2phi[n];
        self.sjW2masscal = tree.httCandidates_sjW2masscal[n];
        self.sjW2mass = tree.httCandidates_sjW2mass[n];
        self.sjW2btag = tree.httCandidates_sjW2btag[n];
        self.sjNonWptcal = tree.httCandidates_sjNonWptcal[n];
        self.sjNonWpt = tree.httCandidates_sjNonWpt[n];
        self.sjNonWeta = tree.httCandidates_sjNonWeta[n];
        self.sjNonWphi = tree.httCandidates_sjNonWphi[n];
        self.sjNonWmasscal = tree.httCandidates_sjNonWmasscal[n];
        self.sjNonWmass = tree.httCandidates_sjNonWmass[n];
        self.sjNonWbtag = tree.httCandidates_sjNonWbtag[n];
        pass
    @staticmethod
    def make_array(tree):
        return [httCandidates(tree, i) for i in range(tree.nhttCandidates)]
class trgObjects_hltBTagCaloCSVp087Triple:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltBTagCaloCSVp087Triple(tree, i) for i in range(tree.ntrgObjects_hltBTagCaloCSVp087Triple)]
class GenTaus:
    def __init__(self, tree, n):
        self.pdgId = tree.GenTaus_pdgId[n];
        self.pt = tree.GenTaus_pt[n];
        self.eta = tree.GenTaus_eta[n];
        self.phi = tree.GenTaus_phi[n];
        self.mass = tree.GenTaus_mass[n];
        self.charge = tree.GenTaus_charge[n];
        self.status = tree.GenTaus_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenTaus(tree, i) for i in range(tree.nGenTaus)]
class trgObjects_hltMHT70:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltMHT70(tree, i) for i in range(tree.ntrgObjects_hltMHT70)]
class Jet:
    def __init__(self, tree, n):
        self.id = tree.Jet_id[n];
        self.puId = tree.Jet_puId[n];
        self.btagCSV = tree.Jet_btagCSV[n];
        self.btagCMVA = tree.Jet_btagCMVA[n];
        self.rawPt = tree.Jet_rawPt[n];
        self.mcPt = tree.Jet_mcPt[n];
        self.mcFlavour = tree.Jet_mcFlavour[n];
        self.partonFlavour = tree.Jet_partonFlavour[n];
        self.hadronFlavour = tree.Jet_hadronFlavour[n];
        self.mcMatchId = tree.Jet_mcMatchId[n];
        self.corr_JECUp = tree.Jet_corr_JECUp[n];
        self.corr_JECDown = tree.Jet_corr_JECDown[n];
        self.corr = tree.Jet_corr[n];
        self.corr_JERUp = tree.Jet_corr_JERUp[n];
        self.corr_JERDown = tree.Jet_corr_JERDown[n];
        self.corr_JER = tree.Jet_corr_JER[n];
        self.pt = tree.Jet_pt[n];
        self.eta = tree.Jet_eta[n];
        self.phi = tree.Jet_phi[n];
        self.mass = tree.Jet_mass[n];
        self.rawPtAfterSmearing = tree.Jet_rawPtAfterSmearing[n];
        self.idxFirstTauMatch = tree.Jet_idxFirstTauMatch[n];
        self.heppyFlavour = tree.Jet_heppyFlavour[n];
        self.ctagVsL = tree.Jet_ctagVsL[n];
        self.ctagVsB = tree.Jet_ctagVsB[n];
        self.btagBDT = tree.Jet_btagBDT[n];
        self.btagProb = tree.Jet_btagProb[n];
        self.btagBProb = tree.Jet_btagBProb[n];
        self.btagSoftEl = tree.Jet_btagSoftEl[n];
        self.btagSoftMu = tree.Jet_btagSoftMu[n];
        self.btagnew = tree.Jet_btagnew[n];
        self.btagCSVV0 = tree.Jet_btagCSVV0[n];
        self.btagCMVAV2 = tree.Jet_btagCMVAV2[n];
        self.chHEF = tree.Jet_chHEF[n];
        self.neHEF = tree.Jet_neHEF[n];
        self.chEmEF = tree.Jet_chEmEF[n];
        self.neEmEF = tree.Jet_neEmEF[n];
        self.muEF = tree.Jet_muEF[n];
        self.chMult = tree.Jet_chMult[n];
        self.nhMult = tree.Jet_nhMult[n];
        self.leadTrackPt = tree.Jet_leadTrackPt[n];
        self.mcEta = tree.Jet_mcEta[n];
        self.mcPhi = tree.Jet_mcPhi[n];
        self.mcM = tree.Jet_mcM[n];
        self.leptonPdgId = tree.Jet_leptonPdgId[n];
        self.leptonPt = tree.Jet_leptonPt[n];
        self.leptonPtRel = tree.Jet_leptonPtRel[n];
        self.leptonPtRelInv = tree.Jet_leptonPtRelInv[n];
        self.leptonDeltaR = tree.Jet_leptonDeltaR[n];
        self.leptonDeltaPhi = tree.Jet_leptonDeltaPhi[n];
        self.leptonDeltaEta = tree.Jet_leptonDeltaEta[n];
        self.vtxMass = tree.Jet_vtxMass[n];
        self.vtxNtracks = tree.Jet_vtxNtracks[n];
        self.vtxPt = tree.Jet_vtxPt[n];
        self.vtx3DSig = tree.Jet_vtx3DSig[n];
        self.vtx3DVal = tree.Jet_vtx3DVal[n];
        self.vtxPosX = tree.Jet_vtxPosX[n];
        self.vtxPosY = tree.Jet_vtxPosY[n];
        self.vtxPosZ = tree.Jet_vtxPosZ[n];
        self.pullVectorPhi = tree.Jet_pullVectorPhi[n];
        self.pullVectorMag = tree.Jet_pullVectorMag[n];
        self.qgl = tree.Jet_qgl[n];
        self.ptd = tree.Jet_ptd[n];
        self.axis2 = tree.Jet_axis2[n];
        self.mult = tree.Jet_mult[n];
        self.numberOfDaughters = tree.Jet_numberOfDaughters[n];
        self.btagIdx = tree.Jet_btagIdx[n];
        self.mcIdx = tree.Jet_mcIdx[n];
        self.blike_VBF = tree.Jet_blike_VBF[n];
        self.pt_reg = tree.Jet_pt_reg[n];
        self.pt_regVBF = tree.Jet_pt_regVBF[n];
        self.pt_reg_corrJECUp = tree.Jet_pt_reg_corrJECUp[n];
        self.pt_regVBF_corrJECUp = tree.Jet_pt_regVBF_corrJECUp[n];
        self.pt_reg_corrJECDown = tree.Jet_pt_reg_corrJECDown[n];
        self.pt_regVBF_corrJECDown = tree.Jet_pt_regVBF_corrJECDown[n];
        self.pt_reg_corrJERUp = tree.Jet_pt_reg_corrJERUp[n];
        self.pt_regVBF_corrJERUp = tree.Jet_pt_regVBF_corrJERUp[n];
        self.pt_reg_corrJERDown = tree.Jet_pt_reg_corrJERDown[n];
        self.pt_regVBF_corrJERDown = tree.Jet_pt_regVBF_corrJERDown[n];
        self.bTagWeightJESUp = tree.Jet_bTagWeightJESUp[n];
        self.bTagWeightJESDown = tree.Jet_bTagWeightJESDown[n];
        self.bTagWeightLFUp = tree.Jet_bTagWeightLFUp[n];
        self.bTagWeightLFDown = tree.Jet_bTagWeightLFDown[n];
        self.bTagWeightHFUp = tree.Jet_bTagWeightHFUp[n];
        self.bTagWeightHFDown = tree.Jet_bTagWeightHFDown[n];
        self.bTagWeightHFStats1Up = tree.Jet_bTagWeightHFStats1Up[n];
        self.bTagWeightHFStats1Down = tree.Jet_bTagWeightHFStats1Down[n];
        self.bTagWeightHFStats2Up = tree.Jet_bTagWeightHFStats2Up[n];
        self.bTagWeightHFStats2Down = tree.Jet_bTagWeightHFStats2Down[n];
        self.bTagWeightLFStats1Up = tree.Jet_bTagWeightLFStats1Up[n];
        self.bTagWeightLFStats1Down = tree.Jet_bTagWeightLFStats1Down[n];
        self.bTagWeightLFStats2Up = tree.Jet_bTagWeightLFStats2Up[n];
        self.bTagWeightLFStats2Down = tree.Jet_bTagWeightLFStats2Down[n];
        self.bTagWeightcErr1Up = tree.Jet_bTagWeightcErr1Up[n];
        self.bTagWeightcErr1Down = tree.Jet_bTagWeightcErr1Down[n];
        self.bTagWeightcErr2Up = tree.Jet_bTagWeightcErr2Up[n];
        self.bTagWeightcErr2Down = tree.Jet_bTagWeightcErr2Down[n];
        self.bTagWeight = tree.Jet_bTagWeight[n];
        self.btagCSVLSF = tree.Jet_btagCSVLSF[n];
        self.btagCSVLSF_Up = tree.Jet_btagCSVLSF_Up[n];
        self.btagCSVLSF_Down = tree.Jet_btagCSVLSF_Down[n];
        self.btagCSVMSF = tree.Jet_btagCSVMSF[n];
        self.btagCSVMSF_Up = tree.Jet_btagCSVMSF_Up[n];
        self.btagCSVMSF_Down = tree.Jet_btagCSVMSF_Down[n];
        self.btagCSVTSF = tree.Jet_btagCSVTSF[n];
        self.btagCSVTSF_Up = tree.Jet_btagCSVTSF_Up[n];
        self.btagCSVTSF_Down = tree.Jet_btagCSVTSF_Down[n];
        self.btagCMVAV2LSF = tree.Jet_btagCMVAV2LSF[n];
        self.btagCMVAV2LSF_Up = tree.Jet_btagCMVAV2LSF_Up[n];
        self.btagCMVAV2LSF_Down = tree.Jet_btagCMVAV2LSF_Down[n];
        self.btagCMVAV2MSF = tree.Jet_btagCMVAV2MSF[n];
        self.btagCMVAV2MSF_Up = tree.Jet_btagCMVAV2MSF_Up[n];
        self.btagCMVAV2MSF_Down = tree.Jet_btagCMVAV2MSF_Down[n];
        self.btagCMVAV2TSF = tree.Jet_btagCMVAV2TSF[n];
        self.btagCMVAV2TSF_Up = tree.Jet_btagCMVAV2TSF_Up[n];
        self.btagCMVAV2TSF_Down = tree.Jet_btagCMVAV2TSF_Down[n];
        pass
    @staticmethod
    def make_array(tree):
        return [Jet(tree, i) for i in range(tree.nJet)]
class FatjetCA15softdrop:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15softdrop_pt[n];
        self.eta = tree.FatjetCA15softdrop_eta[n];
        self.phi = tree.FatjetCA15softdrop_phi[n];
        self.mass = tree.FatjetCA15softdrop_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15softdrop(tree, i) for i in range(tree.nFatjetCA15softdrop)]
class trgObjects_hltPFTripleJetLooseID64:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltPFTripleJetLooseID64(tree, i) for i in range(tree.ntrgObjects_hltPFTripleJetLooseID64)]
class LHE_weights_pdf:
    def __init__(self, tree, n):
        self.id = tree.LHE_weights_pdf_id[n];
        self.wgt = tree.LHE_weights_pdf_wgt[n];
        pass
    @staticmethod
    def make_array(tree):
        return [LHE_weights_pdf(tree, i) for i in range(tree.nLHE_weights_pdf)]
class primaryVertices:
    def __init__(self, tree, n):
        self.x = tree.primaryVertices_x[n];
        self.y = tree.primaryVertices_y[n];
        self.z = tree.primaryVertices_z[n];
        self.isFake = tree.primaryVertices_isFake[n];
        self.ndof = tree.primaryVertices_ndof[n];
        self.Rho = tree.primaryVertices_Rho[n];
        self.score = tree.primaryVertices_score[n];
        pass
    @staticmethod
    def make_array(tree):
        return [primaryVertices(tree, i) for i in range(tree.nprimaryVertices)]
class softActivityJets:
    def __init__(self, tree, n):
        self.pt = tree.softActivityJets_pt[n];
        self.eta = tree.softActivityJets_eta[n];
        self.phi = tree.softActivityJets_phi[n];
        self.mass = tree.softActivityJets_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [softActivityJets(tree, i) for i in range(tree.nsoftActivityJets)]
class FatjetCA15subjetfiltered:
    def __init__(self, tree, n):
        self.pt = tree.FatjetCA15subjetfiltered_pt[n];
        self.eta = tree.FatjetCA15subjetfiltered_eta[n];
        self.phi = tree.FatjetCA15subjetfiltered_phi[n];
        self.mass = tree.FatjetCA15subjetfiltered_mass[n];
        pass
    @staticmethod
    def make_array(tree):
        return [FatjetCA15subjetfiltered(tree, i) for i in range(tree.nFatjetCA15subjetfiltered)]
class GenWZQuark:
    def __init__(self, tree, n):
        self.pdgId = tree.GenWZQuark_pdgId[n];
        self.pt = tree.GenWZQuark_pt[n];
        self.eta = tree.GenWZQuark_eta[n];
        self.phi = tree.GenWZQuark_phi[n];
        self.mass = tree.GenWZQuark_mass[n];
        self.charge = tree.GenWZQuark_charge[n];
        self.status = tree.GenWZQuark_status[n];
        pass
    @staticmethod
    def make_array(tree):
        return [GenWZQuark(tree, i) for i in range(tree.nGenWZQuark)]
class trgObjects_hltSingleJet80:
    def __init__(self, tree, n):
        pass
    @staticmethod
    def make_array(tree):
        return [trgObjects_hltSingleJet80(tree, i) for i in range(tree.ntrgObjects_hltSingleJet80)]
class H_reg_corrJECUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_reg_corrJECUp_pt", None)
        _eta = getattr(tree, "H_reg_corrJECUp_eta", None)
        _phi = getattr(tree, "H_reg_corrJECUp_phi", None)
        _mass = getattr(tree, "H_reg_corrJECUp_mass", None)
        return H_reg_corrJECUp(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class HaddJetsdR08:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HaddJetsdR08_pt", None)
        _eta = getattr(tree, "HaddJetsdR08_eta", None)
        _phi = getattr(tree, "HaddJetsdR08_phi", None)
        _mass = getattr(tree, "HaddJetsdR08_mass", None)
        return HaddJetsdR08(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class H:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_pt", None)
        _eta = getattr(tree, "H_eta", None)
        _phi = getattr(tree, "H_phi", None)
        _mass = getattr(tree, "H_mass", None)
        return H(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class softActivityVH:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _njets2 = getattr(tree, "softActivityVH_njets2", None)
        _njets5 = getattr(tree, "softActivityVH_njets5", None)
        _njets10 = getattr(tree, "softActivityVH_njets10", None)
        _HT = getattr(tree, "softActivityVH_HT", None)
        return softActivityVH(_njets2, _njets5, _njets10, _HT)
    def __init__(self, njets2,njets5,njets10,HT):
        self.njets2 = njets2 #number of jets from soft activity with pt>2Gev
        self.njets5 = njets5 #number of jets from soft activity with pt>5Gev
        self.njets10 = njets10 #number of jets from soft activity with pt>10Gev
        self.HT = HT #sum pt of sa jets
        pass
class met_shifted_JetResUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_JetResUp_pt", None)
        _phi = getattr(tree, "met_shifted_JetResUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_JetResUp_sumEt", None)
        return met_shifted_JetResUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_pt", None)
        _eta = getattr(tree, "met_eta", None)
        _phi = getattr(tree, "met_phi", None)
        _mass = getattr(tree, "met_mass", None)
        _sumEt = getattr(tree, "met_sumEt", None)
        _rawPt = getattr(tree, "met_rawPt", None)
        _rawPhi = getattr(tree, "met_rawPhi", None)
        _rawSumEt = getattr(tree, "met_rawSumEt", None)
        _genPt = getattr(tree, "met_genPt", None)
        _genPhi = getattr(tree, "met_genPhi", None)
        _genEta = getattr(tree, "met_genEta", None)
        return met(_pt, _eta, _phi, _mass, _sumEt, _rawPt, _rawPhi, _rawSumEt, _genPt, _genPhi, _genEta)
    def __init__(self, pt,eta,phi,mass,sumEt,rawPt,rawPhi,rawSumEt,genPt,genPhi,genEta):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        self.sumEt = sumEt #
        self.rawPt = rawPt #
        self.rawPhi = rawPhi #
        self.rawSumEt = rawSumEt #
        self.genPt = genPt #
        self.genPhi = genPhi #
        self.genEta = genEta #
        pass
class H_reg:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_reg_pt", None)
        _eta = getattr(tree, "H_reg_eta", None)
        _phi = getattr(tree, "H_reg_phi", None)
        _mass = getattr(tree, "H_reg_mass", None)
        return H_reg(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class HCSV_reg_corrJERDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_reg_corrJERDown_pt", None)
        _eta = getattr(tree, "HCSV_reg_corrJERDown_eta", None)
        _phi = getattr(tree, "HCSV_reg_corrJERDown_phi", None)
        _mass = getattr(tree, "HCSV_reg_corrJERDown_mass", None)
        return HCSV_reg_corrJERDown(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class HCSV:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_pt", None)
        _eta = getattr(tree, "HCSV_eta", None)
        _phi = getattr(tree, "HCSV_phi", None)
        _mass = getattr(tree, "HCSV_mass", None)
        return HCSV(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class met_shifted_MuonEnDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_MuonEnDown_pt", None)
        _phi = getattr(tree, "met_shifted_MuonEnDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_MuonEnDown_sumEt", None)
        return met_shifted_MuonEnDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met_shifted_ElectronEnUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_ElectronEnUp_pt", None)
        _phi = getattr(tree, "met_shifted_ElectronEnUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_ElectronEnUp_sumEt", None)
        return met_shifted_ElectronEnUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met_shifted_ElectronEnDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_ElectronEnDown_pt", None)
        _phi = getattr(tree, "met_shifted_ElectronEnDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_ElectronEnDown_sumEt", None)
        return met_shifted_ElectronEnDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class fakeMET:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "fakeMET_pt", None)
        _eta = getattr(tree, "fakeMET_eta", None)
        _phi = getattr(tree, "fakeMET_phi", None)
        _mass = getattr(tree, "fakeMET_mass", None)
        return fakeMET(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class met_shifted_TauEnDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_TauEnDown_pt", None)
        _phi = getattr(tree, "met_shifted_TauEnDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_TauEnDown_sumEt", None)
        return met_shifted_TauEnDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class V:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "V_pt", None)
        _eta = getattr(tree, "V_eta", None)
        _phi = getattr(tree, "V_phi", None)
        _mass = getattr(tree, "V_mass", None)
        return V(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class HCSV_reg_corrJERUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_reg_corrJERUp_pt", None)
        _eta = getattr(tree, "HCSV_reg_corrJERUp_eta", None)
        _phi = getattr(tree, "HCSV_reg_corrJERUp_phi", None)
        _mass = getattr(tree, "HCSV_reg_corrJERUp_mass", None)
        return HCSV_reg_corrJERUp(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class met_shifted_TauEnUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_TauEnUp_pt", None)
        _phi = getattr(tree, "met_shifted_TauEnUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_TauEnUp_sumEt", None)
        return met_shifted_TauEnUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class HCSV_reg_corrJECUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_reg_corrJECUp_pt", None)
        _eta = getattr(tree, "HCSV_reg_corrJECUp_eta", None)
        _phi = getattr(tree, "HCSV_reg_corrJECUp_phi", None)
        _mass = getattr(tree, "HCSV_reg_corrJECUp_mass", None)
        return HCSV_reg_corrJECUp(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class met_shifted_UnclusteredEnUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_UnclusteredEnUp_pt", None)
        _phi = getattr(tree, "met_shifted_UnclusteredEnUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_UnclusteredEnUp_sumEt", None)
        return met_shifted_UnclusteredEnUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met_shifted_UnclusteredEnDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_UnclusteredEnDown_pt", None)
        _phi = getattr(tree, "met_shifted_UnclusteredEnDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_UnclusteredEnDown_sumEt", None)
        return met_shifted_UnclusteredEnDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met_shifted_JetEnUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_JetEnUp_pt", None)
        _phi = getattr(tree, "met_shifted_JetEnUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_JetEnUp_sumEt", None)
        return met_shifted_JetEnUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class H_reg_corrJERDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_reg_corrJERDown_pt", None)
        _eta = getattr(tree, "H_reg_corrJERDown_eta", None)
        _phi = getattr(tree, "H_reg_corrJERDown_phi", None)
        _mass = getattr(tree, "H_reg_corrJERDown_mass", None)
        return H_reg_corrJERDown(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class HCSV_reg:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_reg_pt", None)
        _eta = getattr(tree, "HCSV_reg_eta", None)
        _phi = getattr(tree, "HCSV_reg_phi", None)
        _mass = getattr(tree, "HCSV_reg_mass", None)
        return HCSV_reg(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class met_shifted_JetEnDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_JetEnDown_pt", None)
        _phi = getattr(tree, "met_shifted_JetEnDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_JetEnDown_sumEt", None)
        return met_shifted_JetEnDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class met_shifted_JetResDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_JetResDown_pt", None)
        _phi = getattr(tree, "met_shifted_JetResDown_phi", None)
        _sumEt = getattr(tree, "met_shifted_JetResDown_sumEt", None)
        return met_shifted_JetResDown(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class softActivity:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _njets2 = getattr(tree, "softActivity_njets2", None)
        _njets5 = getattr(tree, "softActivity_njets5", None)
        _njets10 = getattr(tree, "softActivity_njets10", None)
        _HT = getattr(tree, "softActivity_HT", None)
        return softActivity(_njets2, _njets5, _njets10, _HT)
    def __init__(self, njets2,njets5,njets10,HT):
        self.njets2 = njets2 #number of jets from soft activity with pt>2Gev
        self.njets5 = njets5 #number of jets from soft activity with pt>5Gev
        self.njets10 = njets10 #number of jets from soft activity with pt>10Gev
        self.HT = HT #sum pt of sa jets
        pass
class met_shifted_MuonEnUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "met_shifted_MuonEnUp_pt", None)
        _phi = getattr(tree, "met_shifted_MuonEnUp_phi", None)
        _sumEt = getattr(tree, "met_shifted_MuonEnUp_sumEt", None)
        return met_shifted_MuonEnUp(_pt, _phi, _sumEt)
    def __init__(self, pt,phi,sumEt):
        self.pt = pt #
        self.phi = phi #
        self.sumEt = sumEt #
        pass
class HCSV_reg_corrJECDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "HCSV_reg_corrJECDown_pt", None)
        _eta = getattr(tree, "HCSV_reg_corrJECDown_eta", None)
        _phi = getattr(tree, "HCSV_reg_corrJECDown_phi", None)
        _mass = getattr(tree, "HCSV_reg_corrJECDown_mass", None)
        return HCSV_reg_corrJECDown(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class H_reg_corrJERUp:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_reg_corrJERUp_pt", None)
        _eta = getattr(tree, "H_reg_corrJERUp_eta", None)
        _phi = getattr(tree, "H_reg_corrJERUp_phi", None)
        _mass = getattr(tree, "H_reg_corrJERUp_mass", None)
        return H_reg_corrJERUp(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass
class H_reg_corrJECDown:
    """
    
    """
    @staticmethod
    def make_obj(tree):
        _pt = getattr(tree, "H_reg_corrJECDown_pt", None)
        _eta = getattr(tree, "H_reg_corrJECDown_eta", None)
        _phi = getattr(tree, "H_reg_corrJECDown_phi", None)
        _mass = getattr(tree, "H_reg_corrJECDown_mass", None)
        return H_reg_corrJECDown(_pt, _eta, _phi, _mass)
    def __init__(self, pt,eta,phi,mass):
        self.pt = pt #
        self.eta = eta #
        self.phi = phi #
        self.mass = mass #
        pass

from PhysicsTools.HeppyCore.framework.analyzer import Analyzer
class EventAnalyzer(Analyzer):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(EventAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
    def process(self, event):
        event.FatjetAK08ungroomed = FatjetAK08ungroomed.make_array(event.input)
        event.FatjetCA15pruned = FatjetCA15pruned.make_array(event.input)
        event.FatjetCA15softdrop = FatjetCA15softdrop.make_array(event.input)
        event.FatjetCA15softdropz2b1 = FatjetCA15softdropz2b1.make_array(event.input)
        event.FatjetCA15subjetfiltered = FatjetCA15subjetfiltered.make_array(event.input)
        event.FatjetCA15trimmed = FatjetCA15trimmed.make_array(event.input)
        event.FatjetCA15ungroomed = FatjetCA15ungroomed.make_array(event.input)
        event.Flag_hbheFilterNew = getattr(event.input, "Flag_hbheFilterNew", None)
        event.Flag_hbheIsoFilter = getattr(event.input, "Flag_hbheIsoFilter", None)
        event.GenBQuarkFromH = GenBQuarkFromH.make_array(event.input)
        event.GenBQuarkFromHafterISR = GenBQuarkFromHafterISR.make_array(event.input)
        event.GenBQuarkFromTop = GenBQuarkFromTop.make_array(event.input)
        event.GenHadTaus = GenHadTaus.make_array(event.input)
        event.GenHiggsBoson = GenHiggsBoson.make_array(event.input)
        event.GenHiggsSisters = GenHiggsSisters.make_array(event.input)
        event.GenJet = GenJet.make_array(event.input)
        event.GenLep = GenLep.make_array(event.input)
        event.GenLepFromTau = GenLepFromTau.make_array(event.input)
        event.GenLepFromTauRecovered = GenLepFromTauRecovered.make_array(event.input)
        event.GenLepFromTop = GenLepFromTop.make_array(event.input)
        event.GenLepRecovered = GenLepRecovered.make_array(event.input)
        event.GenNuFromTop = GenNuFromTop.make_array(event.input)
        event.GenStatus2bHad = GenStatus2bHad.make_array(event.input)
        event.GenTaus = GenTaus.make_array(event.input)
        event.GenTausRecovered = GenTausRecovered.make_array(event.input)
        event.GenTop = GenTop.make_array(event.input)
        event.GenVbosons = GenVbosons.make_array(event.input)
        event.GenVbosonsRecovered = GenVbosonsRecovered.make_array(event.input)
        event.GenWZQuark = GenWZQuark.make_array(event.input)
        event.H = H.make_obj(event.input)
        event.HCSV = HCSV.make_obj(event.input)
        event.HCSV_reg = HCSV_reg.make_obj(event.input)
        event.HCSV_reg_corrJECDown = HCSV_reg_corrJECDown.make_obj(event.input)
        event.HCSV_reg_corrJECUp = HCSV_reg_corrJECUp.make_obj(event.input)
        event.HCSV_reg_corrJERDown = HCSV_reg_corrJERDown.make_obj(event.input)
        event.HCSV_reg_corrJERUp = HCSV_reg_corrJERUp.make_obj(event.input)
        event.HVdPhi = getattr(event.input, "HVdPhi", None)
        event.H_reg = H_reg.make_obj(event.input)
        event.H_reg_corrJECDown = H_reg_corrJECDown.make_obj(event.input)
        event.H_reg_corrJECUp = H_reg_corrJECUp.make_obj(event.input)
        event.H_reg_corrJERDown = H_reg_corrJERDown.make_obj(event.input)
        event.H_reg_corrJERUp = H_reg_corrJERUp.make_obj(event.input)
        event.HaddJetsdR08 = HaddJetsdR08.make_obj(event.input)
        event.Jet = Jet.make_array(event.input)
        event.LHE_weights_pdf = LHE_weights_pdf.make_array(event.input)
        event.LHE_weights_scale = LHE_weights_scale.make_array(event.input)
        event.SubjetAK08softdrop = SubjetAK08softdrop.make_array(event.input)
        event.SubjetCA15pruned = SubjetCA15pruned.make_array(event.input)
        event.SubjetCA15softdrop = SubjetCA15softdrop.make_array(event.input)
        event.SubjetCA15softdropz2b1 = SubjetCA15softdropz2b1.make_array(event.input)
        event.SubjetCA15subjetfiltered = SubjetCA15subjetfiltered.make_array(event.input)
        event.TauGood = TauGood.make_array(event.input)
        event.V = V.make_obj(event.input)
        event.VMt = getattr(event.input, "VMt", None)
        event.Vtype = getattr(event.input, "Vtype", None)
        event.VtypeSim = getattr(event.input, "VtypeSim", None)
        event.aJCidx = aJCidx.make_array(event.input)
        event.aJidx = aJidx.make_array(event.input)
        event.aLeptons = aLeptons.make_array(event.input)
        event.ajidxaddJetsdR08 = ajidxaddJetsdR08.make_array(event.input)
        event.bTagWeight = getattr(event.input, "bTagWeight", None)
        event.bTagWeight_HFDown = getattr(event.input, "bTagWeight_HFDown", None)
        event.bTagWeight_HFStats1Down = getattr(event.input, "bTagWeight_HFStats1Down", None)
        event.bTagWeight_HFStats1Up = getattr(event.input, "bTagWeight_HFStats1Up", None)
        event.bTagWeight_HFStats2Down = getattr(event.input, "bTagWeight_HFStats2Down", None)
        event.bTagWeight_HFStats2Up = getattr(event.input, "bTagWeight_HFStats2Up", None)
        event.bTagWeight_HFUp = getattr(event.input, "bTagWeight_HFUp", None)
        event.bTagWeight_JESDown = getattr(event.input, "bTagWeight_JESDown", None)
        event.bTagWeight_JESUp = getattr(event.input, "bTagWeight_JESUp", None)
        event.bTagWeight_LFDown = getattr(event.input, "bTagWeight_LFDown", None)
        event.bTagWeight_LFStats1Down = getattr(event.input, "bTagWeight_LFStats1Down", None)
        event.bTagWeight_LFStats1Up = getattr(event.input, "bTagWeight_LFStats1Up", None)
        event.bTagWeight_LFStats2Down = getattr(event.input, "bTagWeight_LFStats2Down", None)
        event.bTagWeight_LFStats2Up = getattr(event.input, "bTagWeight_LFStats2Up", None)
        event.bTagWeight_LFUp = getattr(event.input, "bTagWeight_LFUp", None)
        event.bTagWeight_cErr1Down = getattr(event.input, "bTagWeight_cErr1Down", None)
        event.bTagWeight_cErr1Up = getattr(event.input, "bTagWeight_cErr1Up", None)
        event.bTagWeight_cErr2Down = getattr(event.input, "bTagWeight_cErr2Down", None)
        event.bTagWeight_cErr2Up = getattr(event.input, "bTagWeight_cErr2Up", None)
        event.bx = getattr(event.input, "bx", None)
        event.caloMetPhi = getattr(event.input, "caloMetPhi", None)
        event.caloMetPt = getattr(event.input, "caloMetPt", None)
        event.dRaddJetsdR08 = dRaddJetsdR08.make_array(event.input)
        event.deltaR_jj = getattr(event.input, "deltaR_jj", None)
        event.fakeMET = fakeMET.make_obj(event.input)
        event.fakeMET_sumet = getattr(event.input, "fakeMET_sumet", None)
        event.genHiggsDecayMode = getattr(event.input, "genHiggsDecayMode", None)
        event.genTTHtoTauTauDecayMode = getattr(event.input, "genTTHtoTauTauDecayMode", None)
        event.hJCidx = hJCidx.make_array(event.input)
        event.hJidx = hJidx.make_array(event.input)
        event.hJidx_sortcsv = hJidx_sortcsv.make_array(event.input)
        event.heavyFlavourCategory = getattr(event.input, "heavyFlavourCategory", None)
        event.hjidxaddJetsdR08 = hjidxaddJetsdR08.make_array(event.input)
        event.htJet30 = getattr(event.input, "htJet30", None)
        event.httCandidates = httCandidates.make_array(event.input)
        event.isrJetVH = getattr(event.input, "isrJetVH", None)
        event.json = getattr(event.input, "json", None)
        event.json_silver = getattr(event.input, "json_silver", None)
        event.lheHT = getattr(event.input, "lheHT", None)
        event.lheNb = getattr(event.input, "lheNb", None)
        event.lheNc = getattr(event.input, "lheNc", None)
        event.lheNg = getattr(event.input, "lheNg", None)
        event.lheNj = getattr(event.input, "lheNj", None)
        event.lheNl = getattr(event.input, "lheNl", None)
        event.lheV_pt = getattr(event.input, "lheV_pt", None)
        event.met = met.make_obj(event.input)
        event.metPuppi_phi = getattr(event.input, "metPuppi_phi", None)
        event.metPuppi_pt = getattr(event.input, "metPuppi_pt", None)
        event.metPuppi_rawpt = getattr(event.input, "metPuppi_rawpt", None)
        event.metType1p2_pt = getattr(event.input, "metType1p2_pt", None)
        event.met_rawpt = getattr(event.input, "met_rawpt", None)
        event.met_shifted_ElectronEnDown = met_shifted_ElectronEnDown.make_obj(event.input)
        event.met_shifted_ElectronEnUp = met_shifted_ElectronEnUp.make_obj(event.input)
        event.met_shifted_JetEnDown = met_shifted_JetEnDown.make_obj(event.input)
        event.met_shifted_JetEnUp = met_shifted_JetEnUp.make_obj(event.input)
        event.met_shifted_JetResDown = met_shifted_JetResDown.make_obj(event.input)
        event.met_shifted_JetResUp = met_shifted_JetResUp.make_obj(event.input)
        event.met_shifted_MuonEnDown = met_shifted_MuonEnDown.make_obj(event.input)
        event.met_shifted_MuonEnUp = met_shifted_MuonEnUp.make_obj(event.input)
        event.met_shifted_TauEnDown = met_shifted_TauEnDown.make_obj(event.input)
        event.met_shifted_TauEnUp = met_shifted_TauEnUp.make_obj(event.input)
        event.met_shifted_UnclusteredEnDown = met_shifted_UnclusteredEnDown.make_obj(event.input)
        event.met_shifted_UnclusteredEnUp = met_shifted_UnclusteredEnUp.make_obj(event.input)
        event.met_sig = getattr(event.input, "met_sig", None)
        event.mhtJet30 = getattr(event.input, "mhtJet30", None)
        event.mhtPhiJet30 = getattr(event.input, "mhtPhiJet30", None)
        event.nPU0 = getattr(event.input, "nPU0", None)
        event.nPVs = getattr(event.input, "nPVs", None)
        event.pileUpVertex_ptHat = pileUpVertex_ptHat.make_array(event.input)
        event.pileUpVertex_z = pileUpVertex_z.make_array(event.input)
        event.primaryVertices = primaryVertices.make_array(event.input)
        event.puWeightDown = getattr(event.input, "puWeightDown", None)
        event.puWeightUp = getattr(event.input, "puWeightUp", None)
        event.rho = getattr(event.input, "rho", None)
        event.rhoCHPU = getattr(event.input, "rhoCHPU", None)
        event.rhoCentral = getattr(event.input, "rhoCentral", None)
        event.rhoN = getattr(event.input, "rhoN", None)
        event.selLeptons = selLeptons.make_array(event.input)
        event.simPrimaryVertex_z = getattr(event.input, "simPrimaryVertex_z", None)
        event.softActivity = softActivity.make_obj(event.input)
        event.softActivityJets = softActivityJets.make_array(event.input)
        event.softActivityVH = softActivityVH.make_obj(event.input)
        event.softActivityVHJets = softActivityVHJets.make_array(event.input)
        event.tkMetPVchs_phi = getattr(event.input, "tkMetPVchs_phi", None)
        event.tkMetPVchs_pt = getattr(event.input, "tkMetPVchs_pt", None)
        event.tkMet_phi = getattr(event.input, "tkMet_phi", None)
        event.tkMet_pt = getattr(event.input, "tkMet_pt", None)
        event.trgObjects_caloJets = trgObjects_caloJets.make_array(event.input)
        event.trgObjects_caloMet = trgObjects_caloMet.make_array(event.input)
        event.trgObjects_caloMht = trgObjects_caloMht.make_array(event.input)
        event.trgObjects_caloMhtNoPU = trgObjects_caloMhtNoPU.make_array(event.input)
        event.trgObjects_hltBTagCaloCSVp014DoubleWithMatching = trgObjects_hltBTagCaloCSVp014DoubleWithMatching.make_array(event.input)
        event.trgObjects_hltBTagCaloCSVp022Single = trgObjects_hltBTagCaloCSVp022Single.make_array(event.input)
        event.trgObjects_hltBTagCaloCSVp026DoubleWithMatching = trgObjects_hltBTagCaloCSVp026DoubleWithMatching.make_array(event.input)
        event.trgObjects_hltBTagCaloCSVp067Single = trgObjects_hltBTagCaloCSVp067Single.make_array(event.input)
        event.trgObjects_hltBTagCaloCSVp087Triple = trgObjects_hltBTagCaloCSVp087Triple.make_array(event.input)
        event.trgObjects_hltBTagPFCSVp016SingleWithMatching = trgObjects_hltBTagPFCSVp016SingleWithMatching.make_array(event.input)
        event.trgObjects_hltBTagPFCSVp11DoubleWithMatching = trgObjects_hltBTagPFCSVp11DoubleWithMatching.make_array(event.input)
        event.trgObjects_hltDoubleCentralJet90 = trgObjects_hltDoubleCentralJet90.make_array(event.input)
        event.trgObjects_hltDoubleJet65 = trgObjects_hltDoubleJet65.make_array(event.input)
        event.trgObjects_hltDoublePFCentralJetLooseID90 = trgObjects_hltDoublePFCentralJetLooseID90.make_array(event.input)
        event.trgObjects_hltDoublePFJetsC100 = trgObjects_hltDoublePFJetsC100.make_array(event.input)
        event.trgObjects_hltEle25WPTight = trgObjects_hltEle25WPTight.make_array(event.input)
        event.trgObjects_hltEle25eta2p1WPLoose = trgObjects_hltEle25eta2p1WPLoose.make_array(event.input)
        event.trgObjects_hltIsoMu20 = trgObjects_hltIsoMu20.make_array(event.input)
        event.trgObjects_hltL1sETM50ToETM100IorETM60Jet60dPhiMin0p4IorDoubleJetC60ETM60 = trgObjects_hltL1sETM50ToETM100IorETM60Jet60dPhiMin0p4IorDoubleJetC60ETM60.make_array(event.input)
        event.trgObjects_hltL1sQuadJetCIorTripleJetVBFIorHTT = trgObjects_hltL1sQuadJetCIorTripleJetVBFIorHTT.make_array(event.input)
        event.trgObjects_hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet = trgObjects_hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet.make_array(event.input)
        event.trgObjects_hltMET70 = trgObjects_hltMET70.make_array(event.input)
        event.trgObjects_hltMHT70 = trgObjects_hltMHT70.make_array(event.input)
        event.trgObjects_hltMHTNoPU90 = trgObjects_hltMHTNoPU90.make_array(event.input)
        event.trgObjects_hltPFDoubleJetLooseID76 = trgObjects_hltPFDoubleJetLooseID76.make_array(event.input)
        event.trgObjects_hltPFMET90 = trgObjects_hltPFMET90.make_array(event.input)
        event.trgObjects_hltPFMHTTightID90 = trgObjects_hltPFMHTTightID90.make_array(event.input)
        event.trgObjects_hltPFQuadJetLooseID15 = trgObjects_hltPFQuadJetLooseID15.make_array(event.input)
        event.trgObjects_hltPFSingleJetLooseID92 = trgObjects_hltPFSingleJetLooseID92.make_array(event.input)
        event.trgObjects_hltPFTripleJetLooseID64 = trgObjects_hltPFTripleJetLooseID64.make_array(event.input)
        event.trgObjects_hltQuadCentralJet30 = trgObjects_hltQuadCentralJet30.make_array(event.input)
        event.trgObjects_hltQuadCentralJet45 = trgObjects_hltQuadCentralJet45.make_array(event.input)
        event.trgObjects_hltQuadJet15 = trgObjects_hltQuadJet15.make_array(event.input)
        event.trgObjects_hltQuadPFCentralJetLooseID30 = trgObjects_hltQuadPFCentralJetLooseID30.make_array(event.input)
        event.trgObjects_hltQuadPFCentralJetLooseID45 = trgObjects_hltQuadPFCentralJetLooseID45.make_array(event.input)
        event.trgObjects_hltSingleJet80 = trgObjects_hltSingleJet80.make_array(event.input)
        event.trgObjects_hltTripleJet50 = trgObjects_hltTripleJet50.make_array(event.input)
        event.trgObjects_hltVBFCaloJetEtaSortedMqq150Deta1p5 = trgObjects_hltVBFCaloJetEtaSortedMqq150Deta1p5.make_array(event.input)
        event.trgObjects_hltVBFPFJetCSVSortedMqq200Detaqq1p2 = trgObjects_hltVBFPFJetCSVSortedMqq200Detaqq1p2.make_array(event.input)
        event.trgObjects_hltVBFPFJetCSVSortedMqq460Detaqq4p1 = trgObjects_hltVBFPFJetCSVSortedMqq460Detaqq4p1.make_array(event.input)
        event.trgObjects_pfHt = trgObjects_pfHt.make_array(event.input)
        event.trgObjects_pfJets = trgObjects_pfJets.make_array(event.input)
        event.trgObjects_pfMet = trgObjects_pfMet.make_array(event.input)
        event.trgObjects_pfMht = trgObjects_pfMht.make_array(event.input)
        event.ttCls = getattr(event.input, "ttCls", None)
        event.vLeptons = vLeptons.make_array(event.input)
