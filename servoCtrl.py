#!/usr/bin/env python

from __future__ import division
import Adafruit_PCA9685
import time

sCtrl = Adafruit_PCA9685.PCA9685()

# Pulse lengths
servo_range = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

def setup():
    # Set frequency to 60hz, good for servos.
    sCtrl.set_pwm_freq(60)

def loop():
    while True:
        for r in range(150, 601, 50):
            changePulse(r)
        for r in range(600, 149, -50):
            changePulse(r)
    
def changePulse(p):
    sCtrl.set_pwm(2, 0, p)
    time.sleep(0.05)
    sCtrl.set_pwm(2, 0, 0)

def destroy():
    sCtrl.set_pwm(2, 0, 350)
    time.sleep(1)
    sCtrl.set_pwm(2, 0, 0)
    
if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
