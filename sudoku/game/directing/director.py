from game.shared.color import Color
from game.shared.point import Point
from game.scripting.board_creation import Board_Creation
from game.casting.artifact import Artifact


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, color):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._color = color
        self._number = ''
        self._reset_game = False

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

        self._number = self._keyboard_service.get_number()

        if self._keyboard_service.reset_game():
            self._reset_game = True
            return

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        numbers = cast.get_actors("numbers")

        banner.set_text(
            "Move the selector with arrows and reset the game with the 'R' Letter")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for artifact in numbers:
            if robot.get_position().equals(artifact.get_position()):
                if artifact.get_text() == '0' and self._number != "" or artifact.get_color() == self._color and self._number != "":
                    artifact.set_text(self._number)
                    artifact.set_color(self._color)

        if self._reset_game:
            self._reset(cast)
            return

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _reset(self, cast):
        """This method reset the numbers and robot at the first time.

        Args:
            cast (Cast): The cast of actors.
        """

        robot = cast.get_first_actor("robots")
        x = 0
        y = 0
        position = Point(x, y)
        robot.set_position(position)

        numbers = cast.get_actors("numbers")

        for artifact in numbers:
            cast.remove_actor("numbers", artifact)

        # create the board of numbers
        board_creation = Board_Creation()
        INITIAL_BOARD = board_creation.board_state()

        for n in range(9):
            for j in range(9):
                text = str(INITIAL_BOARD[n][j])

                position = Point(n + 1, j + 1)
                position = position.scale(50)

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
                artifact.set_font_size(50)
                artifact.set_color(color)
                artifact.set_position(position)
                cast.add_actor("numbers", artifact)

        self._reset_game = False
