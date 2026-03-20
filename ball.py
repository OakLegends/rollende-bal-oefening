import pygame


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = screen.get_height() // 2
        self.radius = 50

        self.speed_x = 5.0  # x-richting snelheid
        self.speed_y = 4.0  # y-richting snelheid

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

    def increase_speed(self):
        self.speed_x *= 1.15
        self.speed_y *= 1.15

    def decrease_speed(self):
        self.speed_x *= 0.88
        self.speed_y *= 0.88
        # voorkom dat hij bijna stil komt te staan
        if abs(self.speed_x) < 0.4:
            self.speed_x = 0.4 if self.speed_x > 0 else -0.4
        if abs(self.speed_y) < 0.4:
            self.speed_y = 0.4 if self.speed_y > 0 else -0.4

    def get_color(self):
        # Totale snelheid = som van absolute snelheden
        total_speed = abs(self.speed_x) + abs(self.speed_y)

        if total_speed > 18:
            return 255, 40, 40  # fel rood – heel snel
        elif total_speed > 12:
            return 255, 120, 0  # oranje
        elif total_speed > 8:
            return 220, 220, 60  # geel
        elif total_speed > 5:
            return 80, 220, 80  # groen
        else:
            return 100, 140, 255  # blauw – langzaam

    def draw(self):
        color = self.get_color()
        pygame.draw.circle(self.screen, color, (int(self.x), int(self.y)), self.radius)