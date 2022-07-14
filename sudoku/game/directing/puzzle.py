from game.directing.director import Director


class Puzzle(Director):
    """It help to validate the entries of the user, if it is in the row and in the column. 

      The responsibility of Puzzle is to keep track of the numbers of the game, and the validation.

      Attributes:
      """

    def __init__(self):
        self.numbers_board = []
        self.x = 0
        self.y = 0
        self.number = 0

    def set_board(self, matrix):

        for numbers in matrix:
            self.numbers_board.append(numbers)

    def get_board(self):

        return self.numbers_board

    def update_board(self, x, y, number):

    def validate_board(self, x, y):
