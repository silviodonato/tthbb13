// -*- C++ -*-
//
// Package:    TTH/TTHNtupleAnalyzer
// Class:      TTHNtupleAnalyzer
//
/**\class TTHNtupleAnalyzer TTHNtupleAnalyzer.cc TTH/TTHNtupleAnalyzer/plugins/TTHNtupleAnalyzer.cc

 Description: A simple N-tuplizer for TTH(->bb), mapping the EDM miniAOD format to a "simple flat ROOT TTree"

 Implementation:
    Based on https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
    The base event is described by TTHTree, implemented in tth_tree.hh (autogenerated by tree_header.jl based on a specification)

    Tests for this module are in test/runtests.sh

    Helpful links:
        https://github.com/CJLST/ZZAnalysis/wiki/miniAOD-twiki
        https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD
*/
//
// Original Author:  Joosep Pata
//         Created:  Tue, 15 Jul 2014 10:06:28 GMT
//
//


// system include files
#include <memory>
#include <algorithm>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

//for top tagger
#include "DataFormats/JetReco/interface/CATopJetTagInfo.h"

#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

//#include "CommonTools/UtilAlgos/interface/PhysObjectMatcher.h"
//#include "CommonTools/UtilAlgos/interface/MatchByDRDPt.h"
//#include "CommonTools/UtilAlgos/interface/MatchLessByDPt.h"
//#include "CommonTools/UtilAlgos/interface/MCMatchSelector.h"
#include <EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h>

#include "TTH/TTHNtupleAnalyzer/interface/tth_tree.hh"
#include "TStopwatch.h"

#define CANDPRINT(x) " pt=" << x.pt() << " eta=" << x.eta() << " phi=" << x.phi() << " id=" << x.pdgId() << " st=" << x.status()
#define PCANDPRINT(x) " pt=" << x->pt() << " eta=" << x->eta() << " phi=" << x->phi() << " id=" << x->pdgId() << " st=" << x->status()
#define GENJET_DR 0.5
#define GENJET_REL_DP 0.5

#define GENLEPTON_DR 0.5
#define GENLEPTON_REL_DP 0.5

template <typename T, typename R>
std::vector<R> to_ptrvec(T coll) {
    std::vector<R> ret;
    for (auto e : coll) {
        assert(&e != NULL);
        ret.push_back((R)&e);
    }
    return ret;
}

template <typename T>
bool sort_by_pt(T a, T b) {
    assert(a!=NULL && b!=NULL);
    return (a->pt() > b->pt());
};

const reco::GenParticle* find_dr_dp_id_match(const reco::Candidate& x, edm::Handle<edm::View<reco::GenParticle>> pruned) {
    std::vector<const reco::GenParticle*> matched;
    for (auto& p : *pruned) {
        const float dr = sqrt(reco::deltaR2(x.p4(), p.p4()));
        const float rel_dp = fabs(x.pt()-p.pt())/p.pt();
        //LogDebug("jets") << "dR=" << dr << " rel_dp=" << rel_dp;
        if (dr<GENLEPTON_DR && rel_dp<GENLEPTON_REL_DP && x.pdgId()==p.pdgId()) {
            matched.push_back(&p);
        }
    }
    LogDebug("find_dr_dp_id_match") << "dR < " << GENLEPTON_DR << " matched " << matched.size();

    //sort genparticles by dR(recojet, genparticle) ascending
    auto sortf = [&x](const reco::GenParticle* a, const reco::GenParticle* b) -> bool {
        return (reco::deltaR2(x.p4(), a->p4()) < reco::deltaR2(x.p4(), b->p4()));
    };

    std::sort(matched.begin(), matched.end(), sortf);
    //if we had at least one match, choose lowest dR
    if (matched.size()>0) {
        LogDebug("find_dr_dp_id_match") << "best match " << PCANDPRINT(matched[0]);
        return matched[0];
    } else {
        return (const reco::GenParticle*)NULL;
    }
}

class TTHNtupleAnalyzer : public edm::EDAnalyzer {
public:
    explicit TTHNtupleAnalyzer(const edm::ParameterSet&);
    ~TTHNtupleAnalyzer();

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


private:
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    virtual void finalizeLoop();

    const edm::EDGetTokenT<pat::MuonCollection> muonToken_;
    const edm::EDGetTokenT<pat::ElectronCollection> electronToken_;
    const edm::EDGetTokenT<pat::TauCollection> tauToken_;
    const edm::EDGetTokenT<pat::JetCollection> jetToken_;
    const edm::EDGetTokenT<edm::View<reco::BasicJet>> topJetToken_;
    const edm::EDGetTokenT<edm::View<reco::CATopJetTagInfo>> topJetInfoToken_;
    const edm::EDGetTokenT<reco::VertexCollection> vertexToken_;

    const edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;
    const edm::EDGetTokenT<edm::View<pat::PackedGenParticle> > packedGenToken_;

    const edm::EDGetTokenT<pat::JetCollection> fatjetToken_;
    const edm::EDGetTokenT<pat::METCollection> metToken_;

    const edm::EDGetTokenT<LHEEventProduct> lheToken_;

    TTHTree* tthtree;
    const edm::Service<TFileService> fs;
    const bool isMC;

    TStopwatch* sw;

    const std::vector<std::string> tauIdentifiers_;
    const std::vector<std::string> eleIdentifiers_;
    //const ElectronEffectiveArea::ElectronEffectiveAreaType electron_eff_area_type = ElectronEffectiveArea::ElectronEffectiveAreaType::kEleGammaAndNeutralHadronIso03;
    //const ElectronEffectiveArea::ElectronEffectiveAreaType electron_eff_area_target = ElectronEffectiveArea::ElectronEffectiveAreaTarget::kEleEAData2012;
};

TTHTree::TTHTree(TTree* _tree) {
    tree = _tree;
    loop_initialize();
    make_branches();
}

TTHNtupleAnalyzer::TTHNtupleAnalyzer(const edm::ParameterSet& iConfig) :
    muonToken_(consumes<pat::MuonCollection>(iConfig.getParameter<edm::InputTag>("muons"))),
    electronToken_(consumes<pat::ElectronCollection>(iConfig.getParameter<edm::InputTag>("electrons"))),
    tauToken_(consumes<pat::TauCollection>(iConfig.getParameter<edm::InputTag>("taus"))),
    jetToken_(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>("jets"))),
    topJetToken_(consumes<edm::View<reco::BasicJet>>(iConfig.getParameter<edm::InputTag>("topjets"))),
    topJetInfoToken_(consumes<edm::View<reco::CATopJetTagInfo>>(iConfig.getParameter<edm::InputTag>("topjetinfos"))),
    vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
    prunedGenToken_(consumes<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("pruned"))),
    packedGenToken_(consumes<edm::View<pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("packed"))),
    fatjetToken_(consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>("fatjets"))),
    metToken_(consumes<pat::METCollection>(iConfig.getParameter<edm::InputTag>("mets"))),
    lheToken_(consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lhe"))),
    tthtree(new TTHTree(fs->make<TTree>("events", "events"))),
    isMC(iConfig.getParameter<bool>("isMC")),
    tauIdentifiers_(iConfig.getParameter<std::vector<std::string>>("tauIdentifiers")),
    eleIdentifiers_(iConfig.getParameter<std::vector<std::string>>("eleIdentifiers"))
{
    sw = new TStopwatch();
}


TTHNtupleAnalyzer::~TTHNtupleAnalyzer()
{
    delete sw;
}

double dbc_rel_iso(const pat::Electron& lepton) {
    return (
               (lepton.chargedHadronIso() +
                std::max(0.0, lepton.neutralHadronIso() + lepton.photonIso() - 0.5*lepton.puChargedHadronIso()))/lepton.pt()
           );
}

double dbc_rel_iso(const pat::Muon& lepton) {
    return (
               (lepton.chargedHadronIso() +
                std::max(0.0, lepton.neutralHadronIso() + lepton.photonIso() - 0.5*lepton.puChargedHadronIso()))/lepton.pt()
           );
}

void TTHNtupleAnalyzer::finalizeLoop() {
}

// ------------ method called for each event  ------------
void
TTHNtupleAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    sw->Start();
    tthtree->loop_initialize();

    tthtree->event__id = (unsigned int)iEvent.id().event();
    tthtree->event__run = (unsigned int)iEvent.id().run();
    tthtree->event__lumi = (unsigned int)iEvent.id().luminosityBlock();

//Primary vertices
    edm::Handle<reco::VertexCollection> vertices;
    iEvent.getByToken(vertexToken_, vertices);
    if (vertices->empty()) {
        edm::LogError("loop") << "no vertices found";
        finalizeLoop();
        return;
    }
    const reco::Vertex &PV = vertices->front();
    tthtree->n__pv = vertices->size();

//Pileup
    if (isMC) {
        Handle<std::vector<PileupSummaryInfo>> PupInfo;
        iEvent.getByLabel(edm::InputTag("addPileupInfo"), PupInfo);
        std::vector<PileupSummaryInfo>::const_iterator PVI;
        tthtree->n__pvi = PupInfo->size();
        int n_pu = 0;
        for (PVI = PupInfo->begin(); PVI != PupInfo->end(); ++PVI)
        {
            const int BX = PVI->getBunchCrossing();
            LogDebug("PVI") << n_pu << " BX=" << BX;
            tthtree->pvi__n0[n_pu] = PVI->getPU_NumInteractions();
            tthtree->pvi__bx[n_pu] = BX;
            if (BX == 0)
            {
                tthtree->pvi__ntrue[n_pu] = PVI->getTrueNumInteractions();
            }
            n_pu += 1;
        }
    }

    edm::Handle<pat::MuonCollection> muons;
    iEvent.getByToken(muonToken_, muons);

    Handle<edm::View<reco::GenParticle> > pruned;
    iEvent.getByToken(prunedGenToken_,pruned);

    int n__lep = 0;

    int n_mu = 0;
    int n_ele = 0;
    int n_tau = 0;

    int n__jet = 0;

    for (const pat::Muon &x : *muons) {
        LogDebug("muons") << "n_mu=" << n_mu <<
                          " pt=" << x.pt() <<
                          " dz(PV)=" << x.muonBestTrack()->dz(PV.position()) <<
                          " lID=" << x.isLooseMuon() <<
                          " tID=" << x.isTightMuon(PV);
        tthtree->lep__eta[n__lep] = x.eta();
        tthtree->lep__pt[n__lep] = x.pt();
        tthtree->lep__phi[n__lep] = x.phi();
        tthtree->lep__mass[n__lep] = x.mass();
        tthtree->lep__id[n__lep] = x.pdgId();
        tthtree->lep__charge[n__lep] = x.charge();
        tthtree->lep__is_tight[n__lep] = x.isTightMuon(PV);
        tthtree->lep__is_loose[n__lep] = x.isLooseMuon();

        tthtree->lep__ch_iso[n__lep] = x.chargedHadronIso();
        tthtree->lep__puch_iso[n__lep] = x.puChargedHadronIso();
        tthtree->lep__ec_iso[n__lep] = x.ecalIso();
        tthtree->lep__hc_iso[n__lep] = x.hcalIso();
        tthtree->lep__p_iso[n__lep] = x.particleIso();
        tthtree->lep__ph_iso[n__lep] = x.photonIso();

        //manual DBC iso
        //const auto& pfiso = x.pfIsolationR04();
        //tthtree->lep__rel_iso[n__lep] = (pfiso.sumChargedHadronPt + std::max(0.0, pfiso.sumNeutralHadronEt + pfiso.sumPhotonEt - 0.5 * pfiso.sumPUPt))/x.pt();

        //automatic delta-beta relative isolation
        tthtree->lep__rel_iso[n__lep] = dbc_rel_iso(x);

        if (x.muonBestTrack().isNonnull()) {
            tthtree->lep__dxy[n__lep] = x.muonBestTrack()->dxy(PV.position());
            tthtree->lep__dz[n__lep] = x.muonBestTrack()->dz(PV.position());
        } else {
            edm::LogWarning("muon") << "gsfTrack is 0 for n_mu=" << n_mu;
        }
        if (isMC) {
            const reco::GenParticle* gp = x.genParticle();
            if (gp == NULL) {
                LogDebug("muon") << "n__lep=" << n__lep << " does not have genParticle(), doing dR/dP matching";
                gp = find_dr_dp_id_match(x, pruned);
            }
            if (x.genParticle() != NULL) {
                tthtree->gen_lep__eta[n__lep] = gp->eta();
                tthtree->gen_lep__pt[n__lep] = gp->pt();
                tthtree->gen_lep__phi[n__lep] = gp->phi();
                tthtree->gen_lep__mass[n__lep] = gp->mass();
                tthtree->gen_lep__id[n__lep] = gp->pdgId();
                tthtree->gen_lep__status[n__lep] = gp->status();
            } else {
                LogDebug("muons") << "genParticle()==0 for muon n_mu=" << n_mu;
            }
        }
        n_mu += 1;
        n__lep += 1;
    }

    edm::Handle<pat::ElectronCollection> electrons;
    iEvent.getByToken(electronToken_, electrons);
    for (const pat::Electron &x : *electrons) {
        LogDebug("electrons") << "n_ele=" << n_ele <<
                              " pt=" << x.pt();
        tthtree->lep__eta[n__lep] = x.eta();
        tthtree->lep__pt[n__lep] = x.pt();
        tthtree->lep__phi[n__lep] = x.phi();
        tthtree->lep__mass[n__lep] = x.mass();
        tthtree->lep__id[n__lep] = x.pdgId();
        tthtree->lep__charge[n__lep] = x.charge();

        tthtree->lep__ch_iso[n__lep] = x.chargedHadronIso();
        tthtree->lep__puch_iso[n__lep] = x.puChargedHadronIso();
        tthtree->lep__ec_iso[n__lep] = x.ecalIso();
        tthtree->lep__hc_iso[n__lep] = x.hcalIso();
        tthtree->lep__p_iso[n__lep] = x.particleIso();
        tthtree->lep__ph_iso[n__lep] = x.photonIso();

        //manual rho-corrected, probably deprecated
        //const double eff_area = ElectronEffectiveArea::GetElectronEffectiveArea(
        //    electron_eff_area_type,
        //    x.eta(),
        //    electron_eff_area_target
        //);
        //isocorr = PFChargedIso (PFNoPU) + max(PFIso(γ+NH) - rho * Aeff(γ+NH), 0.)
        //float rc_iso = (lepton.chargedHadronIso() + std::max(0., lepton.neutralHadronIso() + lepton.photonIso() - ea*(*rho)))/lepton.userFloat("ptCorr");
        tthtree->lep__rel_iso[n__lep] = dbc_rel_iso(x);

        //FIXME: implement tight/loose definition
        tthtree->lep__is_tight[n__lep] = (x.passConversionVeto());
        //tthtree->lep__is_loose[n__lep] = x.isLooseElectron();

        unsigned int ele_id_idx = 0;
        tthtree->lep__id_bitmask[n__lep] = 0;
        for (const auto& ele_id : eleIdentifiers_) {
            LogDebug("ele") << " n__lep=" << n__lep << " ID(" << ele_id << ")=" << x.electronID(ele_id);
            if (x.electronID(ele_id)) {
                //passes, flip bit with index tau_id_idx to ON
                tthtree->lep__id_bitmask[n__lep] = tthtree->lep__id_bitmask[n__lep] | (1 << ele_id_idx);
            } else {
                //fails, flip bit with index tau_id_idx to OFF
                tthtree->lep__id_bitmask[n__lep] = tthtree->lep__id_bitmask[n__lep] & ~(1 << ele_id_idx);
            }
            ele_id_idx += 1;
            if (ele_id_idx>= 32) {
                edm::LogWarning("ele") << "More electron ID-s specified than can fit in bitmask, truncating after " << ele_id;
                break;
            }
        }

        if (x.gsfTrack().isNonnull()) {
            tthtree->lep__dxy[n__lep] = x.gsfTrack()->dxy(PV.position());
            tthtree->lep__dz[n__lep] = x.gsfTrack()->dz(PV.position());
        } else {
            edm::LogWarning("electron") << "gsfTrack is 0 for n_ele=" << n_ele;
        }
        if (isMC) {
            const reco::GenParticle* gp = x.genParticle();
            if (gp == NULL) {
                LogDebug("electron") << "n__lep=" << n__lep << " does not have genParticle(), doing dR/dP matching";
                gp = find_dr_dp_id_match(x, pruned);
            }
            if (gp != NULL) {
                tthtree->gen_lep__eta[n__lep] = gp->eta();
                tthtree->gen_lep__pt[n__lep] = gp->pt();
                tthtree->gen_lep__phi[n__lep] = gp->phi();
                tthtree->gen_lep__mass[n__lep] = gp->mass();
                tthtree->gen_lep__id[n__lep] = gp->pdgId();
                tthtree->gen_lep__status[n__lep] = gp->status();
            } else {
                LogDebug("electron") << "genParticle()==0 for electron n_ele=" << n_ele;
            }
        }
        n_ele += 1;
        n__lep += 1;
    }

    edm::Handle<pat::TauCollection> taus;
    iEvent.getByToken(tauToken_, taus);
    for (const pat::Tau &x : *taus) {
        LogDebug("taus") << "n_tau=" << n_tau <<
                         " pt=" << x.pt();
        tthtree->lep__eta[n__lep] = x.eta();
        tthtree->lep__pt[n__lep] = x.pt();
        tthtree->lep__phi[n__lep] = x.phi();
        tthtree->lep__mass[n__lep] = x.mass();
        tthtree->lep__id[n__lep] = x.pdgId();
        tthtree->lep__charge[n__lep] = x.charge();

        tthtree->lep__ch_iso[n__lep] = x.chargedHadronIso();
        tthtree->lep__puch_iso[n__lep] = x.puChargedHadronIso();
        tthtree->lep__ec_iso[n__lep] = x.ecalIso();
        tthtree->lep__hc_iso[n__lep] = x.hcalIso();
        tthtree->lep__p_iso[n__lep] = x.particleIso();
        tthtree->lep__ph_iso[n__lep] = x.photonIso();

        //Bit-shift specified tau id-s into the id_bitmask
        //Order is specified in the python config
        //http://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit-in-c-c
        unsigned int tau_id_idx = 0;
        tthtree->lep__id_bitmask[n__lep] = 0;
        for (const auto& tau_id : tauIdentifiers_) {
            if (x.tauID(tau_id)) {
                //passes, flip bit with index tau_id_idx to ON
                tthtree->lep__id_bitmask[n__lep] = tthtree->lep__id_bitmask[n__lep] | (1 << tau_id_idx);
            } else {
                //fails, flip bit with index tau_id_idx to OFF
                tthtree->lep__id_bitmask[n__lep] = tthtree->lep__id_bitmask[n__lep] & ~(1 << tau_id_idx);
            }
            tau_id_idx += 1;
            if (tau_id_idx>= 32) {
                edm::LogWarning("tau") << "More tau ID-s specified than can fit in bitmask, truncating after " << tau_id;
                break;
            }
        }


        if (x.leadTrack().isNonnull()) {
            tthtree->lep__dxy[n__lep] = x.leadTrack()->dxy(PV.position());
            tthtree->lep__dz[n__lep] = x.leadTrack()->dz(PV.position());
        } else {
            LogDebug("tau") << "leadTrack is 0 for n_tau=" << n_tau;
        }

        const reco::GenParticle* gp = x.genParticle();
        if (isMC) {
            if (gp == NULL) {
                LogDebug("tau") << "n__lep=" << n__lep << " does not have genParticle(), doing dR/dP matching";
                gp = find_dr_dp_id_match(x, pruned);
            }

            if (gp != NULL) {
                tthtree->gen_lep__eta[n__lep] = gp->eta();
                tthtree->gen_lep__pt[n__lep] = gp->pt();
                tthtree->gen_lep__phi[n__lep] = gp->phi();
                tthtree->gen_lep__mass[n__lep] = gp->mass();
                tthtree->gen_lep__id[n__lep] = gp->pdgId();
                tthtree->gen_lep__status[n__lep] = gp->status();
            } else {
                LogDebug("taus") << "genParticle()==0 for tau n_tau=" << n_tau;
            }
        }
        n_tau += 1;
        n__lep += 1;
    }

    edm::Handle<pat::JetCollection> jets;
    iEvent.getByToken(jetToken_, jets);

    //sort jets by pt
    //auto jetps = to_ptrvec<const std::vector<pat::Jet>&, const pat::Jet*>(*jets);
    //std::sort(jetps.begin(), jetps.end(), sort_by_pt<const pat::Jet*>);

    for (auto x : *jets) {
        //assert(_x != NULL);
        //const pat::Jet& x = *_x;
        LogDebug("jets") << "n__jet=" << n__jet << CANDPRINT(x);
        tthtree->jet__eta[n__jet] = x.eta();
        tthtree->jet__pt[n__jet] = x.pt();
        tthtree->jet__phi[n__jet] = x.phi();
        tthtree->jet__mass[n__jet] = x.mass();
        tthtree->jet__energy[n__jet] = x.energy();
        tthtree->jet__bd_csv[n__jet] = x.bDiscriminator("combinedSecondaryVertexBJetTags");
        tthtree->jet__id[n__jet] = x.partonFlavour();

        tthtree->jet__nh_e[n__jet] = x.neutralHadronEnergy();
        tthtree->jet__ne_e[n__jet] = x.neutralEmEnergy();
        tthtree->jet__ch_e[n__jet] = x.chargedHadronEnergy();
        tthtree->jet__ce_e[n__jet] = x.chargedEmEnergy();
        tthtree->jet__mu_e[n__jet] = x.muonEnergy();
        tthtree->jet__el_e[n__jet] = x.electronEnergy();
        tthtree->jet__ph_e[n__jet] = x.photonEnergy();

        //unsigned int constituent_idx = 0;
        //for (const auto& constituent : x.getJetConstituents()) {
        //    if (n__jet >= M_MAX || constituent_idx >= M_MAX) {
        //        LogDebug("jet") << "jet constituent maximum count reached: n_jet=" << n__jet << " n_constituent=" << constituent_idx << " max=" << M_MAX;
        //        break;
        //    }
        //    if (constituent.isNull()) {
        //        edm::LogWarning("jet") << "jet constituent is null: n_jet=" << n__jet << " n_constituent=" << constituent_idx;
        //        break;
        //    }
        //    tthtree->jet__c_pt[n__jet][constituent_idx] = constituent->pt();
        //    constituent_idx += 1;
        //}

        if (isMC) {
            //generated parton
            const reco::GenParticle* gp = x.genParticle();
            if (gp == NULL) {
                LogDebug("jets") << "n__jet=" << n__jet << " does not have genParticle(), doing dR/dP matching";
                std::vector<const reco::GenParticle*> matched;
                for (auto& p : *pruned) {
                    const float dr = sqrt(reco::deltaR2(x.p4(), p.p4()));
                    const float rel_dp = fabs(x.pt()-p.pt())/p.pt();
                    //LogDebug("jets") << "dR=" << dr << " rel_dp=" << rel_dp;
                    if (dr<GENJET_DR && rel_dp<GENJET_REL_DP) {
                        matched.push_back(&p);
                    }
                }
                LogDebug("jets") << "dR < " << GENJET_DR << " matched " << matched.size();

                //sort genparticles by dR(recojet, genparticle) ascending
                auto sortf = [&x](const reco::GenParticle* a, const reco::GenParticle* b) -> bool {
                    return (reco::deltaR2(x.p4(), a->p4()) < reco::deltaR2(x.p4(), b->p4()));
                };

                std::sort(matched.begin(), matched.end(), sortf);
                //if we had at least one match, choose lowest dR
                if (matched.size()>0) {
                    gp = matched[0];
                    LogDebug("jets") << "best match " << PCANDPRINT(gp);
                }
            }

            if (gp != NULL) {
                tthtree->gen_jet_parton__eta[n__jet] = gp->eta();
                tthtree->gen_jet_parton__pt[n__jet] = gp->pt();
                tthtree->gen_jet_parton__phi[n__jet] = gp->phi();
                tthtree->gen_jet_parton__mass[n__jet] = gp->mass();
                tthtree->gen_jet_parton__id[n__jet] = gp->pdgId();
                tthtree->gen_jet_parton__status[n__jet] = gp->status();

                //we can also loop over the gen particle mothers
                for (auto _m : gp->motherRefVector()) {
                    if (_m.isNull()) {
                        continue;
                    }
                    auto& m = *_m;
                    LogDebug("jets") << "jet " << n__jet << " genParticle mother " << CANDPRINT(m);
                }
            } else {
                LogDebug("jets") << "jet " << n__jet << " genParticle==0";
            }

            //generator-level jet
            const reco::GenJet* gj = x.genJet();
            if (gj != NULL) {
                tthtree->gen_jet__eta[n__jet] = gj->eta();
                tthtree->gen_jet__pt[n__jet] = gj->pt();
                tthtree->gen_jet__phi[n__jet] = gj->phi();
                tthtree->gen_jet__mass[n__jet] = gj->mass();
                tthtree->gen_jet__id[n__jet] = gj->pdgId();
                tthtree->gen_jet__status[n__jet] = gj->status();

                ////Get generator level constituents
                ////FIXME: do we want to save the constituents or just perform some maths on it?
                //unsigned int i = 0;
                //for (auto cn : gj->getGenConstituents()) {
                //    if (i >= M_MAX || n__jet >= M_MAX) {
                //        LogDebug("jets") << "constituent " << i << " loop iteration exceeded M_MAX=" << M_MAX;
                //        break;
                //    }
                //    if (cn != NULL) {
                //        LogDebug("jets") << "constituent " << i << " is null";
                //        continue;
                //    } else {
                //        LogDebug("jets") << "constituent " << i << " is not null";
                //    }
                //    LogDebug("jets") << "constituent " << i << cn->pt();
                //    LogDebug("jets") << "constituent " << i << " " << PCANDPRINT(cn);
                //    LogDebug("jets") << "constituent " << i << " end of loop";
                //    i += 1;
                //}


            } else {
                LogDebug("jet") << "jet " << n__jet << " did not have genJet";
            }
        }
        n__jet += 1;
    }

    //Top tagger jets
    edm::Handle<edm::View<reco::BasicJet>> top_jets;
    iEvent.getByToken(topJetToken_, top_jets);

    edm::Handle<edm::View<reco::CATopJetTagInfo>> top_jet_infos;
    iEvent.getByToken(topJetInfoToken_, top_jet_infos);

    assert(top_jets->size()==top_jet_infos->size());

    for (unsigned int n_top_jet=0; n_top_jet<top_jets->size(); n_top_jet++) {
        const reco::BasicJet& x = top_jets->at(n_top_jet);
        const reco::CATopJetTagInfo& jet_info = top_jet_infos->at(n_top_jet);
        //assert(_x != NULL);
        //const pat::Jet& x = *_x;
        LogDebug("top jets") << "n__jet=" << n_top_jet << CANDPRINT(x);
        tthtree->jet_toptagger__eta[n_top_jet] = x.eta();
        tthtree->jet_toptagger__pt[n_top_jet] = x.pt();
        tthtree->jet_toptagger__phi[n_top_jet] = x.phi();
        tthtree->jet_toptagger__mass[n_top_jet] = x.mass();
        tthtree->jet_toptagger__energy[n_top_jet] = x.energy();
        tthtree->jet_toptagger__top_mass[n_top_jet] = jet_info.properties().topMass;
        tthtree->jet_toptagger__w_mass[n_top_jet] = jet_info.properties().wMass;
        tthtree->jet_toptagger__min_mass[n_top_jet] = jet_info.properties().minMass;
        tthtree->jet_toptagger__n_sj[n_top_jet] = jet_info.properties().nSubJets;
    }
    tthtree->n__jet_toptagger = top_jets->size();

    if (n__lep>=N_MAX) {
        edm::LogError("N_MAX") << "Exceeded vector N_MAX with n__lep: " << n__lep << ">=> " << N_MAX;
        throw std::exception();
    }

    if (n__jet>=N_MAX) {
        edm::LogError("N_MAX") << "Exceeded vector N_MAX with n__jet: " << n__jet << ">=> " << N_MAX;
        throw std::exception();
    }


    edm::Handle<pat::JetCollection> fatjets;
    iEvent.getByToken(fatjetToken_, fatjets);
    //for (const pat::Jet &j : *fatjets) {
    //}

    edm::Handle<pat::METCollection> mets;
    iEvent.getByToken(metToken_, mets);
    const pat::MET &met = mets->front();
    tthtree->met__pt = met.pt();
    tthtree->met__phi = met.phi();

    if (isMC) {
        tthtree->met__pt__en_up = met.shiftedPt(pat::MET::JetEnUp);
        tthtree->met__pt__en_down = met.shiftedPt(pat::MET::JetEnDown);
        tthtree->gen_met__pt = met.genMET()->pt();
        tthtree->gen_met__phi = met.genMET()->phi();
    }

    //get the LHE gen-level stuff
    //code from LB
    if (isMC) {
        edm::Handle<LHEEventProduct> lhe;
        iEvent.getByToken(lheToken_, lhe);

        const lhef::HEPEUP hepeup_ = lhe->hepeup();
        const std::vector<lhef::HEPEUP::FiveVector> pup_ = hepeup_.PUP; // px, py, pz, E, M

        double lheHT = 0.0;
        unsigned int lheNj = 0;
        unsigned int countBquarks=0, countCquarks=0, countUDSquarks=0, countGquarks=0, countExtraPartons=0;
        for (unsigned int i=0; i<pup_.size(); ++i) {
            int id=hepeup_.IDUP[i]; //pdgId
            int status = hepeup_.ISTUP[i];
            int idabs=TMath::Abs(id);

            // gluons and quarks
            if(status == 1 && ((idabs == 21) || (idabs > 0 && idabs < 7))) {
                // first entry is px, second py
                lheHT += TMath::Sqrt( TMath::Power(hepeup_.PUP[i][0],2) + TMath::Power(hepeup_.PUP[i][1],2) );
                lheNj++;
            }

            if ( hepeup_.ISTUP[i] >= 0 && status == 1 ) {
                if (!(hepeup_.MOTHUP[i].first !=1 && hepeup_.MOTHUP[i].second !=2)) {
                    if(idabs==5  ) countBquarks++;
                    if(idabs==4  ) countCquarks++;
                    if(idabs<=3 && idabs>=1 ) countUDSquarks++;
                    if(idabs==21  ) countGquarks++;
                    if(idabs==21 || (idabs>=1 && idabs<=5)) countExtraPartons++;
                }
            }
        }
        tthtree->lhe__ht = lheHT;
        tthtree->lhe__n_j = lheNj;
        tthtree->lhe__n_b = countBquarks;
        tthtree->lhe__n_c = countCquarks;
        tthtree->lhe__n_l = countUDSquarks;
        tthtree->lhe__n_g = countGquarks;
        tthtree->lhe__n_e = countExtraPartons;
    }

    //These also index the number of generated lepton/jets
    tthtree->n__lep = n__lep;
    tthtree->n__jet = n__jet;

    sw->Stop();
    tthtree->debug__time1r = sw->RealTime();
    tthtree->debug__time1c = sw->CpuTime();
    LogDebug("time") << tthtree->debug__time1r << " " << tthtree->debug__time1c;
    tthtree->tree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void
TTHNtupleAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TTHNtupleAnalyzer::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
/*
void
TTHNtupleAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
TTHNtupleAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
TTHNtupleAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
TTHNtupleAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TTHNtupleAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TTHNtupleAnalyzer);
