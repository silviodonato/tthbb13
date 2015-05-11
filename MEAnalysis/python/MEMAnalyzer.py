from TTH.MEAnalysis.VHbbTree import lvec
import ROOT
#Load the MEM integrator libraries
# ROOT.gSystem.Load("libFWCoreFWLite")
# ROOT.gROOT.ProcessLine('AutoLibraryLoader::enable();')
# ROOT.gSystem.Load("libFWCoreFWLite")
ROOT.gSystem.Load("libCintex")
ROOT.gROOT.ProcessLine('ROOT::Cintex::Cintex::Enable();')
ROOT.gSystem.Load("libTTHMEIntegratorStandalone")

from ROOT import MEM

#Pre-define shorthands for permutation and integration variable vectors
CvectorPermutations = getattr(ROOT, "std::vector<MEM::Permutations::Permutations>")
CvectorPSVar = getattr(ROOT, "std::vector<MEM::PSVar::PSVar>")

from TTH.MEAnalysis.Analyzer import FilterAnalyzer
class MECategoryAnalyzer(FilterAnalyzer):
    """
    Performs ME categorization
    FIXME: doc
    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        self.conf = cfg_ana._conf
        super(MECategoryAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
        self.cat_map = {"NOCAT":-1, "cat1": 1, "cat2": 2, "cat3": 3, "cat6":6}
        self.btag_cat_map = {"NOCAT":-1, "L": 0, "H": 1}

    def beginLoop(self, setup):
        super(MECategoryAnalyzer, self).beginLoop(setup)

        for c in ["NOCAT", "cat1", "cat2", "cat3", "cat6"]:
            self.counters["processing"].register(c)

    def process(self, event):
        self.counters["processing"].inc("processed")

        cat = "NOCAT"
        pass_btag_lr = (self.conf.jets["untaggedSelection"] == "btagLR" and
            event.btag_LR_4b_2b > self.conf.mem["btagLRCut"][event.cat]
        )
        pass_btag_csv = (self.conf.jets["untaggedSelection"] == "btagCSV" and
            len(event.btagged_jets) >= 4
        )
        cat_btag = "NOCAT"

        if pass_btag_lr or pass_btag_csv:
            cat_btag = "H"

        if event.is_sl:

            #at least 6 jets, if 6, Wtag in [60,100], if more Wtag in [72,94]
            if ((len(event.good_jets) == 6 and event.Wmass >= 60 and event.Wmass < 100) or
               (len(event.good_jets) > 6 and event.Wmass >= 72 and event.Wmass < 94)):
               cat = "cat1"
               #W-tagger fills wquark_candidate_jets
            #at least 6 jets, no W-tag
            elif len(event.good_jets) >= 6:
                cat = "cat2"
            #one W daughter missing
            elif len(event.good_jets) == 5:
                event.wquark_candidate_jets = event.buntagged_jets
                cat = "cat3"
        elif event.is_dl and len(event.good_jets)>=4:
            event.wquark_candidate_jets = []
            cat = "cat6"

        self.counters["processing"].inc(cat)
        event.cat = cat
        event.cat_btag = cat_btag
        event.catn = self.cat_map.get(cat, -1)
        event.cat_btag_n = self.btag_cat_map.get(cat_btag, -1)

        passes = True
        if passes:
            self.counters["processing"].inc("passes")
        return passes

class MEAnalyzer(FilterAnalyzer):
    """
    Performs ME calculation using the external integrator.
    It supports multiple MEM algorithms at the same time, configured via the
    self.configs dictionary. The outputs are stored in a vector in the event.

    The ME algorithms are run only in case the njet/nlep/Wtag category (event.cat)
    is in the accepted categories specified in the config.
    Additionally, we require the b-tagging category (event.cat_btag) to be "H" (high).

    For each ME configuration on each event, the jets which are counted to be b-tagged
    in event.btagged_jets are added as the candidates for t->b (W) or h->bb.
    These jets must be exactly 4, otherwise no permutation is accepted (in case
    using BTagged/QUntagged assumptions).

    Any additional jets are assumed to come from the hadronic W decay. These are
    specified in event.wquark_candidate_jets.

    Based on the event njet/nlep/Wtag category, if a jet fmor the W is counted as missing,
    it is integrated over using additional variables set by self.vars_to_integrate.

    The MEM top pair hypothesis (di-leptonic or single leptonic top pair) is chosen based
    on the reconstructed lepton multiplicity (event.good_leptons).

    The algorithm is shortly as follows:
    1. check if event passes event.cat and event.cat_btag
    2. loop over all MEM configurations i=[0...Nmem)
        2a. add all 4 b-tagged jets to integrator
        2b. add all 0-3 untagged jets to integrator
        2c. add all leptons to integrator
        2d. decide SL/DL top pair hypo based on leptons
        2e. based on event.cat, add additional integration vars
        2f. run ME integrator for both tth and ttbb hypos
        2g. save output in event.mem_output_tth[i] (or ttbb)
        2i. clean up event in integrator

    Relies on:
    event.good_jets, event.good_leptons, event.cat, event.input.met_pt

    Produces:
    mem_results_tth (MEMOutput): probability for the tt+H(bb) hypothesis
    mem_results_ttbb (MEMOutput): probability for the tt+bb hypothesis

    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        self.conf = cfg_ana._conf
        super(MEAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)

        self.configs = {
            "SL_2qW": MEM.MEMConfig(),
            "SL_2qW_gen": MEM.MEMConfig(),
            "SL_1qW": MEM.MEMConfig(),
            "SL_1qW_gen": MEM.MEMConfig(),
            "DL": MEM.MEMConfig(),
            "DL_gen": MEM.MEMConfig(),
#            "NumPointsDouble": MEM.MEMConfig(),
#            "NumPointsHalf": MEM.MEMConfig(),
#            "NoJacobian": MEM.MEMConfig(),
#            "NoDecayAmpl": MEM.MEMConfig(),
#            "NoPDF": MEM.MEMConfig(),
#            "NoScattAmpl": MEM.MEMConfig(),
#            "QuarkEnergy98": MEM.MEMConfig(),
#            "QuarkEnergy10": MEM.MEMConfig(),
#            "NuPhiRestriction": MEM.MEMConfig(),
#            "JetsPtOrder": MEM.MEMConfig(),
#            "JetsPtOrderIntegrationRange": MEM.MEMConfig(),
#            "Recoil": MEM.MEMConfig(),
#            "Sudakov": MEM.MEMConfig(),
#            "Minimize": MEM.MEMConfig(),
        }

        #These MEM configurations will actually be considered for calculation
        self.memkeys = self.conf.mem["methodsToRun"]

        self.configs["SL_2qW"].defaultCfg()
        self.configs["SL_2qW_gen"].defaultCfg()
        self.configs["SL_1qW"].defaultCfg()
        self.configs["SL_1qW_gen"].defaultCfg()
        self.configs["DL"].defaultCfg()
        self.configs["DL_gen"].defaultCfg()
        #self.configs["gen"].defaultCfg()
        #self.configs["genMissedWQ"].defaultCfg()
        #self.configs["newTF"].defaultCfg()
        #self.configs["MissedWQ"].defaultCfg()
        #self.configs["MissedWQOldTF"].defaultCfg()
        #self.configs["NumPointsDouble"].defaultCfg(2.0)
        #self.configs["NumPointsHalf"].defaultCfg(0.5)
        #self.configs["NoJacobian"].defaultCfg()
        #self.configs["NoDecayAmpl"].defaultCfg()
        #self.configs["NoPDF"].defaultCfg()
        #self.configs["NoScattAmpl"].defaultCfg()
        #self.configs["QuarkEnergy98"].defaultCfg()
        #self.configs["QuarkEnergy10"].defaultCfg()
        #self.configs["NuPhiRestriction"].defaultCfg()
        #self.configs["JetsPtOrder"].defaultCfg()
        #self.configs["JetsPtOrderIntegrationRange"].defaultCfg()
        #self.configs["Recoil"].defaultCfg()
        #self.configs["Sudakov"].defaultCfg()
        #self.configs["Minimize"].defaultCfg()

        for (k, v) in self.configs.items():
            v.b_quark_candidates = lambda event: event.btagged_jets
            v.l_quark_candidates = lambda event: event.wquark_candidate_jets
            v.lepton_candidates = lambda event: event.good_leptons
            v.transfer_function_method = MEM.TFMethod.Builtin

            v.mem_assumptions = set([])
            v.enabled = True

            for nb in [0, 1]:
                for fl1, fl2 in [('b', MEM.TFType.bLost), ('l', MEM.TFType.qLost)]:
                    tf = self.conf.tf_matrix[fl1][nb].Make_CDF()

                    #set pt cut for efficiency function
                    tf.SetParameter(0, self.conf.jets["pt"])
                    v.set_tf_global(fl2, nb, tf)

        #self.configs["newTF"].transfer_function_method = MEM.TFMethod.External

        for k in ["SL_2qW_gen", "SL_1qW_gen"]:
            self.configs[k].b_quark_candidates = lambda event: event.b_quarks_gen
            self.configs[k].l_quark_candidates = lambda event: event.l_quarks_gen
            self.configs[k].lepton_candidates = lambda event: event.good_leptons

        for x in ["SL_2qW"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 1 and
                len(c.b_quark_candidates(y)) >= 4 and
                len(c.l_quark_candidates(y)) >= 2 and
                y.cat_btag == "H"
            )
        for x in ["SL_2qW_gen"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 1 and
                len(c.b_quark_candidates(y)) >= 4 and
                len(c.l_quark_candidates(y)) >= 2
            )
        for x in ["SL_1qW"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 1 and
                len(c.b_quark_candidates(y)) >= 4 and
                len(c.l_quark_candidates(y)) >= 1 and
                y.cat_btag == "H"
            )
            self.configs[x].mem_assumptions.add("missed_wq")
        for x in ["SL_1qW_gen"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 1 and
                len(c.b_quark_candidates(y)) >= 4 and
                len(c.l_quark_candidates(y)) >= 1
            )
            self.configs[x].mem_assumptions.add("missed_wq")
        for x in ["DL"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 2 and
                len(c.b_quark_candidates(y)) >= 4 and
                y.cat_btag == "H"
            )
            self.configs[x].mem_assumptions.add("dl")
        for x in ["DL_gen"]:
            self.configs[x].do_calculate = lambda y, c: (
                len(y.good_leptons) == 2 and
                len(c.b_quark_candidates(y)) >= 4
            )
            self.configs[x].mem_assumptions.add("dl")

        for k in ["SL_2qW", "SL_1qW", "SL_2qW_gen", "SL_1qW_gen"]:
            self.configs[k].mem_assumptions.add("sl")

        #self.configs["NoJacobian"].int_code &= ~ MEM.IntegrandType.Jacobian
        #self.configs["NoDecayAmpl"].int_code &= ~ MEM.IntegrandType.DecayAmpl
        #self.configs["NoPDF"].int_code &= ~ MEM.IntegrandType.PDF
        #self.configs["NoScattAmpl"].int_code &=  ~ MEM.IntegrandType.ScattAmpl
        #self.configs["QuarkEnergy98"].j_range_CL = 0.98
        #self.configs["QuarkEnergy98"].b_range_CL = 0.98
        #self.configs["QuarkEnergy10"].j_range_CL = 0.10
        #self.configs["QuarkEnergy10"].b_range_CL = 0.10
        #self.configs["NuPhiRestriction"].m_range_CL = 99
        #self.configs["JetsPtOrder"].highpt_first  = 0
        #self.configs["JetsPtOrderIntegrationRange"].highpt_first  = 0
        #self.configs["JetsPtOrderIntegrationRange"].j_range_CL = 0.99
        #self.configs["JetsPtOrderIntegrationRange"].b_range_CL = 0.99
        #self.configs["Recoil"].int_code |= MEM.IntegrandType.Recoil
        #self.configs["Sudakov"].int_code |= MEM.IntegrandType.Sudakov
        #self.configs["Minimize"].do_minimize = 1
        #self.configs["Minimize"].int_code = 0

        #only in 6J SL
        #self.configs["Sudakov"].do_calculate = (
        #    lambda x: len(x.good_jets) == 6 and
        #    len(x.good_leptons) == 1
        #)

        #Create the ME integrator.
        #Arguments specify the verbosity
        self.integrator = MEM.Integrand(
            #0,
            MEM.output,
            self.configs["SL_2qW"]
        )

        #Create an emtpy std::vector<MEM::Permutations::Permutations>
        self.permutations = CvectorPermutations()

        #Assume that only jets passing CSV>0.5 are b quarks
        self.permutations.push_back(MEM.Permutations.BTagged)

        #Assume that only jets passing CSV<0.5 are l quarks
        self.permutations.push_back(MEM.Permutations.QUntagged)

        self.integrator.set_permutation_strategy(self.permutations)

        #Pieces of ME to calculate
        # self.integrator.set_integrand(
        #     MEM.IntegrandType.Constant
        #     |MEM.IntegrandType.ScattAmpl
        #     |MEM.IntegrandType.DecayAmpl
        #     |MEM.IntegrandType.Jacobian
        #     |MEM.IntegrandType.PDF
        #     |MEM.IntegrandType.Transfer
        # )
        #self.integrator.set_sqrts(13000.);

        #Create an empty vector for the integration variables
        self.vars_to_integrate = CvectorPSVar()

    def add_obj(self, objtype, **kwargs):
        """
        Add an event object (jet, lepton, MET) to the ME integrator.

        objtype: specifies the object type
        kwargs: p4s: spherical 4-momentum (pt, eta, phi, M) as a tuple
                obsdict: dict of additional observables to pass to MEM
                tf_dict: Dictionary of MEM.TFType->TF1 of transfer functions
        """
        if kwargs.has_key("p4s"):
            pt, eta, phi, mass = kwargs.pop("p4s")
            v = ROOT.TLorentzVector()
            v.SetPtEtaPhiM(pt, eta, phi, mass);
        elif kwargs.has_key("p4c"):
            v = ROOT.TLorentzVector(*kwargs.pop("p4c"))
        obs_dict = kwargs.pop("obs_dict", {})
        tf_dict = kwargs.pop("tf_dict", {})

        o = MEM.Object(v, objtype)

        #Add observables from observable dictionary
        for k, v in obs_dict.items():
            o.addObs(k, v)
        for k, v in tf_dict.items():
            o.addTransferFunction(k, v)
        self.integrator.push_back_object(o)

    def beginLoop(self, setup):
        super(MEAnalyzer, self).beginLoop(setup)

    def configure_mem(self, event, mem_cfg):
        self.integrator.set_cfg(mem_cfg)
        self.vars_to_integrate.clear()
        self.integrator.next_event()
        mem_cfg.enabled = True

        #One quark from W missed, integrate over its direction if possible
        if "missed_wq" in mem_cfg.mem_assumptions:
            self.vars_to_integrate.push_back(MEM.PSVar.cos_qbar1)
            self.vars_to_integrate.push_back(MEM.PSVar.phi_qbar1)
        #Add heavy flavour jets that are assumed to come from top/higgs decay
        for jet in mem_cfg.b_quark_candidates(event):
            self.add_obj(
                MEM.ObjectType.Jet,
                p4s=(jet.pt, jet.eta, jet.phi, jet.mass),
                obs_dict={MEM.Observable.BTAG: jet.btagFlag},
                tf_dict={
                    MEM.TFType.bReco: jet.tf_b, MEM.TFType.qReco: jet.tf_l,
                }
            )
            if "meminput" in self.conf.general["verbosity"]:
                print "bq", jet.pt, jet.eta, jet.phi, jet.mass, jet.btagFlag

        #Add light jets that are assumed to come from hadronic W decay
        for jet in mem_cfg.l_quark_candidates(event):
            self.add_obj(
                MEM.ObjectType.Jet,
                p4s=(jet.pt, jet.eta, jet.phi, jet.mass),
                obs_dict={MEM.Observable.BTAG: jet.btagFlag},
                tf_dict={
                    MEM.TFType.bReco: jet.tf_b, MEM.TFType.qReco: jet.tf_l,
                }
            )
            if "meminput" in self.conf.general["verbosity"]:
                print "lq", jet.pt, jet.eta, jet.phi, jet.mass, jet.btagFlag
        for lep in mem_cfg.lepton_candidates(event):
            self.add_obj(
                MEM.ObjectType.Lepton,
                p4s=(lep.pt, lep.eta, lep.phi, lep.mass),
                obs_dict={MEM.Observable.CHARGE: lep.charge},
            )
            if "meminput" in self.conf.general["verbosity"]:
                print "lp", lep.pt, lep.eta, lep.phi, lep.mass, lep.charge
        self.add_obj(
            MEM.ObjectType.MET,
            #MET is caused by massless object
            p4s=(event.input.met_pt, 0, event.input.met_phi, 0),
        )

    #Check if event.nMatch_label >= conf.mem[cat][label]
    def require(self, required_match, label, event):
        nreq = required_match.get(label, None)
        if nreq is None:
            return True

        nmatched = getattr(event, "nMatch_"+label)

        #In case event did not contain b form higgs (e.g. ttbb)
        if "hb" in label and len(event.GenBQuarkFromH) < nreq:
            return True

        passes = (nmatched >= nreq)
        return passes

    def process(self, event):
        self.counters["processing"].inc("processed")

        #Clean up any old MEM state
        self.vars_to_integrate.clear()
        self.integrator.next_event()

        #Initialize members for tree filler
        event.mem_results_tth = []
        event.mem_results_ttbb = []

        #jets = sorted(event.good_jets, key=lambda x: x.pt, reverse=True)
        leptons = event.good_leptons
        met_pt = event.input.met_pt
        met_phi = event.input.met_phi

        if "reco" in self.conf.general["verbosity"]:
            for j in jets:
                print "jet", j.pt, j.eta, j.phi, j.mass, j.btagCSV, j.btagFlag, j.mcFlavour
            for l in leptons:
                print "lep", l.pt, l.eta, l.phi, l.mass, l.charge



        #Here we optionally restrict the ME calculation to only matched events
        #Get the conf dict specifying which matches we require
        required_match = self.conf.mem.get("requireMatched", {}).get(event.cat, {})

        #Calculate all the match booleans
        #match label -> matched boolean
        passd = {
            p: self.require(required_match, p, event) for p in
            ["wq", "wq_btag", "tb", "tb_btag", "hb", "hb_btag"]
        }

        #Fail if any fails
        for k, v in passd.items():
            if not v:
                #print "Failed to match", k
                return True

        res = {}
        print event.cat, event.cat_btag, len(event.good_jets), event.nBCSVM, event.n_mu_tight, event.n_el_tight
        for hypo in [MEM.Hypothesis.TTH, MEM.Hypothesis.TTBB]:
            skipped = []
            for confname in self.memkeys:
                mem_cfg = self.configs[confname]

                fstate = MEM.FinalState.TTH
                if "dl" in mem_cfg.mem_assumptions:
                    fstate = MEM.FinalState.LL
                elif "sl" in mem_cfg.mem_assumptions:
                    fstate = MEM.FinalState.LH
                print "MEM", ("hypo", hypo), ("conf", confname), fstate, len(mem_cfg.b_quark_candidates(event)), len(mem_cfg.l_quark_candidates(event))
                #Run MEM if we did not explicitly disable it
                if (self.conf.mem["calcME"] and
                        mem_cfg.do_calculate(event, mem_cfg) and mem_cfg.enabled
                    ):
                    print "MEM", confname, "started"

                    self.configure_mem(event, mem_cfg)
                    r = self.integrator.run(
                        fstate,
                        hypo,
                        self.vars_to_integrate
                    )
                    print "MEM done", ("hypo", hypo), ("conf", confname)

                    res[(hypo, confname)] = r
                else:
                    skipped += [confname]
                    r = MEM.MEMOutput()
                    res[(hypo, confname)] = r
            print "skipped confs", skipped
        if "default" in self.memkeys:
            p1 = res[(MEM.Hypothesis.TTH, "default")].p
            p2 = res[(MEM.Hypothesis.TTBB, "default")].p

            #In case of an erroneous calculation, print a message
            if self.conf.mem["calcME"] and (p1<=0 or p2<=0 or (p1 / (p1+0.02*p2))<0.0001):
                print "MEM BADPROB", p1, p2

        #print out full MEM result dictionary
        #print "RES", [(k, res[k].p) for k in sorted(res.keys())]

        event.mem_results_tth = [res[(MEM.Hypothesis.TTH, k)] for k in self.memkeys]
        event.mem_results_ttbb = [res[(MEM.Hypothesis.TTBB, k)] for k in self.memkeys]
