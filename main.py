import pygame
from ball import Ball
from game_manager import GameManager

pygame.init()
pygame.mixer.init()   # belangrijk voor geluid

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Cirkel met achtergrond + kleur + geluid")
clock = pygame.time.Clock()

# Achtergrond proberen laden
try:
    background = pygame.image.load("space.png")
    background = pygame.transform.scale(background, screen.get_size())
except pygame.error:
    print("Geen achtergrond.jpg gevonden → effen scherm")
    background = None

# Geluid laden
try:
    collision_sound = pygame.mixer.Sound("Hemelvaart.wav")   # ← verander naar jouw bestandsnaam
except pygame.error:
    print("Geen bounce.wav gevonden → geluid uitgeschakeld")
    collision_sound = None

ball = Ball(screen, collision_sound=collision_sound)

game_manager = GameManager(screen, clock, ball, background)
game_manager.main()

pygame.quit()