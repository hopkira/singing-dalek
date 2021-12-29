import os
import time
import csv

SPEED_DEFAULT = 175
AMP_DEFAULT = 190
AMP_UP = 200
AMP_DOWN = 180
PITCH_DEFAULT = 99
SOX_PITCH_DEFAULT = 0
CENTRAL_NOTE = 'C'
CENTRAL_NOTE_CENTS = 26
SOX_VOL_UP = 5000
SOX_VOL_DEFAULT = 20
SOX_VOL_DOWN = 10

note_cents_dict = {
    '+': {'cent': 1200},
    '-': {'cent': -1200},
    'A': {'cent': -300},
    'B': {'cent': -100},
    'C': {'cent': 0},
    'D': {'cent': 200},
    'E': {'cent': 400},
    'F': {'cent': 500},
    'G': {'cent': 700}
    }

def note_to_cents(note):
    cents = CENTRAL_NOTE_CENTS
    for modifier in note:
        cents = cents + note_cents_dict[modifier]['cent']
    return cents

def sing(filename):
    with open(filename) as csvfile:
        song = csv.reader(csvfile)
        for note, duration, syllable, volume in song:
            speed = SPEED_DEFAULT
            amplitude = AMP_DEFAULT
            pitch = PITCH_DEFAULT
            sox_vol = SOX_VOL_DEFAULT
            sox_pitch = SOX_PITCH_DEFAULT
            # Alter volume of syllable if indicated
            if volume == ">":
                sox_vol = SOX_VOL_UP
                amplitude = AMP_UP
            elif volume == '<':
                sox_vol = SOX_VOL_DOWN
                amplitude = AMP_DOWN
            # Either pause, or speak the syllable
            if note == 'P':
                time.sleep(float(duration)/4.0)
            else:
                sox_pitch = note_to_cents(note) # adjust pitch
                speed = 175/float(duration) # adjust speed
            cmd = "espeak -v en-rp '%s' -p %s -s %s -a %s -z --stdout|play -v %s - synth sine fmod 25 pitch %s" % (syllable, pitch, speed, amplitude, sox_vol, sox_pitch)
            os.system(cmd)

if __name__ == "__main__":
    import argparse
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, default='jinglebells.csv',
        help="CSV input filename for song")
    args = vars(ap.parse_args())
    sing(args['input'])