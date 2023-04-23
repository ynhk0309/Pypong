from data.player import Player
from data.player_side import PlayerSide
from data.ball import Ball
import random
from data.ball_direction import BallXDirection, BallYDirection

# creating a new ball
ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))
print(type(ball.y_direction.value))