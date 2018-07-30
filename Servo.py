#!/usr/bin/env python

import Adafruit_PCA9685
import time

class Servo:
    
    #Constructor
    def __init__(self, channel, servo_min, servo_max, frequency):
        self.channel = channel
        self.servo_min = servo_min
        self.servo_max = servo_max
        self.frequency = frequency
        
    def setup(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(self.frequency)
        
    def setPulse(self, pulse):
        if(pulse < self.servo_min):
            pulse = self.servo_min
        elif(pulse > self.servo_max):
            pulse = self.servo_max
        self.pwm.set_pwm(self.channel, 0, pulse)

        