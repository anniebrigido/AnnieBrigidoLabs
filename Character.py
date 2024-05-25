#Character class controls the game.

class Character:
    #Attributes include position and state.
    def __init__(self, position, state="standing"):
        #Initializes the character
        self.position = position
        self.state = state

    #Operation of the character class include jump, duck, and run.
    def jump(self):
        #Allows for a character to jump.
        print("Character jumps")
        self.state = "jumping"

    def duck(self):
        #Allows for a character to duck.
        print("Character ducks")
        self.state = "ducking"

    def run(self):
        #Allows for a character to run.
        print("Character runs")
        self.state = "running"