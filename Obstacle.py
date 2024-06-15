from Displays import *

# Obstacle class
class Obstacle:
    Obstacle_shape = [0x00, 0x04, 0x05, 0x15, 0x17, 0x1C, 0x04, 0x04]

    # Attributes of the obstacle class include: position and type
    def __init__(self, x, y, display):
        # Initializing with a position and display
        self.x_position = x
        self.y_position = y
        self.state = "moving"  # Initial state of the obstacle
        self.display = display
        self.display.addShape(1, bytearray(Obstacle.Obstacle_shape))  # Add shape at position 1

    # Move operation allows moving the obstacle.
    def move(self):
        if self.state == "moving":
            self.x_position -= 1
            if self.x_position < 0:
                self.x_position = self.display.getWidth()  # Reset position to right of the display

    def update(self):
        self.move()
        self.display.showText(chr(1), row=self.y_position, col=self.x_position)  # Use custom character at position 1
