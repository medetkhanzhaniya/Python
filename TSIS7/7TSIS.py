import pygame
import math
import time

PI = math.pi
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800,450))
surface = pygame.Surface((600,318))

clock = pygame.time.Clock()
run = True
font = pygame.font.SysFont("times-new-roman",17,False,True)
font2 = pygame.font.SysFont("times-new-roman",22,False,True)
font3 = pygame.font.SysFont("times-new-roman",15,False,True)
x_txt = font2.render("X",True,BLACK)

y_points = (-1.00 ,-0.75 ,-0.50 ,-0.25 ,0.00 ,0.25 ,0.50 ,0.75 ,1.00)
points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
points1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
points2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(x_txt,(370,400))
    screen.blit(surface, (80, 22))
    for i in y_points:
        text = font.render(str(i),True,BLACK)
        screen.blit(text,(5,-i*159+170))
        pygame.draw.line(screen,BLACK,(50,-i*159+180),(705,-i*159+180))

    
    pygame.draw.line(screen,BLACK,(50,5),(50,360),3) #левая линия сурфейса y-axis
    pygame.draw.line(screen,BLACK,(705,5),(705,360),3)#правая сторона сурфейса  y-axis
    pygame.draw.line(screen,BLACK,(380,5),(380,360),3)# самый центр сурфейса y-axis
    
    pygame.draw.line(screen,BLACK,(50,5),(705,5),3)#верхняя сторона по x-axis
    pygame.draw.line(screen,BLACK,(50,360),(705,360),3)#самый низ сурфейса по x-axis
    pygame.draw.line(screen,BLACK,(50,180),(705,180),3)#центр по x-axis
    
    for i in range(6):
        pygame.draw.line(screen, BLACK, (i * 100 + 130, 5), (i * 100 + 130, 18))#делитель центр центр сверху x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 130, 360), (i * 100 + 130, 347))#делитель центр центр снизу x-axis

        pygame.draw.line(screen, BLACK, (i * 100 + 105, 360), (i * 100 + 105, 351))#делитель центр слева центра снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 105, 5), (i * 100 + 105, 14))#делитель центр  слева центра сверху x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 155, 360), (i * 100 + 155, 351))#делитель центр справа центра снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 155, 5), (i * 100 + 155, 14))#делитель центра справа центра серху x-axis

        pygame.draw.line(screen, BLACK, (i * 100 + 90, 360), (i * 100 + 90, 355))#делитель слева центра слева снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 90, 5), (i * 100 + 90, 10))#делитель слева центра слева сверху x-axis

        pygame.draw.line(screen, BLACK, (i * 100 + 120, 360), (i * 100 + 120, 355))#делитель слева большого центра снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 120, 5), (i * 100 + 120, 10))#делитель слева большого центра сверху x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 145, 360), (i * 100 + 145, 355))#делитель справа большого центра снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 145, 5), (i * 100 + 145, 10))#делитель справа большого центра сверху x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 170, 360), (i * 100 + 170, 355))#делитель справа центра справа снизу x-axis
        pygame.draw.line(screen, BLACK, (i * 100 + 170, 5), (i * 100 + 170, 10))#делитель справа центра справа сверху x-axis
    
    for i in range(7):
        pygame.draw.line(screen, BLACK, (i*100+80, 5), (i*100+80, 360))#линии на y axis где начинается синкос

    for i in range(8):                 #левая сторона сурфейса y-axis
        pygame.draw.line(screen, BLACK, (50, i * 40 + 40), (65, i * 40 + 40))#делитель с левой стороны которая по середине 
        pygame.draw.line(screen, BLACK, (50, i * 40 + 30), (60, i * 40 + 30))#делитель справа центра 
        pygame.draw.line(screen, BLACK, (50, i * 40 + 50), (60, i * 40 + 50))#делитель слева от центра 
                                    #правая сторона сурфейса y-axis
        pygame.draw.line(screen, BLACK, (705, i * 40 + 40), (690, i * 40 + 40))#центр делителя 
        pygame.draw.line(screen, BLACK, (705, i * 40 + 30), (695, i * 40 + 30))#делитель справа
        pygame.draw.line(screen, BLACK, (705, i * 40 + 50), (695, i * 40 + 50))#делитель слева

    
    for x in range(80, 700, 50):
        screen.blit(font.render(points[(x - 80) // 50], False, BLACK), (x - 10, 365))
        screen.blit(font.render(points1[(x - 80) // 50], False, BLACK), (x - 20, 365))
        screen.blit(font.render(points2[(x - 80) // 50], False, BLACK), (x - 10, 385))

    screen.blit(font3.render('sin(x)', False, BLACK), (475, 23))
    screen.blit(font3.render('cos(x)', False, BLACK), (475, 43))

    pygame.draw.line(screen, WHITE, (480,22), (480, 59 ))

    pygame.draw.line(screen, RED, (520, 33), (560, 33))
    for x in range(520, 560, 7):
        pygame.draw.line(screen, BLUE, (x, 50), (x + 3, 50))

#python jai.py

    surface.fill((WHITE))
    width=600
    height=318
    speed = 0.5
    freq = 1
    amp = 120
    
    for x in range(width):
        y = int( (height / 2) + (amp+40) * math.sin((freq+2) * ((float(x)/width) * (2 * PI) + (speed*time.time()))))
        surface.set_at((x, y), RED)
        
    for x in range(width):
        y = int( (height / 2) + (amp+40) * math.cos((freq+2) * ((float(x)/width) * (2 * PI) + (speed*time.time()))))
        surface.set_at((x, y), BLUE)
        surface.set_at((x-1, y), BLUE)
        
    pygame.display.flip()
    clock.tick(100)