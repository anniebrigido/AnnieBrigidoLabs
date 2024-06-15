import time
from DinoGameController import DinoGameController

time.sleep(0.1)  # Wait for USB to become ready

print("Hello, Pi Pico!")

# Initialize and run the game controller
game_controller = DinoGameController()
game_controller.start_game()
game_controller.game_loop()
