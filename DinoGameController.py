import time
from Displays import LCDDisplay
from Button import Button
from Game import Game
from Buzzer import PassiveBuzzer
from LightStrip import *

class DinoGameController:
    """ Controller for the Dino Game """

    def __init__(self):
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._game = Game(display=self._display)
        self._jump_button = Button(10, "Jump", buttonhandler=self)
        self._duck_button = Button(11, "Duck", buttonhandler=self)
        self._buzzer = PassiveBuzzer(16)
        self._lights = LightStrip(name="My light strip", pin=2, numleds=16)
        self._red_light = Light(6, "Red light")
        self._green_light = Light(7, "Green light")

    def start_game(self):
        # Displays welcome message for 5 seconds when starting the game
        self._display.showText("Welcome to Annie", row=0, col=0)
        self._display.showText("Dino Game!", row=1, col=0)
        time.sleep(5)
        self._display.clear()

        self._game.start_game()

    def buttonPressed(self, name):
        if name == "Jump":
            self._game.jump()
            self._buzzer.beep()
            self._green_light.blink(delay=0.5, times=1)
            self._lights.setColor(GREEN, 16)
            time.sleep(2)
        elif name == "Duck":
            self._game.duck()
            self._buzzer.beep()
            self._red_light.blink(delay=0.5, times=1)
            self._lights.setColor(RED, 16)
            time.sleep(2)

    def buttonReleased(self, name):
        print(f"Button {name} released")

    def game_loop(self):
        while not self._game.game_over:
            self.check_buttons()
            self._game.update_game()
            time.sleep(0.1)
        self._game.end_game()
        while self._game.game_over:
            self.check_buttons()
            if self._jump_button.isPressed() or self._duck_button.isPressed():
                self._game = Game(display=self._display)
                self.start_game()

    def check_buttons(self):
        if self._jump_button.isPressed():
            self.buttonPressed("Jump")
        if self._duck_button.isPressed():
            self.buttonPressed("Duck")
