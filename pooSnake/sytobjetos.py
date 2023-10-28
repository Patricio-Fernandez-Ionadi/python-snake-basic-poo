import pygame
import random

vec2 = pygame.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = self.game.SIZE
        self.rect = pygame.rect.Rect([0, 0, self.size, self.size])
        self.set_rnd = game.RESOLUTION // self.size
        self.rect.center = self.get_rnd()
        self.direction = vec2(0, 0)
        self.long = 1
        self.sections = []
        self.directions = {
            pygame.K_UP: 1,
            pygame.K_DOWN: 1,
            pygame.K_LEFT: 1,
            pygame.K_RIGHT: 1,
        }

    def read_keyboard(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.directions[pygame.K_UP]:
                self.direction = vec2(0, -self.size)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 0,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 1,
                }
            if event.key == pygame.K_DOWN and self.directions[pygame.K_DOWN]:
                self.direction = vec2(0, self.size)
                self.directions = {
                    pygame.K_UP: 0,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 1,
                }
            if event.key == pygame.K_LEFT and self.directions[pygame.K_LEFT]:
                self.direction = vec2(-self.size, 0)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 1,
                    pygame.K_RIGHT: 0,
                }
            if event.key == pygame.K_RIGHT and self.directions[pygame.K_RIGHT]:
                self.direction = vec2(self.size, 0)
                self.directions = {
                    pygame.K_UP: 1,
                    pygame.K_DOWN: 1,
                    pygame.K_LEFT: 0,
                    pygame.K_RIGHT: 1,
                }

    def get_rnd(self):
        return [
            random.randrange(self.set_rnd) * self.size + self.size // 2,
            random.randrange(self.set_rnd) * self.size + self.size // 2,
        ]

    def check_limits(self):
        if self.rect.left < 0 or self.rect.right > self.game.RESOLUTION:
            self.game.new_game()

        if self.rect.top < 0 or self.rect.bottom > self.game.RESOLUTION:
            self.game.new_game()

    def check_eatapple(self):
        if self.rect.center == self.game.apple.rect.center:
            self.game.apple.rect.center = self.get_rnd()
            self.long +=1
            self.game.score += 1

    def check_autocollision(self):
        if len(self.sections) != len(set(segment.center for segment in self.sections)):
            self.game.new_game()

    def move_snake(self):
        self.rect.move_ip(self.direction)
        self.sections.append(self.rect.copy())
        self.sections = self.sections[-self.long:]

    def update(self):
        self.move_snake()
        self.check_autocollision()
        self.check_limits()
        self.check_eatapple()

    def draw(self):
        for section in self.sections:
            pygame.draw.rect(self.game.SCREEN, self.game.c['GREEN'], section)


class Apple:
    def __init__(self, game):
        self.game = game
        self.size = self.game.SIZE
        self.rect = pygame.rect.Rect([0, 0, self.size, self.size])
        self.rect.center = self.game.snake.get_rnd()

    def draw(self):
        pygame.draw.circle(self.game.SCREEN, self.game.c['RED'],
                           self.rect.center, self.size // 2)
