# constants: initial values for a ball
INITIAL_X_POSITION = 300
INITIAL_Y_POSITION = 200


class Ball:
    # class variable (ball has the same speed at any instance)
    SPEED = 10

    # constructor (set initial data for a new ball)
    def __init__(self, x_direction, y_direction):
        self.x_position = INITIAL_X_POSITION
        self.y_position = INITIAL_Y_POSITION
        self.x_direction = x_direction
        self.y_direction = y_direction
