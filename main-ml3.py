import time
from Displays import LCDDisplay
from MusicController import *



time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")


""" Displays welcome message for 5 seconds when starting instrument """
mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
mydisplay.showText("Loading Annie's", row=0, col=0)
mydisplay.showText("Instrument!", row=1, col=0)
time.sleep(5) 

MusicController().run()