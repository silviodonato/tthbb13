import copy, math

from TTH.MEAnalysis.vhbb_utils import lvec, MET
from TTH.MEAnalysis.Analyzer import FilterAnalyzer
from TTH.MEAnalysis.JetAnalyzer import attach_jet_transfer_function

class GenTTHAnalyzer(FilterAnalyzer):
    """
    Analyzes the ttbar (and Higgs) system on gen level.
    Identifies leptonic and hadronic gen top quarks. 
    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        self.conf = cfg_ana._conf
        super(GenTTHAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)

    def beginLoop(self, setup):
        super(GenTTHAnalyzer, self).beginLoop(setup)

    def pass_jet_selection(self, quark):
        return quark.pt > 30 and abs(quark.eta) < 2.5

    def process(self, event):
        for (syst, event_syst) in event.systResults.items():
            if event_syst.passes_btag:
                res = self._process(event_syst)
                event.systResults[syst] = res
        return True

    def _process(self, event):

        #Get light quarks from W/Z
        event.l_quarks_w = event.GenWZQuark

        #Get b quarks from top
        event.b_quarks_t = event.GenBQuarkFromTop

        #Get b-quarks from H
        event.b_quarks_h = event.GenBQuarkFromH

        #Get leptonic top children
        #note that the tau lepton might be missing
        event.lep_top = event.GenLepFromTop
        event.nu_top = event.GenNuFromTop
        
        #cat_gen - a string specifying the ttbar decay mode
        event.cat_gen = None
        #cat_gen_n - a numerical value corresponding to the string
        event.cat_gen_n = -1

        #all leptonic and hadronic gen tops
        event.genTopLep = []
        event.genTopHad = []


        #Only run top algos
        if len(event.GenTop) == 2:
        
            #Gen tops might be in random order
            gt1 = event.GenTop[0]
            gt2 = event.GenTop[1]
            dm1 = getattr(gt1, "decayMode", -1)
            dm2 = getattr(gt2, "decayMode", -1)
            #Require exactly 1 neutrino (from leptonic top)
            if (len(event.nu_top) == 1 and
                len(event.l_quarks_w) == 2 and
                len(event.b_quarks_t) == 2) or (
                (dm1 == 0 and dm2==1) or (dm2==0 and dm1==1)):
                
                #First top is leptonic
                if dm1 == 0:
                    event.genTopLep = [gt1]
                    event.genTopHad = [gt2]
                #Second top is leptonic
                elif dm2 == 0:
                    event.genTopLep = [gt2]
                    event.genTopHad = [gt1]
                else:
                    #manually check which b quark and hadrons give a hadronic top
                    hadronic_W = lvec(event.l_quarks_w[0]) + lvec(event.l_quarks_w[1])
                    hadronic_top_cands = []
                    #need to check all b quarks, make gen top candidates
                    for ibq, bq in enumerate(event.GenBQuarkFromTop):
                        hadronic_top_cand = hadronic_W + lvec(bq)
                        #Calculate dR, dPt of this top candidate to all gen tops
                        for itop, top in enumerate(event.GenTop):
                            dr = hadronic_top_cand.DeltaR(lvec(top))
                            dpt2 = (hadronic_top_cand.Pt() - top.pt)**2
                            drpt = math.sqrt(dr**2 + dpt2)
                            hadronic_top_cands += [(drpt, ibq, itop)]
                    
                    #Get the gen top candidate which best matches a real gen top
                    hadronic_top_cands = sorted(hadronic_top_cands, key=lambda x: x[0])
                    best_cand = hadronic_top_cands[0]

                    dr, ibq, itop = best_cand
                    event.genTopHad = [event.GenTop[itop]]
                    event.genTopLep = [event.GenTop[0 if itop==1 else 1]]
                        
                event.cat_gen = "sl"
                event.cat_gen_n = 0
            elif (len(event.nu_top) == 2 and
                len(event.l_quarks_w) == 0 and
                len(event.b_quarks_t) == 2) or (
                (dm1 == 0 and dm2 == 0)):
                event.cat_gen = "dl"
                event.cat_gen_n = 1
                event.genTopLep = [gt1, gt2]
                event.genTopHad = []
            elif (len(event.lep_top) == 0 and
                len(event.nu_top) == 0 and
                len(event.l_quarks_w) == 4 and
                len(event.b_quarks_t) == 2) or (
                (dm1 == 1 and dm2 == 1)):
                event.cat_gen = "fh"
                event.cat_gen_n = 2
                event.genTopHad = [gt1, gt2]
                event.genTopLep = []
            else:
                event.genTopLep = []
                event.genTopHad = []

        event.l_quarks_gen = []
        event.b_quarks_gen = []

        nq = 0
        #Find the light quarks from W that would pass jet selection
        #associate them with a transfer function
        for q in event.l_quarks_w:
            nq += 1
            if self.pass_jet_selection(q):
                q.btagFlag = 0.0
                q.tth_match_label = "wq"
                q.tth_match_index = nq
                attach_jet_transfer_function(q, self.conf)
                event.l_quarks_gen += [q]

        #Find the b quarks from top that would pass jet selection
        #associate them with a transfer function
        for q in event.b_quarks_t:
            nq += 1
            if self.pass_jet_selection(q):
                q.btagFlag = 1.0
                q.tth_match_label = "tb"
                q.tth_match_index = nq
                attach_jet_transfer_function(q, self.conf)
                event.b_quarks_gen += [q]

        #Find the b quarks from Higgs that would pass jet selection
        #associate them with a transfer function
        for q in event.b_quarks_h:
            nq += 1
            if self.pass_jet_selection(q):
                q.btagFlag = 1.0
                q.tth_match_label = "hb"
                q.tth_match_index = nq
                attach_jet_transfer_function(q, self.conf)
                event.b_quarks_gen += [q]

        #Get the total MET from the neutrinos
        spx = 0
        spy = 0
        for nu in event.nu_top:
            p4 = lvec(nu)
            spx += p4.Px()
            spy += p4.Py()
        event.MET_tt = MET(px=spx, py=spy)

        #Get the total ttH visible pt at gen level
        spx = 0
        spy = 0
        for p in (event.l_quarks_w + event.b_quarks_t +
            event.b_quarks_h + event.lep_top):
            p4 = lvec(p)
            spx += p4.Px()
            spy += p4.Py()
        event.tth_px_gen = spx
        event.tth_py_gen = spy

        #Calculate tth recoil
        #rho = -met - tth_matched
        event.tth_rho_px_gen = -event.MET_gen.px - event.tth_px_gen
        event.tth_rho_py_gen = -event.MET_gen.py - event.tth_py_gen

        if "gen" in self.conf.general["verbosity"]:
            for j in event.l_quarks_w:
                print "gen q(W)", j.pt, j.eta, j.phi, j.mass, j.pdgId
            for j in event.b_quarks_t:
                print "gen b(t)", j.pt, j.eta, j.phi, j.mass, j.pdgId
            for j in event.lep_top:
                print "gen l(t)", j.pt, j.eta, j.phi, j.mass, j.pdgId
            for j in event.nu_top:
                print "gen n(t)", j.pt, j.eta, j.phi, j.mass, j.pdgId
            for j in event.b_quarks_h:
                print "gen b(h)", j.pt, j.eta, j.phi, j.mass, j.pdgId
            print "gen cat", event.cat_gen, event.cat_gen_n

        #Store for each jet, specified by it's index in the jet
        #vector, if it is matched to any gen-level quarks
        matched_pairs = {}

        def match_jets_to_quarks(jetcoll, quarkcoll, label, label_numeric):
            for ij, j in enumerate(jetcoll):
                for iq, q in enumerate(quarkcoll):

                    #find DeltaR between jet and quark
                    l1 = lvec(q)
                    l2 = lvec(j)
                    dr = l1.DeltaR(l2)
                    if dr < 0.3:
                        #Jet already had a match: take the one with smaller dR
                        if matched_pairs.has_key(ij):
                            if matched_pairs[ij][1] > dr:
                                matched_pairs[ij] = (label, iq, dr, label_numeric)
                        else:
                            matched_pairs[ij] = (label, iq, dr, label_numeric)

        #Find the best possible match for each individual jet
        match_jets_to_quarks(event.good_jets, event.l_quarks_w, "wq", 0)
        match_jets_to_quarks(event.good_jets, event.b_quarks_t, "tb", 1)
        match_jets_to_quarks(event.good_jets, event.b_quarks_h, "hb", 2)

        #Number of reco jets matched to quarks from W, top, higgs
        event.nMatch_wq = 0
        event.nMatch_tb = 0
        event.nMatch_hb = 0
        #As above, but also required to be tagged/untagged for b/light respectively.
        event.nMatch_wq_btag = 0
        event.nMatch_tb_btag = 0
        event.nMatch_hb_btag = 0
        
        if "debug" in self.conf.general["verbosity"]:
            print "nMatch {0}_{1}_{2} nMatch_btag {3}_{4}_{5}".format(
                event.nMatch_wq,
                event.nMatch_tb,
                event.nMatch_hb,
                event.nMatch_wq_btag,
                event.nMatch_tb_btag,
                event.nMatch_hb_btag,
            )
        
        #Now check what each jet was matched to
        for ij, jet in enumerate(event.good_jets):

            jet.tth_match_label = None
            jet.tth_match_index = -1
            jet.tth_match_dr = -1
            jet.tth_match_label_numeric = -1

            #Jet did not have a match (no jet index in matched_pairs)
            if not matched_pairs.has_key(ij):
                continue #continue jet loop

            #mlabel - string label of quark collection, e.g. "wq"
            #midx - index of quark in vector that the jet was matched to
            #mdr - delta R between jet and matched quark
            #mlabel_num - numeric label of quark collection, e.g. 0
            mlabel, midx, mdr, mlabel_num = matched_pairs[ij]

            jet.tth_match_label = mlabel
            jet.tth_match_index = midx
            jet.tth_match_dr = mdr
            jet.tth_match_label_numeric = mlabel_num

            if mlabel == "wq":
                event.nMatch_wq += 1

                #If this jet is considered to be un-tagged
                if jet.btagFlag == 0.0:
                    event.nMatch_wq_btag += 1
            elif mlabel == "tb":
                event.nMatch_tb += 1

                #If this jet is considered to be b-tagged
                if jet.btagFlag == 1.0:
                    event.nMatch_tb_btag += 1

            elif mlabel == "hb":
                event.nMatch_hb += 1
                if jet.btagFlag == 1.0:
                    event.nMatch_hb_btag += 1

        if "matching" in self.conf.general["verbosity"]:
            matches = {"wq":event.l_quarks_w, "tb": event.b_quarks_t, "hb":event.b_quarks_h}

            for ij, jet in enumerate(event.good_jets):
                if not matched_pairs.has_key(ij):
                    continue
                mlabel, midx, mdr, mlabel_num = matched_pairs[ij]
                print "jet match", ij, mlabel, midx, mdr, jet.pt, matches[mlabel][midx].pt

        #reco-level tth-matched system
        spx = 0.0
        spy = 0.0
        for jet in event.good_jets:
            if not (jet.tth_match_label is None):
                p4 = lvec(jet)
                spx += p4.Px()
                spy += p4.Py()
        for lep in event.good_leptons:
            p4 = lvec(lep)
            match = False
            for glep in event.lep_top:
                p4g = lvec(glep)
                if p4g.DeltaR(p4) < 0.3:
                    match = True
                    break
            if match:
                spx += p4.Px()
                spy += p4.Py()

        event.tth_px_reco = spx
        event.tth_py_reco = spy

        #Calculate tth recoil
        #rho = -met - tth_matched
        event.tth_rho_px_reco = -event.MET.px - event.tth_px_reco
        event.tth_rho_py_reco = -event.MET.py - event.tth_py_reco

        #print out gen-level quarks
        if "input" in self.conf.general["verbosity"]:
            print "gen Q"
            for q in event.l_quarks_gen:
                print q.pt, q.eta, q.phi, q.mass, q.pdgId
            print "gen B"
            for q in event.b_quarks_gen:
                print q.pt, q.eta, q.phi, q.mass, q.pdgId

        return event
