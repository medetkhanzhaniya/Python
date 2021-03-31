import pygame

pygame.init()
screen=pygame.display.set_mode((500,500)) 
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pygame.draw.rect(screen ,(255,255,255), pygame.Rect(30,30,400,400),2)
    pygame.display.flip()
    screen.fill((0,0,0))


    pygame.display.flip()