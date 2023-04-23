import pygame
import random
import math
from src.data.screen import surface

# constants: initial values for a ball
INITIAL_X_POSITION = surface.get_width()/2
INITIAL_Y_POSITION = surface.get_height()/2


class Ball:
    # class variable (ball has the same speed at any instance)
    SPEED = 300
    RADIUS = 7.5

    # constructor (set initial data for a new ball)
    def __init__(self, x_direction, y_direction):
        self.position = pygame.Vector2(INITIAL_X_POSITION, INITIAL_Y_POSITION)
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.circle = pygame.draw.circle(surface, "white", (self.position.x, self.position.y), Ball.RADIUS * 2)
        self.x_speed = random.randint(200, Ball.SPEED)
        self.y_speed = math.sqrt((Ball.SPEED**2) - (self.x_speed**2))
