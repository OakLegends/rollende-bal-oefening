import pygame
import game_manager

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')

# Define FPS
clock = pygame.time.Clock()
FPS = 30

# Create a game manager object
game_manager = game_manager.GameManager(screen, clock, colors=[(0, 255, 255), (0, 0, 0)])
game_manager.main()