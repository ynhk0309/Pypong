from data.player import Player
from data.player_side import PlayerSide
from data.ball import Ball
from data.ball_direction import BallXDirection, BallYDirection

# creating a new ball
ball = Ball(BallXDirection.RIGHT, BallYDirection.UP)

print(ball.X_POSITION, ball.Y_POSITION, ball.x_direction, ball.y_direction, ball.SPEED)
