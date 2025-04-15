import pygame
from pygame.locals import *
from sys import exit
import random

# Inicialização do Pygame
pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Círculos Aleatórios")

# Controla se os círculos devem continuar sendo desenhados
desenhar_circulos = True  # <-- Usado no item (b)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # Item (b): Verifica se a tecla X foi pressionada
        if event.type == KEYDOWN:
            if event.key == K_x:
                desenhar_circulos = False  # Para de desenhar novos círculos
        print(event)

    # Preenche o fundo com preto a cada frame
    screen.fill((0, 0, 0))

    # Item (a): Desenha círculos em posições aleatórias
    if desenhar_circulos:
        for _ in range(10):  # desenha 10 círculos por frame
            posicao = (random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]))
            raio = random.randint(10, 30)
            cor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pygame.draw.circle(screen, cor, posicao, raio)

    pygame.display.update()
