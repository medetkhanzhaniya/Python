import pygame, sys
from pygame.locals import*
import random , time

pygame.init()
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE1 = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 55) #шрифт
font2 = pygame.font.SysFont("Verdana", 40) #шриф
font_small = pygame.font.SysFont("Verdana", 20)  #шрифт 
game_over = font.render("Game Over", True, BLACK) #слово в конце игре 
text = font2.render('Score: '+ str(SCORE1),True,BLACK) 
background = pygame.image.load('AnimatedStreet.png') # фотка на заднем фоне 
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600)) #размер окна
DISPLAYSURF.fill(WHITE) #окно заполняем белым 
pygame.display.set_caption("Game") #название игры гэйм 
 
class Enemy(pygame.sprite.Sprite):
      def speed_en(self):
          return random.randint(1,5)
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('Enemy.png') #загружаем фотку противника 
        self.surf = pygame.Surface((42, 70)) #размер энеми 
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))#
        self.speed=self.speed_en()
      def move(self): #движение энеми 
        global SCORE
        self.rect.move_ip(0,self.speed)


        if (self.rect.top > 600): #если верхняя часть врага достигла конца экрана
            SCORE += 1  #скор прибовляет 1
            self.rect.top = 0   #и его сбрасывает на начало экрана 
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)# на рандомное место по оси Х
            self.speed=self.speed_en()
 
 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('coin.png')
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
 
    
    def move(self):
        global SCORE1
        self.rect.move_ip(0,2)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        if pygame.sprite.spritecollideany(P1,coins):
            pygame.mixer.Sound('eat.ogg').play()
            time.sleep(0.5)
            SCORE1 += 1
            self.rect.top = 0
            self.speed = random.randint(1,5)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('Player.png')
        self.surf = pygame.Surface((40, 75))

        self.rect = self.surf.get_rect(center = (160, 520))#игрок появляется в нижней части экрана
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
M1 = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)
coins = pygame.sprite.Group()
coins.add(M1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED = random.randint(1,5)     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))


    scores1 = font_small.render(str(SCORE1), True, RED)
    DISPLAYSURF.blit(scores1, (350,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          DISPLAYSURF.blit(text, (30,310))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()    


    if pygame.sprite.spritecollideany(P1 , coins):
        coins.top=0
        SCORE1 += 1
        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
    #python 8tsis.py