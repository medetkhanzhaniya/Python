import pygame


pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Cubes game")

x=30
y=30
width=40
height=60
speed=3




isJump=False
jumpCount=10
 


clock=pygame.time.Clock()
run=False

while not run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
    if keys[pygame.K_RIGHT] and x<500-width-5:
        x+=speed 

    if not(isJump):
        if keys[pygame.K_UP]: y -= speed
        if keys[pygame.K_DOWN]: y += speed
        if keys[pygame.K_SPACE]: isJump=True
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

    


    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,255),(x,y,width,height))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()