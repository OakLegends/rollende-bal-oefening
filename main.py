import pygame
from ball import Ball
from game_manager import GameManager

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Cirkel met achtergrond + kleurverandering")
clock = pygame.time.Clock()

# Probeer een achtergrondafbeelding te laden
try:
    background = pygame.image.load("space.png")          # ← verander dit naar jouw bestandsnaam
    background = pygame.transform.scale(background, screen.get_size())
except pygame.error:
    print("Kon achtergrond.jpg niet laden → gebruik effen zwart scherm")
    background = None

ball = Ball(screen)

game_manager = GameManager(screen, clock, ball, background)
game_manager.main()

pygame.quit()