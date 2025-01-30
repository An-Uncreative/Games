# README.md

# Python Game Project

This is a simple Python game that utilizes the Pygame library for rendering graphics and handling user input. It also makes use of object oriented programming to put buttons on the screen for starting and exiting the game.

## Files

- `main.py`: Contains the main game loop, event handling, and rendering logic. It initializes the game, handles user input for movement, and draws the game elements on the screen. The game starts upon a mouse click on the start button, which removes the background image and starts the game.
- `button.py`: Contains the Button class, which is written to put the buttons on the screen.
- `assets/background.png`: The background image used in the game, which will be removed from the display when the user clicks the start button to play the game.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd python-game-project
   ```
3. Install the required dependencies:
   ```
   pip install pygame
   ```

## Running the Game

To run the game, execute the following command in your terminal:
```
python main.py
```

Click anywhere on the screen to start the game and remove the background image. Enjoy!