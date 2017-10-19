#!/usr/bin/env python

from __future__ import division
import Adafruit_PCA9685
import time

sCtrl = Adafruit_PCA9685.PCA9685()

# Pulse lengths
servoRange = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

def setup():
    # Set frequency to 60hz, good for servos.
    sCtrl.set_pwm_freq(60)

def loop():
    while True:
        for r in servoRange:
            changePulse(r)
        for r in reversed(servoRange):
            changePulse(r)
    
def changePulse(p):
    sCtrl.set_pwm(1, 0, p)
    sCtrl.set_pwm(0, 0, p)
    time.sleep(0.05)
    sCtrl.set_pwm(1, 0, 0)
    sCtrl.set_pwm(0, 0, 0)

def destroy():
    sCtrl.set_pwm(1, 0, 350)
    sCtrl.set_pwm(0, 0, 350)
    time.sleep(0.5)
    sCtrl.set_pwm(1, 0, 0)
    sCtrl.set_pwm(0, 0, 0)
    
if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
