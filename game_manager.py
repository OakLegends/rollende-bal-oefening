import pygame


class GameManager:
    def __init__(self, score, screen, ball, clock, colors):
        self.score = score
        self.screen = screen
        self.ball = ball
        self.clock = clock
        self.colors = colors  # [achtergrond, tekst/lijnen?]

    def main(self):
        running = True

        while running:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Toetsen indrukken (kan meerdere tegelijk)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.ball.move_up()
            if keys[pygame.K_DOWN]:
                self.ball.move_down()

            # Scherm wissen
            self.screen.fill(self.colors[1])  # zwart

            # Bal tekenen
            self.ball.draw()

            # Scherm updaten
            pygame.display.flip()

            # Limiteer framerate
            self.clock.tick(60)

        pygame.quit()