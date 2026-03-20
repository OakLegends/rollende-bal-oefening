import pygame


class Ball:
    def __init__(self, name, x, y, radius, velocity, isRight, screen):
        self.name = name
        self.radius = radius
        self.velocity = velocity
        self.isRight = isRight
        self.screen = screen

        # Maak een rect die groot genoeg is om de cirkel te omvatten
        self.rect = pygame.Rect(0, 0, radius * 2, radius * 2)

        # Startpositie
        self.rect.centerx = x
        self.rect.centery = y

        # Als het de rechter paddle moet zijn (voor later)
        if self.isRight:
            self.rect.centerx = screen.get_width() - 80

    def draw(self):
        # Teken een rode cirkel op de huidige positie
        pygame.draw.circle(self.screen, (255, 0, 0), self.rect.center, self.radius)

    def move_up(self):
        if self.rect.top > 10:
            self.rect.y -= self.velocity

    def move_down(self):
        if self.rect.bottom < self.screen.get_height() - 10:
            self.rect.y += self.velocity