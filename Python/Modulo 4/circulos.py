import pygame 
from pygame.locals import * 
from sys import exit 
import random 

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 , 32)
pygame.display.set_caption( "Jogo dos Círculos") 

desenhar_circulos = True    # ITEM B 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()

# ITEM B:  
        if event.type == KEYDOWN:
            if event.key == K_x:
                desenhar_circulos = False
            print(event)
        
    
    screen.fill((0, 0, 0))
            
# ITEM A:     
    if desenhar_circulos:
        for i in range(10):
            posicao = (random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]))
            raio = random.randint(10, 30)             
            cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))             
            pygame.draw.circle(screen, cor, posicao, raio)     
                
    pygame.display.update()
