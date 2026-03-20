import pygame

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = screen.get_height() // 2
        self.radius = 50
        self.speed = 5              # positief = rechts, negatief = links

    def update(self):
        self.x += self.speed

        # Botsing rechterkant
        if self.x + self.radius > self.screen.get_width():
            self.speed = -self.speed   # richting omkeren

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)