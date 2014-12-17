""" CrabHelpers:
Collection of functions for simple crab3 submission.
"""

#######################################
# Imports
#######################################

import subprocess
import imp
import glob
import re
import os

from TTH.TTHNtupleAnalyzer.Samples import Samples


#######################################
# submit
#######################################

def submit(name,
           sample_shortname,
           version,
           cmssw_config_path,
           cmssw_config_script = "Main_cfg.py",
           site = "T2_CH_CSCS",
           template_filename = "c_TEMPLATE.py",
           cfg_filename = "c_tmp.py",
           blacklist = []):
    """Submit a single job to the Grid"""

    # Import template, add parameters and save to new file
    imp.load_source("template", template_filename)
    import template

    template.config.General.workArea = "crab_{0}_{1}_{2}".format(name, version, sample_shortname)
    template.config.General.requestName = "{0}_{1}_{2}".format(name, version, sample_shortname)
    template.config.JobType.psetName = cmssw_config_path + cmssw_config_script
    template.config.Data.inputDataset = Samples[sample_shortname]
    template.config.Data.unitsPerJob = 90
    template.config.Site.storageSite = site

    if blacklist:
        template.config.Site.blacklist = blacklist


    outfile = open(cfg_filename, "w")
    outfile.write(str(template.config))
    outfile.close()

    print "Created config for", sample_shortname
    print "Now calling crab submit"

    subprocess.call(["crab", "submit", "-c", "c_tmp.py"])
# End of submit


#######################################
# status
#######################################

import json
def status(name,
           sample_shortname,
           version,
           parse=False):
    """Get status of a single job on the Grid."""

    working_dir = "crab_{0}_{1}_{2}/crab_{0}_{1}_{2}".format(name, version, sample_shortname)

    if not parse:
        subprocess.call(["crab", "status", "-d", working_dir], stdout=of)
    else:
        of = open("crab.stdout", "w")
        subprocess.call(["crab", "status", "-d", working_dir, "--json"], stdout=of)
        of.close()
        of = open("crab.stdout", "r")
        lines = of.readlines()
        of.close()
        jsonlines = reduce(
            lambda x,y: dict(x.items() + y.items()),
            map(lambda x: eval(x.strip()), filter(lambda x: x.startswith("{"), lines)),
            {}
        )
        return jsonlines
# End of status


#######################################
# download
#######################################

def download(name,
             sample_shortname,
             version,
             target_basepath):
    """Download a single job from the Grid. Assume we are in the same
    directory used for submission (crab_configs)
    and the crab working directory is of the form
    crab_ntop_v3_zprime_m1000_1p_13tev/crab_ntop_v3_zprime_m1000_1p_13tev

    Download to target_basepath + job name
    """

    working_dir = "crab_{0}_{1}_{2}/crab_{0}_{1}_{2}".format(name, version, sample_shortname)

    output_dir = target_basepath + "{0}_{1}_{2}".format(name, version, sample_shortname)
    subprocess.call(["crab", "getoutput", "-d", working_dir, "--outputpath", output_dir])
# End of download


#######################################
# get LFN
#######################################

def get_lfn(name, sample_shortname, version, file_output=True):
    working_dir = "crab_{0}_{1}_{2}/crab_{0}_{1}_{2}".format(name, version, sample_shortname)
    of = open("crab.stdout", "w")
    ret = subprocess.call(["crab", "getoutput", "-d", working_dir, "--dump"], stdout=of)
    of.close()
    if not ret==0:
        print "ERROR: could not get output"
        print "".join(open("crab.stdout", "r").readlines())
    of = open("crab.stdout", "r")
    lines = "".join(of.readlines())
    lines = lines.split("===")
    lfns = {}
    for line in lines:
        m = re.match(".*job ([0-9]+)\n.*\nLFN: (/.*root)\n", line)
        if m:
            lfns[int(m.group(1))] = m.group(2)
    return lfns
# End of get LFN
#######################################
# hadd
#######################################

def hadd(name,
         sample_shortname,
         version,
         basepath = ""):
    """ Hadd all root files in basepath+jobname to basepath/jobname.root
    """

    input_dir = basepath + "{0}_{1}_{2}/*".format(name, version, sample_shortname)
    input_filenames = glob.glob(input_dir)

    output_filename = basepath + "{0}_{1}_{2}.root".format(name, version, sample_shortname)

    subprocess.call(["hadd", "-f", output_filename] + input_filenames)

def hadd_from_file(name,
         sample_shortname,
         version,
         basepath = ""):
    """ Hadd all root files in basepath+jobname to basepath/jobname.root
    """

    input_fn = "crab_{0}_{1}_{2}/crab_{0}_{1}_{2}/files.txt".format(name, version, sample_shortname)
    if os.path.isfile(input_fn):
        input_filenames = map(lambda x: x.strip(), open(input_fn).readlines())
        if len(input_filenames)>0:
            output_filename = basepath + "/{0}_{1}_{2}.root".format(name, version, sample_shortname)
            subprocess.call(["echo", "hadd", "-f", output_filename, "-n", "500"] + input_filenames)
            return
    print "no output from {0}".format(sample_shortname)
# End of hadd
