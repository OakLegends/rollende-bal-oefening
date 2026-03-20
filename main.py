import pygame
from ball import Ball
from game_manager import GameManager

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Oefening 2 – Cirkel naar rechts")
clock = pygame.time.Clock()

ball = Ball(screen)

game_manager = GameManager(screen, clock, ball)
game_manager.main()

pygame.quit()