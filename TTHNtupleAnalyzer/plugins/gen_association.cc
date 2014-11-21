#include "TTH/TTHNtupleAnalyzer/interface/gen_association.h"

using namespace std;
//recurses over a gen particle and its first daughter and returns the first instance of this
//gen particle which does not have the same ID as its daughter
//W->W->W->mu returns the last W in the chain.

bool has_daughter(const reco::Candidate* p, int id) {
	for (unsigned int i=0; i < p->numberOfDaughters(); i++) {
		if (p->daughter(i)->pdgId() == id) {
			return true;	
		}
	}
	return false;
}

const reco::Candidate* get_daughter_with_abs_id(const reco::Candidate* p, int id) {
	for (unsigned int i=0; i < p->numberOfDaughters(); i++) {
		if (std::abs(p->daughter(i)->pdgId()) == id) {
			return p->daughter(i);
		}
	}
	return 0;
}

const reco::Candidate* get_daughter_with_id(const reco::Candidate* p, int id) {
	for (unsigned int i=0; i < p->numberOfDaughters(); i++) {
		if (p->daughter(i)->pdgId() == id) {
			return p->daughter(i);
		}
	}
	return 0;
}

const reco::Candidate* get_mother_with_id(const reco::Candidate* p, int id) {
	for (unsigned int i=0; i < p->numberOfMothers(); i++) {
		if (p->mother(i)->pdgId() == id) {
			return p->mother(i);
		}
	}
	return 0;
}

const reco::Candidate* find_nonself_child(const reco::Candidate* p, int id=0) {
	if (p==0) {
		return 0;
	}
	if (id==0) {
		id = p->pdgId();
	}
	const reco::Candidate* self_dau = get_daughter_with_id(p, id);
	if (self_dau == 0 || p->status()==3) {
		LogDebug("find_nonself_child") << "nonself found " << id << " " << PCANDPRINT(p);
		return p;
	} else {
		LogDebug("find_nonself_child") << "recursing down " << id << " " << PCANDPRINT(self_dau);
		return find_nonself_child(self_dau, id);
	}
	//if (p->numberOfDaughters()>0 && self_dau != 0) {

	//	if (id != p->daughter(0)->pdgId()) {
	//		LogDebug("find_nonself_child") << "nonself found " << id << " " << p->daughter(0)->pdgId() << PCANDPRINT(p->daughter(0));
	//		return p;
	//	} else {
	//		LogDebug("find_nonself_child") << "recursing down " << id << " " << p->daughter(0)->pdgId();
	//		return find_nonself_child(p->daughter(0), id);
	//	}
	//} else {
	//	return 0;
	//}
		
}

const reco::Candidate* find_first_ancestor(const reco::Candidate* p, int id=0) {
	LogDebug("find_first_ancestor") << p << " " << id;
	if (p==0) {
		return 0;
	}
	if (id==0) {
		id = p->pdgId();
	}

	if (p->numberOfMothers()==0) {
		return p;
	}
	
	const reco::Candidate* self_mother = get_mother_with_id(p, id);
	if (self_mother == 0) {
		LogDebug("find_first_ancestor") << "nonself found " << id << " " << PCANDPRINT(p);
		return p;
	} else {
		LogDebug("find_first_ancestor") << "recursing down " << id << " " << PCANDPRINT(self_mother);
		return find_first_ancestor(self_mother, id);
	}
	
	return 0;
}

//recursively prints out the children of a gen particle
void recursive_genparticle_print(const reco::Candidate* p, unsigned int level=0) {
	for (unsigned int i=0;i<level;i++) {
		cout << ".";
	}
	if (level>10) {
		cout << "|";
		return;
	}
	if (p!=0) {
		cout << PCANDPRINT(p) << " " << p->numberOfDaughters() << " " << level << endl;
		for (unsigned int i=0;i<p->numberOfDaughters();i++)
			recursive_genparticle_print(p->daughter(i), level+1);
	}
	else {
		cout << "p=0" << endl;
	}
}

void fill_top_branches(TTHTree* tthtree, const reco::Candidate* top, const std::string pref, bool assign_daughters=true) {
	
	LogDebug("fill_top_branches") << pref << PCANDPRINT(top);
	
	*(tthtree->get_address<float*>(pref + "__pt")) = top->pt();
	*(tthtree->get_address<float*>(pref + "__eta")) = top->eta();
	*(tthtree->get_address<float*>(pref + "__phi"))= top->phi();
	*(tthtree->get_address<float*>(pref + "__mass")) = top->mass();

	if (!assign_daughters) {
		return;
	}
	if(top->numberOfDaughters()<2) {
		edm::LogError("genparticles") << "top ndau " << pref << " " << top->numberOfDaughters();
		recursive_genparticle_print(top);
	} else {
		//const reco::Candidate* dau1 = top->daughter(0);
		//const reco::Candidate* dau2 = top->daughter(1);
		const reco::Candidate* b = get_daughter_with_abs_id(top, 5);
		const reco::Candidate* w = get_daughter_with_abs_id(top, 24);
		LogDebug("fill_top_branches") << " w " << w << " b " << b;
		
		if (b==0 || w==0) {
			edm::LogError("genparticle") << "top could not assign b " << b << " or w " << w;
			edm::LogWarning("genparticle") << "top daughters " << top->numberOfDaughters();
			for (unsigned int i=0;i < top->numberOfDaughters(); i++) {
				cerr << " dau " << i << top->daughter(i) << " " << top->daughter(i)->pdgId();
			}
			cerr << endl;
			recursive_genparticle_print(top);
		} else {
			LogDebug("fill_top_branches") << " b";
			*(tthtree->get_address<float*>(pref + "__b__pt")) = b->pt();
			*(tthtree->get_address<float*>(pref + "__b__eta")) = b->eta();
			*(tthtree->get_address<float*>(pref + "__b__phi"))= b->phi();
			*(tthtree->get_address<float*>(pref + "__b__mass")) = b->mass();
			
			LogDebug("fill_top_branches") << " w " << w->pdgId();
			const reco::Candidate* w2 = find_nonself_child(w);
			const reco::Candidate* w_dau1 = 0;
			const reco::Candidate* w_dau2 = 0;
			
			if (w2 != 0) {
				w = w2;
				w_dau1 = w->daughter(0);
				w_dau2 = w->daughter(1);
			} else {
				edm::LogError("genparticles") << "could not find w " << w;
				recursive_genparticle_print(w);
			}

			if(w_dau1 != 0) { 
				LogDebug("fill_top_branches") << " w_dau1";
				*(tthtree->get_address<float*>(pref + "__w_d1__pt")) = w_dau1->pt();
				*(tthtree->get_address<float*>(pref + "__w_d1__eta")) = w_dau1->eta();
				*(tthtree->get_address<float*>(pref + "__w_d1__phi")) = w_dau1->phi();
				*(tthtree->get_address<float*>(pref + "__w_d1__mass")) = w_dau1->mass();
				*(tthtree->get_address<int*>(pref + "__w_d1__id")) = w_dau1->pdgId();
				*(tthtree->get_address<int*>(pref + "__w_d1__status")) = w_dau1->status();
				LogDebug("genparticles") << "top w dau1 " << PCANDPRINT(w_dau1); 
			} else {
				edm::LogError("genparticles") << "top w dau1 " << w_dau1 << " null pointer";
				cerr << w->numberOfDaughters() << " ";
				for (unsigned int i=0;i<w->numberOfDaughters();i++)
					cerr << w->daughter(i) << " ";
				cerr << endl;
				recursive_genparticle_print(top);
			} //w_dau1 != 0

			if(w_dau2 != 0) { 
				LogDebug("fill_top_branches") << " w_dau2";
				*(tthtree->get_address<float*>(pref + "__w_d2__pt")) = w_dau2->pt();
				*(tthtree->get_address<float*>(pref + "__w_d2__eta")) = w_dau2->eta();
				*(tthtree->get_address<float*>(pref + "__w_d2__phi")) = w_dau2->phi();
				*(tthtree->get_address<float*>(pref + "__w_d2__mass")) = w_dau2->mass();
				*(tthtree->get_address<int*>(pref + "__w_d2__id")) = w_dau2->pdgId();
				*(tthtree->get_address<int*>(pref + "__w_d2__status")) = w_dau2->status();
				LogDebug("genparticles") << "top w dau2 " << PCANDPRINT(w_dau2); 
			} else {
				edm::LogError("genparticles") << "top w dau2 " << w_dau2 << " null pointer!";
				cerr << w->numberOfDaughters() << " ";
				for (unsigned int i=0;i<w->numberOfDaughters();i++)
					cerr << w->daughter(i) << " ";
				cerr << endl;
				recursive_genparticle_print(top);
			} //w_dau2 != 0
		} //b!=0 && w!=0
	} //dau1!=0  && dau2!=0
} //fill_top_branches

void gen_association(edm::Handle<edm::View<reco::GenParticle>> pruned, TTHTree* tthtree) {
	// Packed particles are all the status 1, so usable to remake jets
	// The navigation from status 1 to pruned is possible (the other direction should be made by hand)
	//Handle<edm::View<pat::PackedGenParticle>> packed;
	//iEvent.getByToken(packedGenToken_, packed);

	//last top quarks of chain
	vector<const reco::GenParticle*> tops_last;
	vector<const reco::GenParticle*> antitops_last;
	
	//first top quarks of chain
	vector<const reco::Candidate*> tops_first;
	vector<const reco::Candidate*> antitops_first;
	
	vector<const reco::GenParticle*> bquarks;
	vector<const reco::GenParticle*> antibquarks;
	
	//find top and antitop
	//check if status=3 (pythia) or if decaying to W
	for (auto& gp : *pruned) {
		//top quarks
		if (gp.pdgId() == 6 && has_daughter(&gp, 24)) {
			tops_last.push_back(&gp);

			//find first of chain
			const reco::Candidate* anc = find_first_ancestor(&gp);
			if (anc!=0) {
				tops_first.push_back(anc);
			}
			LogDebug("genparticles") << "top " << CANDPRINT(gp) << " dau1 " << gp.daughter(0) << " dau2 " << gp.daughter(1);
		}
		else if (gp.pdgId() == -6 && has_daughter(&gp, -24)) {
			
			antitops_last.push_back(&gp);
			const reco::Candidate* anc = find_first_ancestor(&gp);
			if (anc!=0) {
				antitops_first.push_back(anc);
			}
			//find last of chain
			LogDebug("genparticles") << "antitop " << CANDPRINT(gp) << " dau1 " << gp.daughter(0) << " dau2 " << gp.daughter(1);
		}
		
		//b-quarks from Higgs decay
		else if (gp.pdgId() == 5 && gp.status() == 3 && gp.mother(0)!=0 && abs(gp.mother(0)->pdgId()) == 25) {
			bquarks.push_back(&gp);
			LogDebug("genparticles") << "bquark " << CANDPRINT(gp) << " dau1 " << gp.daughter(0) << " dau2 " << gp.daughter(1);
		}
		
		else if (gp.pdgId() == -5 && gp.status() == 3 && gp.mother(0)!=0 && abs(gp.mother(0)->pdgId()) == 25) {
			antibquarks.push_back(&gp);
			LogDebug("genparticles") << "antibquark " << CANDPRINT(gp) << " dau1 " << gp.daughter(0) << " dau2 " << gp.daughter(1);
		}

	} //pruned genparticles
	LogDebug("genparticles")
		<< "gensummary last top " << tops_last.size() << " antitop " << antitops_last.size()
		<< "gensummary first top " << tops_first.size() << " antitop " << antitops_first.size()
		<< " bquark " << bquarks.size() << " antibquarks " << antibquarks.size();

	if (tops_last.size()==1) {
		fill_top_branches(tthtree, tops_last[0], "gen_t");
	}
	if (antitops_last.size()==1) {
		fill_top_branches(tthtree, antitops_last[0], "gen_tbar");
	}
	
	if (tops_first.size()==1) {
		fill_top_branches(tthtree, tops_first[0], "gen_t2", false);
	}
	if (antitops_first.size()==1) {
		fill_top_branches(tthtree, antitops_first[0], "gen_tbar2", false);
	}

	if (bquarks.size()==1 && bquarks[0]!=0) {
		tthtree->gen_b__pt = bquarks[0]->pt(); 
		tthtree->gen_b__eta = bquarks[0]->eta(); 
		tthtree->gen_b__phi = bquarks[0]->phi(); 
		tthtree->gen_b__mass = bquarks[0]->mass(); 
		tthtree->gen_b__status = bquarks[0]->status(); 
		tthtree->gen_b__id = bquarks[0]->pdgId(); 
	}
	if (antibquarks.size()==1 && antibquarks[0]!=0) {
		tthtree->gen_bbar__pt = antibquarks[0]->pt(); 
		tthtree->gen_bbar__eta = antibquarks[0]->eta(); 
		tthtree->gen_bbar__phi = antibquarks[0]->phi(); 
		tthtree->gen_bbar__mass = antibquarks[0]->mass(); 
		tthtree->gen_bbar__status = antibquarks[0]->status(); 
		tthtree->gen_bbar__id = antibquarks[0]->pdgId(); 
	}
} // isMC
