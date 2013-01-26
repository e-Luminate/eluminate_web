#!/usr/bin/env python

# determines filename and extension, 
# then delegates compiling the LESS files to lessc via a shell command

import sys, os.path
from subprocess import call
import glob

SRC_PATH = "eluminate_web/static/less/"
DEST_PATH = "eluminate_web/static/css/"


                      
for less_file in glob.glob(os.path.join(SRC_PATH, "*.less")):

    base,ext = os.path.splitext(os.path.basename(less_file))
    dest_file = base + ".css"
    
    cmd = "lessc {0} > {1}".format(less_file , os.path.join(DEST_PATH, dest_file))
    print "Recompiling css with command {0}".format(cmd)
    call( cmd , shell=True)
    
