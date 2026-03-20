import pygame

class GameManager:
    def __init__(self, screen, clock, ball):
        self.screen = screen
        self.clock = clock
        self.ball = ball

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.ball.update()

            self.screen.fill((0, 0, 0))
            self.ball.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()