import pygame
import random

RESOLUCION = (1000, 600)
FPS = 10

AZUL_OSC = (0, 0, 90)
BLANCO = (240, 240, 240)
ROJO = (230, 0, 0)
VERDE = (0, 230, 0)
VERDE_C = (0, 150, 0)


class CachoSnake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 40
        self.posxy = (self.x, self.y)
        self.direccion = 'derecha'
        self.snake = []

    def leer_teclado(self):
        lita_teclas = pygame.key.get_pressed()
        if lita_teclas[pygame.K_RIGHT]:
            self.direccion = 'derecha'
        if lita_teclas[pygame.K_LEFT]:
            self.direccion = 'izquierda'
        if lita_teclas[pygame.K_UP]:
            self.direccion = 'arriba'
        if lita_teclas[pygame.K_DOWN]:
            self.direccion = 'abajo'

    def hacia_donde(self):
        if self.direccion == 'derecha':
            self.x += 1 * self.ancho
        if self.direccion == 'izquierda':
            self.x -= 1 * self.ancho
        if self.direccion == 'arriba':
            self.y -= 1 * self.ancho
        if self.direccion == 'abajo':
            self.y += 1 * self.ancho

        self.posxy = (self.x, self.y)

    def seguir_cabeza(self):
        for i in range(len(self.snake)):
            if i != 0:
                crecer = len(self.snake) - i
                self.snake[crecer] = self.snake[crecer - 1]


class Manzana():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 40
        self.posxy = (self.x, self.y)

    def otra_manzana(self):
        self.x = random.randrange(
            RESOLUCION[0] // self.ancho - 1) * self.ancho  # // => division
        self.y = random.randrange(RESOLUCION[1] // self.ancho - 1) * self.ancho
        self.posxy = (self.x, self.y)


pygame.init()

pantalla = pygame.display.set_mode(RESOLUCION)
reloj = pygame.time.Clock()

cachoSnake = CachoSnake(40, 40)
cachoSnake.snake.append(cachoSnake.posxy)

manzana = Manzana(0, 0)
manzana.otra_manzana()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    cachoSnake.leer_teclado()
    cachoSnake.hacia_donde()
    cachoSnake.snake[0] = cachoSnake.posxy

    pantalla.fill(AZUL_OSC)

    rectManzana = (manzana.x + manzana.ancho // 2,
                   manzana.y + manzana.ancho // 2)
    dibuja_manzana = pygame.draw.circle(
        pantalla, ROJO, rectManzana, manzana.ancho // 2)

    contador = 0
    for i in cachoSnake.snake:
        if contador == 0:
            rectSnake = (i[0], i[1], cachoSnake.ancho, cachoSnake.ancho)
            dibuja_snake_cabeza = pygame.draw.rect(
                pantalla, VERDE_C, rectSnake)
        else:
            rectSnake = (i[0], i[1], cachoSnake.ancho, cachoSnake.ancho)
            dibuja_snake = pygame.draw.rect(pantalla, VERDE_C, rectSnake)
            if cachoSnake.snake[0] == cachoSnake.snake[contador]:
                run = False
        contador += 1

    if manzana.posxy == cachoSnake.snake[0]:
        manzana.otra_manzana()
        cachoSnake.snake.append(cachoSnake.posxy)
    cachoSnake.seguir_cabeza()

    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()
