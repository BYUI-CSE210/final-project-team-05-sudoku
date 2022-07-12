import os
import random

from tkinter.tix import CELL

from raylib import DEFAULT, FONT_BITMAP

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.scripting.board_creation import Board_Creation

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
#MAX_X = 900
#MAX_Y = 600
MAX_X = 550
MAX_Y = 550
#CELL_SIZE = 15
#FONT_SIZE = 15
CELL_SIZE = 50
FONT_SIZE = 50
SMALL_FONT_SIZE = 14


COLS = 9
ROWS = 9
CAPTION = "Sudoku Game"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
#DEFAULT_ARTIFACTS = 40
MATRIX = 9

# INITIAL_BOARD = [
#     [7, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 0, 4, 0, 0, 0, 2],
#     [1, 0, 8, 5, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 9, 5, 6, 4],
#     [0, 0, 0, 6, 0, 8, 0, 0, 0],
#     [6, 9, 7, 4, 0, 0, 8, 0, 0],
#     [0, 0, 0, 0, 0, 2, 6, 0, 9],
#     [3, 0, 0, 0, 7, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5],
# ]


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(SMALL_FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the artifacts
    board_creation = Board_Creation()
    INITIAL_BOARD = board_creation.board_state()
    # with open(DATA_PATH) as file:
    #   data = file.read()
    # messages = data.splitlines()

    for n in range(MATRIX):
        for j in range(MATRIX):
            text = str(INITIAL_BOARD[n][j])

            #x = random.randint(1, COLS - 1)
            #y = random.randint(1, ROWS - 1)
            position = Point(n + 1, j + 1)
            position = position.scale(CELL_SIZE)

            if INITIAL_BOARD[n][j] != 0:
                print(INITIAL_BOARD[n][j])
                r = (255)
                g = (255)
                b = (255)
            else:
                r = (0)
                g = (0)
                b = (0)
            color = Color(r, g, b)

            artifact = Artifact()
            artifact.set_text(text)
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(color)
            artifact.set_position(position)
            # artifact.set_message(message)
            cast.add_actor("numbers", artifact)

    # create the pointer
    x = 0
    y = 0
    position = Point(x, y)

    robot = Actor()
    robot.set_text("0")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    color = Color(0, 150, 250)
    director = Director(keyboard_service, video_service, color)
    director.start_game(cast)


if __name__ == "__main__":
    main()
