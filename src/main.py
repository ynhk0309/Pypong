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

player_left = Player(PlayerSide.LEFT, 160)
player_right = Player(PlayerSide.RIGHT, 1120)

ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))

font = pygame.font.SysFont(None, 100)
player_left_score = font.render(str(player_left.score), True, "white")
player_left_score_rect = player_left_score.get_rect(center=(surface.get_width() / 2 - 100, 70))
player_right_score = font.render(str(player_right.score), True, "white")
player_right_score_rect = player_right_score.get_rect(center=(surface.get_width() / 2 + 100, 70))

final_statement = None
BOX_WIDTH = 1000
BOX_LENGTH = 100

dt = 0
past_collide_time = 0

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player_left.score == 1 or player_right.score == 1:
        player_left.position.y = surface.get_height()/2
        player_right.position.y = surface.get_height()/2
        ball.position.x = Ball.INITIAL_X_POSITION
        ball.position.y = Ball.INITIAL_Y_POSITION

        if player_left.score > player_right.score:
            winner = "left player"
        else:
            winner = "right player"

        final_statement = font.render("The winner is " + winner + " !", True, "red")
        final_statement_rect = final_statement.get_rect(center=(surface.get_width() / 2, surface.get_height() / 2))

    ball.position.x = ball.position.x + (ball.x_direction.value * ball.x_speed * dt)
    ball.position.y = ball.position.y + (ball.y_direction.value * ball.y_speed * dt)

    if ball.position.x <= 0 + BORDER_WIDTH:
        # update the score
        player_right.score += 1
        player_right_score = font.render(str(player_right.score), True, "white")
        # game reset
        ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))
    if ball.position.x >= surface.get_width() - BORDER_WIDTH:
        # update the score
        player_left.score += 1
        player_left_score = font.render(str(player_left.score), True, "white")
        # game reset
        ball = Ball(random.choice(list(BallXDirection)), random.choice(list(BallYDirection)))
    if ball.position.y <= 0 + Ball.RADIUS + BORDER_WIDTH + 5:
        ball.y_direction = BallYDirection(ball.y_direction.value * (-1))
    if ball.position.y >= surface.get_height() - Ball.RADIUS - BORDER_WIDTH - 5:
        ball.y_direction = BallYDirection(ball.y_direction.value * (-1))

    current_time = pygame.time.get_ticks()
    if player_left.rec.colliderect(ball.circle) and current_time > past_collide_time + 1000:
        past_collide_time = pygame.time.get_ticks()
        ball.y_direction = random.choice(list(BallYDirection))
        ball.x_direction = BallXDirection(ball.x_direction.value * (-1))
    if player_right.rec.colliderect(ball.circle) and current_time > past_collide_time + 1000:
        past_collide_time = pygame.time.get_ticks()
        ball.y_direction = random.choice(list(BallYDirection))
        ball.x_direction = BallXDirection(ball.x_direction.value * (-1))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_left.position.y > 0 + BORDER_WIDTH + 5:
        player_left.position.y -= Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_s] and player_left.position.y < surface.get_height() - Player.LENGTH - BORDER_WIDTH - 5:
        player_left.position.y += Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_UP] and player_right.position.y > 0 + BORDER_WIDTH + 5:
        player_right.position.y -= Player.PLAYER_VELOCITY * dt
    if keys[pygame.K_DOWN] and player_right.position.y < surface.get_height() - Player.LENGTH - BORDER_WIDTH - 5:
        player_right.position.y += Player.PLAYER_VELOCITY * dt

    surface.fill("black")
    pygame.draw.rect(surface, "white", pygame.Rect(0, 0, surface.get_width(), surface.get_height()), BORDER_WIDTH)

    surface.blit(player_left_score, player_left_score_rect)
    surface.blit(player_right_score, player_right_score_rect)

    ball.circle = pygame.draw.circle(surface, "white", (ball.position.x, ball.position.y), Ball.RADIUS * 2)
    player_left.rec = pygame.draw.rect(surface, "white", pygame.Rect(player_left.position.x, player_left.position.y, Player.WIDTH, Player.LENGTH))
    player_right.rec = pygame.draw.rect(surface, "white", pygame.Rect(player_right.position.x, player_right.position.y, Player.WIDTH, Player.LENGTH))

    if final_statement is not None:
        pygame.draw.rect(surface, "white", pygame.Rect((surface.get_width() - BOX_WIDTH) / 2, (surface.get_height() - BOX_LENGTH) / 2, BOX_WIDTH, BOX_LENGTH))
        surface.blit(final_statement, final_statement_rect)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)




'''
if player_left.score > player_right.score:
    winner = "left player"
else:
    winner = "right player"

final_statement = font.render(winner, True, "white")
final_statement_rect = final_statement.get_rect(center=(surface.get_width() / 2, surface.get_height()/2))
surface.blit(final_statement, final_statement_rect)

surface.fill("black")

print("IDK please work")
'''

# pygame.quit()
