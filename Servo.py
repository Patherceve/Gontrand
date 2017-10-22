#!/usr/bin/env python

import Adafruit_PCA9685
import time

class Servo:
    #Constructor
    def __init__(self, channel, startPos):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pulseRange = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
        self.channel = channel
        self.currentPos = startPos

    #Instance method
    def servoSetup(self):
        pwm.set_pwm_freq(60)
        pwm.set_pwm(self.channel, 0, self.pulseRange[currentPos])
        time.sleep(0.3)
        pwm.set_pwm(self.channel, 0, 0)
    
    def changePos(self, newPos):
        if(self.currentPos > newPos):
            for p in range(self.currentPos, (newPos - 1), -1):
                pwm.set_pwm(self.channel, 0, self.pulseRange[p])
                time.sleep(0.08)
            self.currentPos = p
            pwm.set_pwm(self.channel, 0, self.pulseRange[p])
        elif(self.currentPos < newPos):
            for p in range(self.currentPos, (newPos + 1), 1):
                pwm.set_pwm(self.channel, 0, self.pulseRange[p])
                time.sleep(0.08)
            self.currentPos = p
            pwm.set_pwm(self.channel, 0, self.pulseRange[p])
        else:
            pwm.set_pwm(self.channel, 0, 0)
        self.currentPos = newPos
