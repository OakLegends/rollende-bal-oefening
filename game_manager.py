import pygame

class GameManager:
    def __init__(self, screen, clock, ball):
        self.screen = screen
        self.clock = clock
        self.ball = ball
        self.font = pygame.font.SysFont("segoeui", 28)

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ball.increase_speed()
                    elif event.key == pygame.K_DOWN:
                        self.ball.decrease_speed()

            self.ball.update()

            self.screen.fill((12, 12, 28))  # iets donkerder blauwzwart

            self.ball.draw()

            # Toon huidige snelheid (totaal)
            total_speed = abs(self.ball.speed_x) + abs(self.ball.speed_y)
            text = self.font.render(f"Snelheid: {total_speed:.1f}", True, (220, 220, 240))
            self.screen.blit(text, (20, 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()