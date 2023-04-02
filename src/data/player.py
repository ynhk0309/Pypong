import pygame
from src.data.screen import surface

# constants: initial values for a player that don't depend on the player
INITIAL_Y_VELOCITY = 0
INITIAL_SCORE = 0


class Player:
    # class variable (every player has the same length for the paddle)
    LENGTH = 50

    # constructor (set initial data for a new player)
    def __init__(self, player_id, initial_x_position):
        self.player_id = player_id
        self.position = pygame.Vector2(initial_x_position, surface.get_height()/2)
        self.y_velocity = INITIAL_Y_VELOCITY
        self.score = INITIAL_SCORE
        self.rec = pygame.draw.rect(surface, "white", pygame.Rect(self.position.x, self.position.y, 30, 90))
