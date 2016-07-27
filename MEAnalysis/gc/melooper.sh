#!/bin/bash

#export DATASETPATH=ttHTobb_M125_13TeV_powheg_pythia8_dsalerno-VHBBHeppyV21_tthbbV9_v3_3
#export FILE_NAMES=/store/user/dsalerno/tth/VHBBHeppyV21_tthbbV9_v3_3/ttHTobb_M125_13TeV_powheg_pythia8/VHBBHeppyV21_tthbbV9_v3_3/160518_110721/0000/tree_10.root = 1634
#export GC_SCRATCH=/scratch/sdonato

source env.sh 
source common.sh

#go to work directory
cd $GC_SCRATCH

python ${CMSSW_BASE}/src/TTH/Plotting/python/makeJobfile.py
${CMSSW_BASE}/src/TTH/Plotting/melooper job.json
