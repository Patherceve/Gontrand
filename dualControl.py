#!/usr/bin/env python

#Version 2.0 for motor controler L298HN

import RPi.GPIO as GPIO
from Motor import *

def setup():
    global rightMotor, leftMotor

    rightMotor = Motor(7, 11, True)
    leftMotor  = Motor(13, 15, True)
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

def gpioCleanup():
    GPIO.cleanup()
