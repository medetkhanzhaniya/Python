import pygame

size = width, height = (1000, 1000)
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0)) # black


pygame.draw.rect(screen, (0, 100, 10), (20, 30, 100, 100), 1)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()