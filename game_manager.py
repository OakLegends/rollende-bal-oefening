import pygame

class GameManager:
    screen = None
    clock = None
    FPS = 30
    colors = []

    def __init__(self, screen, clock, colors):
        self.screen = screen
        self.clock = clock
        self.FPS = 30
        self.colors = colors

    # Draw the line function
    def draw_circle(self):
        pygame.draw.circle(
            self.screen, (255, 0, 0), (300, 200), 50)
        pygame.display.update()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.colors[1])

            # Draw the line
            self.draw_circle()
            pygame.display.update()
            self.clock.tick(self.FPS)