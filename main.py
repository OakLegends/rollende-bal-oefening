import pygame
from ball import Ball
from game_manager import GameManager

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Rode Cirkel Bewegen')
clock = pygame.time.Clock()

# Maak de rode bal (cirkel)
ball = Ball(
    name='player',
    x=100,                  # start links
    y=screen.get_height() // 2,
    radius=30,
    velocity=8,
    isRight=False,
    screen=screen
)

# Game manager starten
game_manager = GameManager(
    score=0,
    screen=screen,
    ball=ball,
    clock=clock,
    colors=[(255, 255, 255), (0, 0, 0)]   # wit + zwart
)

game_manager.main()

pygame.quit()