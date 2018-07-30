#!/usr/bin/env python

#Version 2.0 for motor controler L298HN

import RPi.GPIO as GPIO

class Motor:
    
    #Constructor
    def __init__(self, motorForward, motorBackward, isForward):
        self.motorForward = motorForward
        self.motorBackward = motorBackward
        self.isForward = isForward
        self.isOn = False

    #Instance methods
    def gpioSetup(self):
        #Numbering
        GPIO.setmode(GPIO.BOARD)
        #Out
        for pinX in [self.motorForward, self.motorBackward]:
            GPIO.setup(pinX, GPIO.OUT)
        self.motorOff()
    
    def motorOn(self):
        if (self.isForward):
            GPIO.output(self.motorForward, True)
            GPIO.output(self.motorBackward, False)
        else:
            GPIO.output(self.motorForward, False)
            GPIO.output(self.motorBackward, True)
        self.isOn = True

    def motorOff(self):
        GPIO.output(self.motorForward, False)
        GPIO.output(self.motorBackward, False)
        self.isOn = False

    def reverseDirection(self):
        if (self.isOn and self.isForward):
            self.isForward = False
            self.motorOn()
        elif (self.isOn and not self.isForward):
            self.isForward = True
            self.motorOn()
        elif (self.isForward):
            self.isForward = False
        elif (not self.isForward):
            self.isForward = True
