import pygame
import sys
from sytobjetos import *


class Game:
    def __init__(self):
        pygame.init()
        self.c = { 
            'BLUE' : (0, 0, 90),
            'YELLOW' : (220, 190, 0),
            'WHITE' : (240, 240, 240),
            'GREY' : (50, 50, 50),
            'RED' : (230, 0, 0),
            'GREEN' : (0, 230, 0),
            'GREEN_L' : (0, 150, 0),  
          }
        self.gameover = False
        self.RESOLUTION = 600
        self.FPS = 10
        self.SIZE = 40
        self.SCREEN = pygame.display.set_mode((self.RESOLUTION,self.RESOLUTION))
        # self.SCREEN = pygame.display.set_mode([self.RESOLUTION] * 2)
        self.CLOCK = pygame.time.Clock()
        self.new_game()

    def draw_grid(self):
        for x in range(0, self.RESOLUTION, self.SIZE):
            pygame.draw.line(self.SCREEN, self.c['GREY'], (x, 0), (x, self.RESOLUTION))

        for y in range(0, self.RESOLUTION, self.SIZE):
            pygame.draw.line(self.SCREEN, self.c['GREY'], (0, y), (self.RESOLUTION, y))

    def draw_text(self, surface, text, size, x, y):
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(text, True, self.c['YELLOW'])
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

    def new_game(self):
        self.score = 0
        self.snake = Snake(self)
        self.apple = Apple(self)

    def update(self):
        pygame.display.flip()
        self.CLOCK.tick(self.FPS)
        self.snake.update()

    def draw(self):
        self.SCREEN.fill(self.c['BLUE'])
        self.draw_grid()
        self.apple.draw()
        self.snake.draw()
        self.draw_text(self.SCREEN, f'Apples: {str(self.score)}', 25, self.RESOLUTION // 2, 10)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.snake.read_keyboard(event)

    def run(self):
        while not self.gameover:
            self.check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
