from data.player import Player
from data.player_side import PlayerSide
from data.ball import Ball
from data.ball_direction import BallXDirection, BallYDirection
from data.screen import surface
import pygame
import random

pygame.init()

clock = pygame.time.Clock()
running = True

player_1 = Player(PlayerSide.LEFT, 160)
player_2 = Player(PlayerSide.RIGHT, 1120)

ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))


while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Do logical updates here.
    # ...

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)

pygame.quit()
