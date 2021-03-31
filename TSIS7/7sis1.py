import pygame
import sys
import math
pygame.init()
screen = pygame.display.set_mode([840, 840])

points = []
screen.fill([0, 0, 0])
n = 10
A = 200
for x in range(840):
    y = int(math.cos(x / 840. * n * math.pi) * A + 240)
    points.append([x, y])
pygame.draw.lines(screen, [255, 255, 255], False, points, 3)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()