from Displays import *

# Character class controls the game.
class Character:
    # Attributes include position and state.
    Character_shape = [0x07, 0x17, 0x16, 0x16, 0x1F, 0x1E, 0x0A, 0x1B]

    def __init__(self, x, y, display):
        # Initializes the character
        self.position_x = x 
        self.position_y = y
        self.state = "run"  # Initial state of the character
        self.jump_height = 0
        self.display = display
        self.display.addShape(0, bytearray(Character.Character_shape))  # Add shape at position 0

    # Operations of the character class include jump, duck, and run.
    def jump(self):
        # Allows for a character to jump.
        print("Character jumps")
        self.state = "jump"
        self.jump_height = 2

    def duck(self):
        # Allows for a character to duck.
        print("Character ducks")
        self.state = "duck"
        self.position_y = 2

    def run(self):
        # Allows for a character to run.
        print("Character runs")
        self.state = "run"
        self.position_y = 1

    def update(self):
        if self.state == "jump" and self.jump_height > 0:
            self.position_y -= 1
            self.jump_height -= 2
        elif self.state == "jump" and self.jump_height == 0:
            self.run()
        else:
            self.position_y = 1

    def collides_with(self, obstacle):
        return self.position_x == obstacle.x_position and self.position_y == obstacle.y_position
