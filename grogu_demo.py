

import pygame

pygame.init()
screen=pygame.display.set_mode((600,500),pygame.RESIZABLE)
pygame.display.set_caption('I am grogu')
screen.fill("white")

grogu=pygame.image.load("I AM GROGU.png")


stop=True



while stop:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            stop=False

    screen.blit(grogu,(10,0))

    pygame.display.update()