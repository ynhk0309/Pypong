# constants: initial values for a player that don't depend on the player
INITIAL_Y_POSITION = 300
INITIAL_Y_VELOCITY = 0
INITIAL_SCORE = 0


class Player:
    # class variable (every player has the same length)
    LENGTH = 50

    # constructor (set initial data for a new player)
    def __init__(self, player_id, initial_x_position):
        self.player_id = player_id
        self.y_position = INITIAL_Y_POSITION
        self.x_position = initial_x_position
        self.y_velocity = INITIAL_Y_VELOCITY
        self.score = INITIAL_SCORE
