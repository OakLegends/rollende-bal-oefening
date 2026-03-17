import pygame


class GameManager:
    score = 0
    screen = None
    # Add a ball variable
    ball1 = None
    clock = None
    FPS = 30
    colors = []

    # Add the ball to the __init__ function.
    def __init__(self, score, screen, ball1, clock, colors):
        self.score = score
        self.screen = screen
        self.ball1 = ball1
        self.clock = clock
        self.FPS = 30
        self.colors = colors

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                # Add key input
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    self.ball1.move_down(self.ball1.velocity, self.screen)
                if keys[pygame.K_UP]:
                    self.ball1.move_up(self.ball1.velocity, self.screen)
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.colors[1])

            # Execute the draw_ball function
            self.ball1.draw_ball(self.screen)

            pygame.display.update()
            self.clock.tick(self.FPS)
            # When something is returned then check which player made the point.
            self.ball1.draw_ball(self.screen)
            pygame.display.update()
            self.clock.tick(self.FPS)
