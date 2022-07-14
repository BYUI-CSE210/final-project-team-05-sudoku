
"""
class Insert():

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
"""
board = [
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 4, 0, 0, 0, 2],
    [1, 0, 8, 5, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 9, 5, 6, 4],
    [0, 0, 0, 6, 0, 8, 0, 0, 0],
    [6, 9, 7, 4, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 2, 6, 0, 9],
    [3, 0, 0, 0, 7, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
]

board_2 = []


for numbers in board:
    board_2.append(numbers)

print(board_2)
