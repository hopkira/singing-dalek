#!/bin/bash
source /home/pi/.virtualenvs/coral/bin/activate
python3 /home/pi/coral-dalek/flash_lights.py &
python3 /home/pi/singing-dalek/manual_script.py &
