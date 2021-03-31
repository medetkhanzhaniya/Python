import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

walkRight=[pygame.image.load('pygame_right_1.png'),
pygame.image.load('pygame_right_2.png'),pygame.image.load('pygame_right_3.png'),
pygame.image.load('pygame_right_4.png'),pygame.image.load('pygame_right_5.png'),
pygame.image.load('pygame_right_6.png')]

walkLeft=[pygame.image.load('pygame_left_1.png'),
pygame.image.load('pygame_left_2.png'),pygame.image.load('pygame_left_3.png'),
pygame.image.load('pygame_left_4.png'),pygame.image.load('pygame_left_5.png'),
pygame.image.load('pygame_right_6.png')]

bg=pygame.image.load('pygame_bg.jpg')
playerStand=pygame.image.load('pygame_idle.png')

clock=pygame.time.Clock()

done = False
is_blue = True
x = 30
y = 30

BLACK = (0, 0, 0)
isJump=False
jumpCount=10


left=False
right=False
animCount=0

def drawWindow():
    global animCount
    #screen.fill(BLACK)
    screen.blit(bg,(0,0))
    if animCount+1>=30:
        animCount=0

    if left:
        screen.blit(walkLeft[animCount // 5 ], (x,y))
        animCount+=1
    elif right:
        screen.blit(walkRight[animCount // 5 ], (x,y))
        animCount+=1
    else:
        screen.blit(playerStand, (x,y))

    pygame.display.update()


clock=pygame.time.Clock()
while not done:
        clock.tick(30)
        pygame.time.delay(50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_LEFT]: 
            x -= 3
            left=True
            right=False
        elif pressed[pygame.K_RIGHT]: 
            x += 3
            left=False
            right=True
        else:
            left=False
            right=False
            animCount=0

        if not(isJump):
            if pressed[pygame.K_UP]: y -= 3
            if pressed[pygame.K_DOWN]: y += 3
            if pressed[pygame.K_SPACE]: isJump=True
        else:
            if jumpCount>=-10:
                if jumpCount<0:
                    y+=(jumpCount**2)/2 
                else:
                    y-=(jumpCount**2)/2
                jumpCount-=1
            else: 
                isJump=False 
                jumpCount=10

        drawWindow()
        pygame.display.flip()
        screen.fill((0,0,0))
        clock.tick(60)