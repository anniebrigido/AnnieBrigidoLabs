import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from Lights import *
from Buzzer import *
from LightStrip import *
from Displays import LCDDisplay

red =  Light(6, "Red light")
green =  Light(7, "Green light")
buzzer = PassiveBuzzer(16)
mylightstrip = LightStrip(name="My light strip", pin=2, numleds=16)
mydisplay = LCDDisplay(sda = 0, scl = 1, i2cid=0)

mydisplay.showText("Hello world")

# for ever loop and blink the red and green in turn
for x in range(0,10): #whle True:#
  #Blink the red once
  red.blink(delay=0.5, times=1)
  #Blink the green once
  green.blink(delay=0.5, times=1)
  
  mylightstrip.blink(delay=0.5, times=1)
  buzzer.beep()