import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#����surface����
screen = pygame.display.set_mode((640,480), 0, 32)

pygame.display.set_caption("Hello, World!")


background = pygame.image.load('sushiplate.jpg').convert()
mouse_cursor = pygame.image.load('fugu.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))

    x,y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor, (x,y))

    pygame.display.update()
