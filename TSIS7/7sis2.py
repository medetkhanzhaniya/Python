import time
import pygame
import math
import sys

width = 640
height = 480

color = pygame.Color(255, 255, 0, 0)
background_color = pygame.Color(0, 0, 0, 0)

pygame.init()
pygame.display.set_caption("SINE WAVE")
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

surface = pygame.Surface((width, height))
surface.fill(background_color)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
    surface.fill(background_color)
    speed = 2
    freq = 3
    amp = 40
    for x in range(width):
        y = int( (height / 2) + amp * math.sin(freq * ((float(x)/width) * (2 * math.pi) + (speed*time.time()))))
        
        surface.set_at((x, y), color)
    for x in range(width):
        y = int( (height / 2) + (amp + 40) * math.cos((freq + 5) * ((float(x)/width) * (2 * math.pi) + (speed*2*time.time()))))

        surface.set_at((x, y), color)
    screen.blit(surface, (0, 0))
    pygame.display.flip()