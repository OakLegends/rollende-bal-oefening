import pygame


class Ball:
    def __init__(self, screen, collision_sound=None):
        self.screen = screen
        self.collision_sound = collision_sound

        self.x = 100
        self.y = screen.get_height() // 2
        self.radius = 50

        self.speed_x = 5.0
        self.speed_y = 4.0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        w = self.screen.get_width()
        h = self.screen.get_height()

        collided = False

        # Rechts / links
        if self.x + self.radius > w:
            self.x = w - self.radius
            self.speed_x = -self.speed_x
            collided = True
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.speed_x = -self.speed_x
            collided = True

        # Onder / boven
        if self.y + self.radius > h:
            self.y = h - self.radius
            self.speed_y = -self.speed_y
            collided = True
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.speed_y = -self.speed_y
            collided = True

        # Geluid afspelen als er een botsing was
        if collided and self.collision_sound is not None:
            self.collision_sound.play()

    def increase_speed(self):
        self.speed_x *= 1.15
        self.speed_y *= 1.15

    def decrease_speed(self):
        self.speed_x *= 0.88
        self.speed_y *= 0.88
        if abs(self.speed_x) < 0.4:
            self.speed_x = 0.4 if self.speed_x > 0 else -0.4
        if abs(self.speed_y) < 0.4:
            self.speed_y = 0.4 if self.speed_y > 0 else -0.4

    def get_color(self):
        total_speed = abs(self.speed_x) + abs(self.speed_y)
        if total_speed > 18:
            return 255, 40, 40
        elif total_speed > 12:
            return 255, 120, 0
        elif total_speed > 8:
            return 220, 220, 60
        elif total_speed > 5:
            return 80, 220, 80
        else:
            return 100, 140, 255

    def draw(self):
        color = self.get_color()
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), self.radius)