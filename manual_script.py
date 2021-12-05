#!/usr/bin/env python3
"""
Simple script combining animation with choral singing
"""
import dalek_anim as DalekBody
import singing_dalek as DalekVoice
import time

# Close eyes
DalekBody.dalek_status(False)
time.sleep(5)
DalekBody.dalek_status(True)
DalekVoice.sing("jinglebells.csv")
time.sleep(1)
DalekBody.dalek_status(False)