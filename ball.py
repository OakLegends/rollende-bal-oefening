import pygame


class Ball:
    name = ""
    speed = 0
    velocity = 0
    isRight = False
    screen = None

    def __init__(self, name, speed, rect, velocity, isRight, screen):
        self.name = name
        self.speed = speed
        self.rect = rect
        self.velocity = velocity
        self.isRight = isRight
        self.screen = screen
        # Center the paddle
        self.rect.centery = self.screen.get_height() // 2
        self.centered = True
        # Set the paddle to the right side of the screen
        if self.isRight:
            self.rect.x = self.screen.get_width() - self.rect.width - 10

    def draw_ball(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (300, 200), 50)
        pygame.display.update()
        pygame.key.set_repeat(100, self.speed)

    def move_up(self, velocity, screen):
        screen.get_height() - self.rect.height
        # Setting the boundaries
        if self.rect.y > 10:
            self.rect.y -= velocity

    def move_down(self, velocity, screen):
        screen.get_height() - self.rect.height
        # Setting the boundaries
        if self.rect.y < screen.get_height() - self.rect.height - 10:
            self.rect.y += velocity
