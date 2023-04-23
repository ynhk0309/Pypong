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

BORDER_WIDTH = 10

player_1 = Player(PlayerSide.LEFT, 160)
player_2 = Player(PlayerSide.RIGHT, 1120)

ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))

font = pygame.font.SysFont(None, 100)
player1_score = font.render(str(player_1.score), True, "white")
player1_score_rect = player1_score.get_rect(center=(surface.get_width()/2 - 100, 70))
player2_score = font.render(str(player_2.score), True, "white")
player2_score_rect = player2_score.get_rect(center=(surface.get_width()/2 + 100, 70))

dt = 0

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.position.x = ball.position.x + (ball.x_direction.value * ball.x_speed * dt)
    ball.position.y = ball.position.y + (ball.y_direction.value * ball.y_speed * dt)

    if ball.position.x <= 0 + BORDER_WIDTH:
        # left player loses (update the score)
        # game reset
        pass
    if ball.position.x >= surface.get_width() - BORDER_WIDTH:
        # right player loses (update the score)
        # game reset
        pass
    if ball.position.y <= 0 + Ball.RADIUS + BORDER_WIDTH + 5:
        ball.y_direction = BallYDirection(ball.y_direction.value * (-1))
    if ball.position.y >= surface.get_height() - Ball.RADIUS - BORDER_WIDTH - 5:
        ball.y_direction = BallYDirection(ball.y_direction.value * (-1))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_1.position.y > 0 + BORDER_WIDTH + 5:
        player_1.position.y -= Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_s] and player_1.position.y < surface.get_height() - Player.LENGTH - BORDER_WIDTH - 5:
        player_1.position.y += Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_UP] and player_2.position.y > 0 + BORDER_WIDTH + 5:
        player_2.position.y -= Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_DOWN] and player_2.position.y < surface.get_height() - Player.LENGTH - BORDER_WIDTH - 5:
        player_2.position.y += Player.PLAYER_VELOCITY * dt

    surface.fill("black")

    pygame.draw.rect(surface, "white", pygame.Rect(0, 0, surface.get_width(), surface.get_height()), BORDER_WIDTH)

    surface.blit(player1_score, player1_score_rect)
    surface.blit(player2_score, player2_score_rect)

    ball.circle = pygame.draw.circle(surface, "white", (ball.position.x, ball.position.y), Ball.RADIUS * 2)
    player_1.rec = pygame.draw.rect(surface, "white", pygame.Rect(player_1.position.x, player_1.position.y, 30, Player.LENGTH))
    player_2.rec = pygame.draw.rect(surface, "white", pygame.Rect(player_2.position.x, player_2.position.y, 30, Player.LENGTH))

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)

pygame.quit()
