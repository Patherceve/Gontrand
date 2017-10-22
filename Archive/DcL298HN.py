#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def setup():
    global leftMotorForward, leftMotorBackward, rightMotorForward, rightMotorBackward

    leftMotorForward = 7
    leftMotorBackward = 11
    rightMotorForward = 13
    rightMotorBackward = 15

    GPIO.setmode(GPIO.BOARD)           
    GPIO.setup(leftMotorForward, GPIO.OUT)
    GPIO.setup(leftMotorBackward, GPIO.OUT)
    GPIO.setup(rightMotorForward, GPIO.OUT)
    GPIO.setup(rightMotorBackward, GPIO.OUT)
    GPIO.output(leftMotorForward, GPIO.LOW)
    GPIO.output(leftMotorBackward, GPIO.LOW)
    GPIO.output(rightMotorForward, GPIO.LOW)
    GPIO.output(rightMotorBackward, GPIO.LOW)
    
def loop():
    while True:
        GPIO.output(leftMotorForward, GPIO.HIGH)
        GPIO.output(leftMotorBackward, GPIO.LOW)
        GPIO.output(rightMotorForward, GPIO.HIGH)
        GPIO.output(rightMotorBackward, GPIO.LOW)
        time.sleep(2)
        GPIO.output(leftMotorForward, GPIO.LOW)
        GPIO.output(leftMotorBackward, GPIO.HIGH)
        GPIO.output(rightMotorForward, GPIO.LOW)
        GPIO.output(rightMotorBackward, GPIO.HIGH)
        time.sleep(2)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
