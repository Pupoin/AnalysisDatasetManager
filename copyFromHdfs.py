#!/usr/bin/env python

import argparse
import glob
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to files in hdfs")
parser.add_argument("-s", "--selection", type=str, default="FinalSelection",
        help="Selection tier (default FinalSelection)")
args = parser.parse_args()

for directory in glob.glob(args.path):
    print directory
    if not os.path.isdir(directory):
        print "Invalid filename: %s" % directory
        exit(1)
    dir_name = directory.split("/")[-1]
    new_dir = "/data/kelong/WZAnalysisData/%s/%s" % (args.selection, dir_name)
    os.mkdir(new_dir)
    for filename in glob.glob(directory + "/*"):
        subprocess.call(["xrdcp", 
            "root://cmsxrootd.hep.wisc.edu/%s" % filename[5:], 
            new_dir]
        )