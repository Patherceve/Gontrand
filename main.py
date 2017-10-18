#!/usr/bin/env python

#Version 2.0 for motor controler L298HN

import time
import curses
import dualControl

def setupScreen():
    global stdscr, maxY, maxX

    stdscr = curses.initscr()
    curses.start_color()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    maxY, maxX = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.addstr(int(maxY/10),int(maxX/2) - 8, 'G.O.N.T.R.A.N.D.', curses.A_BOLD)
    stdscr.addstr(int(maxY/10) + 1,int(maxX/2) - 2, 'V2.0', curses.A_BOLD)
    stdscr.addstr(int(maxY/10) + 2,int(maxX/20), 'Status: ')
    stdscr.addstr(int(maxY/10) + 3,int(maxX/20), 'Motors: ')
    stdscr.addstr(int(maxY/10) + 4,int(maxX/20), 'Direction: ')

    programStatus(1)
    motorStatus(0)
    directionStatus('None')   

def loop():
    dualControl.setup()
    go = True
    
    while go:
        char = stdscr.getch()
        if (char == 113 or char == 27):
            dualControl.switchOff()       
            programStatus(0)
            stdscr.refresh()
            time.sleep(1)
            stdscr.clear()
            destroyScreen()
            go = False
        elif (char == curses.KEY_UP):
            dualControl.forward()
            motorStatus(1)
            directionStatus('  FW')
        elif (char == curses.KEY_DOWN):
            dualControl.reverse()
            motorStatus(1)
            directionStatus('  RV')
        elif (char == curses.KEY_RIGHT):
            dualControl.rotateCW()
            motorStatus(1)
            directionStatus('rt-R')
        elif (char == curses.KEY_LEFT):
            dualControl.rotateCCW()
            motorStatus(1)
            directionStatus('rt-L')
        elif (char == 32):
            dualControl.switchOff()
            motorStatus(0)
            directionStatus('None')

def programStatus(val):
    if (val):
        stdscr.addstr(int(maxY/10) + 2,int(maxX/20) + 8, 'Running', curses.color_pair(2))
    else:
        stdscr.addstr(int(maxY/10) + 2,int(maxX/20) + 8, '   Quit', curses.color_pair(3))
    stdscr.refresh()

def motorStatus(val):
    if (val):
        stdscr.addstr(int(maxY/10) + 3,int(maxX/20) + 8, '     ON', curses.color_pair(2))
    else:
        stdscr.addstr(int(maxY/10) + 3,int(maxX/20) + 8, '    OFF', curses.color_pair(1))
    stdscr.refresh()

def directionStatus(val):
    stdscr.addstr(int(maxY/10) + 4,int(maxX/20) + 11, val)
    stdscr.refresh()

def destroyScreen():    
    stdscr.keypad(False)
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    setupScreen()
    try:
        loop()
    except KeyboardInterrupt: 
        destroyScreen()
    finally:
        dualControl.gpioCleanup()

