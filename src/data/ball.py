import pygame
from src.data.screen import surface

# constants: initial values for a ball
INITIAL_X_POSITION = surface.get_width()/2
INITIAL_Y_POSITION = surface.get_height()/2


class Ball:
    # class variable (ball has the same speed at any instance)
    SPEED = 10

    # constructor (set initial data for a new ball)
    def __init__(self, x_direction, y_direction):
        self.x_position = INITIAL_X_POSITION
        self.y_position = INITIAL_Y_POSITION
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.circle = pygame.draw.circle(surface, "white", (self.x_position,self.y_position), 15)
