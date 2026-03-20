import pygame

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100                # startpositie links
        self.y = screen.get_height() // 2
        self.radius = 50
        self.speed = 5              # snelheid naar rechts

    def update(self):
        self.x += self.speed        # bewegen naar rechts

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)