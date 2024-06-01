import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from Displays import LCDDisplay
from Lights import *
from Buzzer import *
from LightStrip import *
from Button import *
#from Game import*
#from Score import*
#from Obstacle import*
#from Character import*


#Turns on the LCD display
mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)

""" Displays welcome message for 5 seconds when starting game """
mydisplay.showText("Welcome to the", row=0, col=0)
mydisplay.showText("Dino Game!", row=1, col=0)
time.sleep(5)
mydisplay.clear()

#Will display the Dinosaur character shape using the hexcode
shapearray = bytearray([0x07, 0x17, 0x16, 0x16, 0x1F, 0x1E, 0x0A, 0x1B])
mydisplay.addShape(0, shapearray)

#Will display the Dinosaur character shape using the hexcode
shapearray = bytearray([0x00, 0x04, 0x05, 0x15, 0x17, 0x1C, 0x04, 0x04])
mydisplay.addShape(0, shapearray)


# Display the custom characters which be a dinosaur, cactuses, and clouds
mydisplay.clear()
mydisplay.showText("Custom Char:", row=0, col=0)
mydisplay.showText("Dino and cactus", row=1, col=0)
time.sleep(5)

#Incorporating some of our work from the first mini-lab.
red =  Light(6, "Red light")
green =  Light(7, "Green light")
buzzer = PassiveBuzzer(16)
mylightstrip = LightStrip(name="My light strip", pin=2, numleds=16)

# for ever loop and blink the red and green in turn
for x in range(0,10): #whle True:#
  #Blink the red once
  red.blink(delay=0.5, times=1)
  #Blink the green once
  green.blink(delay=0.5, times=1)
  
  mylightstrip.blink(delay=0.5, times=1)
  buzzer.beep()
