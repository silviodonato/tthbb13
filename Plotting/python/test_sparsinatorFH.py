import subprocess
import copy, os
import unittest
import logging
import ROOT

def run_sparsinator(infiles, datasetpath, maxev):
    print "running on files", infiles
    env = copy.copy(os.environ)
    CMSSW_BASE = os.environ["CMSSW_BASE"]
    env["FILE_NAMES"] = " ".join(infiles)
    env["DATASETPATH"] = datasetpath
    env["MAX_EVENTS"] = str(maxev)
    ret = subprocess.Popen([
        "python", "Plotting/python/joosep/sparsinator.py",
    ], env=env).communicate()
    return

def read_inputs(dataset):
    fi = open(dataset)
    lines = [x.split()[0].strip() for x in fi.readlines() if ".root" in x]
    return sorted(lines)

class MakeSparsinatorTestCase(unittest.TestCase):

    def sparsinator_checks(self, fn, sample):
        self.assertTrue(os.path.isfile(fn))
        fi = ROOT.TFile(fn)
        hi = fi.Get("{0}/fh/sparse".format(sample))
        self.assertFalse(hi == None)
        fi.Close()

    def test_sparsinator_data(self):
        run_sparsinator(read_inputs("MEAnalysis/gc/datasets/had_V24_1/BTagCSV.txt")[:4], "BTagCSV", 50)
        self.sparsinator_checks("out.root", "BTagCSV") 
    
    def test_sparsinator_mc(self):
        run_sparsinator(
            read_inputs("MEAnalysis/gc/datasets/had_V24_1/ttHTobb_M125_13TeV_powheg_pythia8.txt")[:1],
            "had_V24_1__ttHTobb_M125_13TeV_powheg_pythia8",
            50
        )
        self.sparsinator_checks("out.root", "ttHTobb_M125_13TeV_powheg_pythia8") 
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
