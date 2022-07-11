import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size=1):
        """Constructs a new KeyboardService using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)

        return direction

    def get_number(self):
        """Gets the selected number based on the currently pressed keys.

        Returns:
            Int: number.
        """
        number = ""

        if pyray.is_key_down(pyray.KEY_ONE):
            number = 1

        if pyray.is_key_down(pyray.KEY_TWO):
            number = 2

        if pyray.is_key_down(pyray.KEY_THREE):
            number = 3

        if pyray.is_key_down(pyray.KEY_FOUR):
            number = 4

        if pyray.is_key_down(pyray.KEY_FIVE):
            number = 5

        if pyray.is_key_down(pyray.KEY_SIX):
            number = 6

        if pyray.is_key_down(pyray.KEY_SEVEN):
            number = 7

        if pyray.is_key_down(pyray.KEY_EIGHT):
            number = 8

        if pyray.is_key_down(pyray.KEY_NINE):
            number = 9

        return str(number)

    def reset_game(self):
        """Activate reset game when the user press "r" key.

        Returns:
            Int: Boolean.
        """

        if pyray.is_key_down(pyray.KEY_R):

            return True

        return False
