#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from Motor import *

def setup():
    global rightMotor, leftMotor

    rightMotor = Motor(11, 12, 13, True)
    leftMotor  = Motor(15, 16, 18, True)
    rightMotor.gpioSetup()
    leftMotor.gpioSetup()

def switchOn():
    rightMotor.motorOn()
    leftMotor.motorOn()

def switchOff():
    rightMotor.motorOff()
    leftMotor.motorOff()

def forward():
    if (not rightMotor.isForward):
        rightMotor.reverseDirection()
    if (not leftMotor.isForward):
        leftMotor.reverseDirection()
    switchOn()

def reverse():
    if (rightMotor.isForward):
        rightMotor.reverseDirection()
    if (leftMotor.isForward):
        leftMotor.reverseDirection()
    switchOn()

def rotateOrTurn(val):
    if (rightMotor.isOn and leftMotor.isOn and rightMotor.isForward and leftMotor.isForward):
        if (val):
            rightMotor.pwmSpeed.ChangeDutyCycle(int(0.65 * rightMotor.currentDutyCycle))
            leftMotor.pwmSpeed.ChangeDutyCycle(leftMotor.currentDutyCycle)
        else:
            rightMotor.pwmSpeed.ChangeDutyCycle(rightMotor.currentDutyCycle)
            leftMotor.pwmSpeed.ChangeDutyCycle(int(0.65 * leftMotor.currentDutyCycle))   
    else:
        if (val):
            rotateCCW()
        else:
            rotateCW()

def rotateCW():
    if (not rightMotor.isForward):
        rightMotor.reverseDirection()
    if (leftMotor.isForward):
        leftMotor.reverseDirection()
    switchOn()

def rotateCCW():
    if (rightMotor.isForward):
        rightMotor.reverseDirection()
    if (not leftMotor.isForward):
        leftMotor.reverseDirection()
    switchOn()

def setSpeed(index):
    rightMotor.speedControl(index)
    leftMotor.speedControl(index)

def gpioCleanup():
    GPIO.cleanup()
