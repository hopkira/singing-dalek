#!/usr/bin/env python3
"""
Simple script combining animation with choral singing
"""
import dalek_anim as DalekBody
import singing_dalek as DalekVoice
import time
import argparse
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default='jinglebells.csv',
    help="CSV input filename for song")
args = vars(ap.parse_args())
DalekBody.dalek_status(False)
time.sleep(5)
DalekBody.dalek_status(True)
DalekVoice.sing(args['input'])
time.sleep(1)
DalekBody.dalek_status(False)