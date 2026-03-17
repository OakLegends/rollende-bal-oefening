import pygame
import game_manager
import ball

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
FPS = 30

# Add the 2 padles to the game manager
ball1 = ball.Ball('player', 10, pygame.Rect(10, 10, 10, 100), 10, False, screen)
game_manager = game_manager.GameManager(
    0, screen, ball1, clock, colors=[(255, 255, 255), (0, 0, 0)])
game_manager.main()
