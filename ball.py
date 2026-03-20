import pygame

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = screen.get_height() // 2
        self.radius = 50
        self.speed_x = 5            # x-richting
        self.speed_y = 4            # y-richting (ook beweging omhoog/omlaag)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        w = self.screen.get_width()
        h = self.screen.get_height()

        # Rechts / links
        if self.x + self.radius > w:
            self.x = w - self.radius
            self.speed_x = -self.speed_x
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.speed_x = -self.speed_x

        # Onder / boven
        if self.y + self.radius > h:
            self.y = h - self.radius
            self.speed_y = -self.speed_y
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)