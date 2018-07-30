#!/usr/bin/env python

from Servo import *

def setup():
    global xAxis, yAxis, minPulse, midPulse, maxPulse
    
    minPulse = 150
    midPulse = 350
    maxPulse = 600
    xAxis = Servo(0, minPulse, maxPulse, 60)
    yAxis = Servo(1, minPulse, maxPulse, 60)
    cleanStart()
    
def lookUp():
    yAxis.setPulse(minPulse)

def lookDown():
    yAxis.setPulse(maxPulse)
    
def lookRight():
    xAxis.setPulse(minPulse)
    
def lookLeft():
    xAxis.setPulse(maxPulse)
    
def center():
    xAxis.setPulse(midPulse)
    yAxis.setPulse(midPulse)

def cleanStart():
    xAxis.setup()
    yAxis.setup()