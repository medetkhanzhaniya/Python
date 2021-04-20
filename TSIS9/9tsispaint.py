import pygame 
pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0) 
WHITE = (255,255,255)
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h], 4)

def drawCircle(surface, color, x, y,radius):
    pygame.draw.circle(surface, color, (x, y), radius, 2)

def drawLine(surface, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(surface, color, (x, y), radius)
        
def erase(surface, x, y,radius):
    pygame.draw.circle(surface, WHITE, (x, y), radius)
# 0 - pencil, 1 - rectangle, 2 - circle, 3 - eraser
# E - take screenshot, W - increse RADIUS, S - decrease RADIUS, N - change tool
isPressed = False
rgb = pygame.image.load("rgb.jpg")
currentTool = 0
toolCount = 4
color = WHITE
radius = 20
done = False
isPressed = False
screen.fill(WHITE)
while not done:
    screen.blit(rgb, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            if event.key == pygame.K_w:
                if radius < 100:
                    radius += 1
            if event.key == pygame.K_s:
                if radius > 1:
                    radius -= 1
            if event.key == pygame.K_e:
                pygame.image.save(screen, 'screenshot.jpg')
        if event.type == pygame.MOUSEBUTTONDOWN:
            curPoint = pygame.mouse.get_pos()
            if currentTool == 0:
                pygame.draw.circle(screen,color , event.pos, radius)
                isPressed = True
            elif currentTool == 1:
                drawRectangle(screen, color, event.pos[0],event.pos[1], radius * 2, radius * 2)
                isPressed = True
            elif currentTool == 2:
                drawCircle(screen, color, event.pos[0], event.pos[1],radius)
                isPressed = True
            elif currentTool == 3:
                erase(screen, event.pos[0],event.pos[1],radius)
                isPressed = True    
        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            mouse_pos = pygame.mouse.get_pos()
            if 0 < mouse_pos[0] < 500 and 0 < mouse_pos[1] < 55:
                color = screen.get_at(mouse_pos)
        if event.type == pygame.MOUSEMOTION and isPressed == True:
            if currentTool == 0:
                pygame.draw.circle(screen, color, event.pos, radius)
                drawLine(screen, color, event.pos, curPoint,  radius)
                curPoint = event.pos
            elif currentTool == 1:
                drawRectangle(screen, color, event.pos[0],event.pos[1], radius * 2, radius * 2)
            elif currentTool == 2:
                drawCircle(screen, color, event.pos[0], event.pos[1],radius)
            elif currentTool == 3:
                erase(screen, event.pos[0],event.pos[1],radius)
        if event.type == pygame.QUIT:
            done = True        
    pygame.display.flip()