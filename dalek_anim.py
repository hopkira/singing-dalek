#!/usr/bin/env python3
"""Dalek State Machine

This module animates the dalek.  It assumes the use of an
Adafruit Servo Controller to control an iris servo
and the lights within the eye and dome
(using a TIP120 transistor to amplify the PWM signal)
Userful blog posts for setup: https://k9-build.blogspot.com/search/label/dalek

Dalek and K9 word marks and logos are trade marks of the British Broadcasting Corporation and
are copyright BBC/Terry Nation 1963

"""
import time

# import servo board
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

FREQUENCY = 50
PERIOD = 1.0 / float(FREQUENCY) * 1000.0

# create iris servo
i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = FREQUENCY

# Servo Channels
IRIS_SERVO = 4
DOME_LIGHTS = 0
IRIS_LIGHT = 1

# Convenience Servo Values
ON = 1.0
AWAKE = True
ASLEEP = False
OFF = 0.0
STEPS = 100
DURATION = 1.0
SERVO_MAX = 0.8
SERVO_MIN = 0.2

SERVO_MAX = 0.8
SERVO_MIN = 0.2

def dalek_status(direction):
    """
    Opens or closes the dalek eye and lights

    Arg:
        direction (boolean): True to open, False to close
    """
    dalek_servo(IRIS_SERVO, 1-direction)
    dalek_light(IRIS_LIGHT, 1-direction)
    for pos in range(0, STEPS):
        if direction:
            value = (float(pos) / float(STEPS))**4
        else:
            value = (1.0 - (float(pos) / float(STEPS)))**4
        dalek_servo(IRIS_SERVO, value)
        dalek_light(IRIS_LIGHT, value)
        time.sleep(DURATION/STEPS)
    dalek_servo(IRIS_SERVO, direction)
    dalek_light(IRIS_LIGHT, direction)

def dalek_servo(channel, value):
    """
    Changes the servo position of a servo on the Adafruit controller.
    Maximum and minumum safe positions are pre-calculated.

    Args:
        channel (int): the channel number of the servo (range 0-16)
        value (float): value between 0.0 and 1.0
    """
    value = SERVO_MIN + (value * (SERVO_MAX - SERVO_MIN)) # normalise between MAX and MIN
    value = 1.0 - value # reverse value
    value = value + 1.0 # change to range 1.2 to 1.8
    duty_cycle = int(value / (PERIOD / 65535.0))
    pca.channels[channel].duty_cycle = duty_cycle

def dalek_light(channel, value):
    """
    Changes the level of illumination of a light attached to the
    PWM output of the servo controller.

    Args:
        channel (int): the channel number of the servo (range 0-16)
        value (float): value between 0.0 and 1.0
    """
    pca.channels[channel].duty_cycle = int(value * 65535.0)
