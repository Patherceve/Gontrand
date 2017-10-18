#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

class Motor:

    #Class variable
    pwmHzSet = 160
    dutyCycle = [60, 80, 100]
    
    #Constructor
    def __init__(self, pin1, pin2, pinEnable, isForward):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pinEnable = pinEnable
        self.isForward = isForward
        self.isOn = False
        self.currentDutyCycle = Motor.dutyCycle[0]

    #Instance methods
    def gpioSetup(self):
        #Numbering
        GPIO.setmode(GPIO.BOARD)
        #Out
        for pinX in [self.pin1, self.pin2, self.pinEnable]:
            GPIO.setup(pinX, GPIO.OUT)
        #PWM
        self.pwmSpeed = GPIO.PWM(self.pinEnable, Motor.pwmHzSet)
        self.pwmSpeed.start(0)
        #FW_RV
        if (self.isForward):
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.HIGH)
        else:
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
    
    def motorOn(self):
        self.pwmSpeed.ChangeDutyCycle(self.currentDutyCycle)
        self.isOn = True

    def motorOff(self):
        self.pwmSpeed.ChangeDutyCycle(0)
        self.isOn = False

    def speedControl(self, preset):
        if (self.isOn):
            self.pwmSpeed.ChangeDutyCycle(Motor.dutyCycle[preset])
        self.currentDutyCycle = Motor.dutyCycle[preset]

    def reverseDirection(self):
        if (self.isForward):
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
            self.isForward = False
        else:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.HIGH)
            self.isForward = True

        
