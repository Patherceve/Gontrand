import tkinter
import dualControl
import dualAxis
import picamera
import os
import sys
import time

def cameraSetup():
    global camera
    camera = picamera.PiCamera()
    
def cameraOn():
    camera.preview_fullscreen = False
    camera.preview_window = (50, 50, 640, 480)
    camera.resolution = (640,480)
    camera.start_preview()

def cameraOff():
    camera.stop_preview()

def keydown(event):
    print('down' + event.keysym)
    if(event.keysym == 'q'):
        sys.exit('Exiting the program')
    elif(event.keysym == 'w'):
        dualControl.forward()
    elif(event.keysym == 'a'):
        dualControl.rotateCCW()
    elif(event.keysym == 'd'):
        dualControl.rotateCW()
    elif(event.keysym == 's'):
        dualControl.reverse()
    elif(event.keysym == 'Up'):
        dualAxis.lookUp()
    elif(event.keysym == 'Down'):
        dualAxis.lookDown()
    elif(event.keysym == 'Right'):
        dualAxis.lookRight()
    elif(event.keysym == 'Left'):
        dualAxis.lookLeft()
    elif(event.keysym == 'Control_R'):
        dualAxis.center()


def keyup(event):
    print('up' + event.keysym)
    if(event.keysym == 'w' or event.keysym == 'a' or event.keysym == 'd' or event.keysym == 's'):
        dualControl.switchOff()
    if(event.keysym == 'Up' or event.keysym == 'Down' or event.keysym == 'Right' or event.keysym == 'Left'):
        dualAxis.cleanStart()

def loop():
    window = tkinter.Tk() #Build the GUI
    window.title("Gontrand V3")
    window.resizable(width=False, height=False)
    window.geometry("320x300+690+50")
    window.bind("<KeyPress>", keydown) #Listen to press keyboard events
    window.bind("<KeyRelease>", keyup) #Listen to release keyboard events
    window.focus_set()
    
    window.buttonframe = tkinter.Frame(window)
    window.buttonframe.grid(row = 5, column = 3, columnspan = 2)
    
    tkinter.Button(window.buttonframe, text = "Start Camera", command = cameraOn).grid(row = 2, column = 1)
    tkinter.Button(window.buttonframe, text = "Kill Camera", command = cameraOff).grid(row = 2, column = 3)
    cameraOn()
    
    window.mainloop()

if __name__ == '__main__':
    os.system('xset r off') #Stop the repeating key
    cameraSetup() #Set the camera
    dualControl.setup() #Set the motors
    dualAxis.setup() #Set the servos
    try:
        loop()
    finally:
        dualAxis.center()
        time.sleep(1)
        cameraOff()
        dualControl.gpioCleanup()
        dualAxis.cleanStart()
        os.system('xset r on')