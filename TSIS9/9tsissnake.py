import pygame, sys 
import random
import time
import pygame_menu
WIDTH = 800
HEIGHT = 600
run = True 
pygame.init()
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont('Verdana', 50)
font1 = pygame.font.SysFont('Verdana', 20)
FPS = 30
clock = pygame.time.Clock()
wall_points = []


def op():

    global run
    class Snake: 
        def __init__(self):
            self.size = 3
            self.radius = 10
            self.dx = 5
            self.dy = 0
            self.elements = [[100, 100], [120, 100], [140, 100]]
            self.score = 0
            self.is_add = False

        def draw(self): 
            for element in self.elements:
                pygame.draw.circle(screen, (139,69, 19), element, self.radius)
        def add_snake(self):
            self.size += 1
            self.score += 1
            self.elements.append([0, 0])
            self.is_add = False


        def move(self):
            if self.is_add:
                self.add_snake()
            for i in range(self.size -1, 0, -1):
                self.elements[i][0]=self.elements[i-1][0]
                self.elements[i][1]=self.elements[i-1][1]
            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy


    class Food:
        def __init__(self):
            self.x = random.randint(100, 700)
            self.y = random.randint(100, 500)
            self.image = pygame.image.load("apple.png")

        def draw(self):
            screen.blit(self.image, (self.x, self.y))


    def show_score(x, y, score):
        show = font1.render('Score' + str(score), True, (0,0,0),)
        screen.blit(show, (x, y))

    def collision():
        if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1]) ):
            snake.is_add = True 
            food.x = random.randint(100, 700)
            food.y = random.randint(100, 500)

    def show_walls():
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (768, i))

    def is_in_walls():
        return snake.elements[0][0] > 770  or snake.elements[0][0] < 30 or  snake.elements[0][1] > 570  or snake.elements[0][1] < 30
    def check_wall(wall_points, snake_list):
        for wall_point in wall_points:
            for snake_point in snake_list:
                if wall_point[0] == snake_point[0] and wall_point[1] == snake_point[1]:
                    game_over()
    def game_over():
        screen.fill((255, 255, 255))
        txt = font.render('Game over', True, (25, 25, 112))
        my_score = font.render('Total score: ' + str(snake.score), True, (135,206,135))
        screen.blit(my_score, (300, 250))
        screen.blit(txt, (300, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
    wall_image = pygame.image.load("walls.png")
    snake = Snake() 
    food = Food()
    while run: 
        mil = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 5
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -5
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -5
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 5
        if is_in_walls():
            game_over()
            run = False
        collision()
        screen.fill((173, 255, 47))
        snake.move()
        snake.draw()
        #show_walls()
        
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (768, i))
            wall_points.append((i,0))
            wall_points.append((i, 570))
            wall_points.append((0, i))
            wall_points.append((768, i))
        check_wall(wall_points, snake.elements)
        food.draw()
        show_score(0, 0, snake.score)
        pygame.display.flip()

    pass



def set_difficulty(value,difficulty):
    pass


def tp():
        
    class Snake:
        def __init__(self):
            self.size = 3
            self.radius = 10
            self.dx = 5
            self.dy = 0
            self.elements = [[100, 100], [120, 100], [140, 100]]
            self.score = 0
            self.is_add = False

        def draw(self):
            for element in self.elements:
                pygame.draw.circle(screen, (139,69,19), element, self.radius)
        def add_snake(self):
            self.size += 1
            self.score += 1
            self.elements.append([0, 0])
            self.is_add = False

        def move(self):
            if self.is_add:
                self.add_snake()
            for i in range(self.size - 1, 0, -1):
                self.elements[i][0] = self.elements[i - 1][0]
                self.elements[i][1] = self.elements[i - 1][1]
            
            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy

    class Food:
        def __init__(self):
            self.x = random.randint(100, 700)
            self.y = random.randint(100, 500)
            self.image = pygame.image.load("apple.png")
            
        
        def draw(self):
            screen.blit(self.image, (self.x, self.y))

    def show_score(x, y, score):
        show = font1.render('Score: ' + str(score), True, (0,0,0))
        screen.blit(show, (x, y))

    def collision():
        if(food.x in range(snake1.elements[0][0] - 20, snake1.elements[0][0])) and (food.y in range(snake1.elements[0][1] - 20, snake1.elements[0][1])):
            snake1.is_add = True
            food.x = random.randint(50, 700)
            food.y = random.randint(50, 500)
        if(food.x in range(snake2.elements[0][0] - 20, snake2.elements[0][0])) and (food.y in range(snake2.elements[0][1] - 20, snake2.elements[0][1])):
            snake2.is_add = True
            food.x = random.randint(50, 700)
            food.y = random.randint(50, 500)

    def is_in_walls():
        return snake1.elements[0][0] > 770 or snake1.elements[0][0] < 30  or  snake1.elements[0][1] > 570  or snake1.elements[0][1] < 30 
    def is_in_walls2():
        return snake2.elements[0][0] > 570 or snake2.elements[0][0] < 30  or  snake2.elements[0][1] > 570  or snake2.elements[0][1] < 30 

    def game_over():
        screen.fill((255, 255, 255))
        txt = font.render('Game over', True, (255, 0,0 ))
        my_score = font.render('Total score1: ' + str(snake1.score), True, (25, 25, 112))
        my_score2 = font.render('Total score2: ' + str(snake2.score), True, (135, 206, 135))
        screen.blit(txt, (250, 150))
        screen.blit(my_score, (250, 250))
        screen.blit(my_score2, (250, 200))
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()
    wall_image = pygame.image.load('walls.png')
    def show_walls():
        for i in range(0, WIDTH, 15):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, HEIGHT - 32))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (WIDTH - 32, i))
    d=5
    snake1 = Snake()
    snake2 = Snake()
    run = True
    food = Food()
  
    while run:
        mil = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d

                if event.key == pygame.K_d and snake2.dx != -d:
                    snake2.dx = d
                    snake2.dy = 0
                if event.key == pygame.K_a and snake2.dx != d:
                    snake2.dx = -d
                    snake2.dy = 0
                if event.key == pygame.K_w and snake2.dy != d:
                    snake2.dx = 0
                    snake2.dy = -d
                if event.key == pygame.K_s and snake2.dy != -d:
                    snake2.dx = 0
                    snake2.dy = d
        
        if is_in_walls():
            game_over()
            run = False
        if is_in_walls2():
            game_over()
            run = False

        collision()
        screen.fill((173,255,47))
        snake1.move()
        snake1.draw()
        snake2.move()
        snake2.draw()
        food.draw()
        show_score(35, 45, snake1.score)
        show_score(450, 45, snake2.score)
        show_walls()
        pygame.display.flip()
    pass

def easy():
        
    class Food:
        def __init__(self):
            self.x = random.randint(0, 800)
            self.y = random.randint(0, 600)

        def gen(self):
            self.x = random.randint(0, 800)
            self.y = random.randint(0, 600)

        def draw(self):
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))
   
   

    class Snake:
        def __init__(self, x, y):
            self.size = 1
            self.elements = [[x, y]]
            self.radius = 10
            self.dx = 5 # right
            self.dy = 0
            self.is_add = False
            self.speed = 20


        # [x1, y1], [x2, y2], [x3, y3], [x3, y3], [x4, y4] i -> i - 1

        def draw(self):
            for element in self.elements:
                pygame.draw.circle(screen, (139,69, 19), element, self.radius)

        def add_to_snake(self):
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False
            if self.size % 3 == 0:
                self.speed += 10

        def move(self):
            if self.is_add:
                self.add_to_snake()

            for i in range(self.size - 1, 0, -1):
                self.elements[i][0] = self.elements[i - 1][0]
                self.elements[i][1] = self.elements[i - 1][1]

            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy
            
        def eat(self, foodx, foody):
            x = self.elements[0][0]
            y = self.elements[0][1]
            
            if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
                return True
            return False
        

        


    snake2 = Snake(150, 100)
    food = Food()

    running = True

    d = 5
    FPS = 30

    clock = pygame.time.Clock()

    while running:
        clock.tick(snake2.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


                if event.key == pygame.K_RIGHT and snake2.dx != -d:
                    snake2.dx = d
                    snake2.dy = 0
                if event.key == pygame.K_LEFT and snake2.dx != d:
                    snake2.dx = -d
                    snake2.dy = 0
                if event.key == pygame.K_UP and snake2.dy != d:
                    snake2.dx = 0
                    snake2.dy = -d
                if event.key == pygame.K_DOWN and snake2.dy != -d:
                    snake2.dx = 0
                    snake2.dy = d


          
        if snake2.eat(food.x, food.y):
            snake2.is_add = True
            food.gen()

        
        snake2.move()
        screen.fill((173, 255, 47))
    
        snake2.draw()
        food.draw()
        pygame.display.flip()

    pass

def easy():
    global run
    class Snake: 
        def __init__(self):
            self.size = 3
            self.radius = 10
            self.dx = 5
            self.dy = 0
            self.elements = [[100, 100], [120, 100], [140, 100]]
            self.score = 0
            self.is_add = False

        def draw(self): 
            for element in self.elements:
                pygame.draw.circle(screen, (139,69, 19), element, self.radius)
        def add_snake(self):
            self.size += 1
            self.score += 1
            self.elements.append([0, 0])
            self.is_add = False


        def move(self):
            if self.is_add:
                self.add_snake()
            for i in range(self.size -1, 0, -1):
                self.elements[i][0]=self.elements[i-1][0]
                self.elements[i][1]=self.elements[i-1][1]
            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy


    class Food:
        def __init__(self):
            self.x = random.randint(100, 700)
            self.y = random.randint(100, 500)
            self.image = pygame.image.load("apple.png")

        def draw(self):
            screen.blit(self.image, (self.x, self.y))


    def show_score(x, y, score):
        show = font1.render('Score' + str(score), True, (0,0,0),)
        screen.blit(show, (x, y))

    def collision():
        if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1]) ):
            snake.is_add = True 
            food.x = random.randint(100, 700)
            food.y = random.randint(100, 500)

    def show_walls():
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (768, i))

    def is_in_walls():
        return snake.elements[0][0] > 770  or snake.elements[0][0] < 30 or  snake.elements[0][1] > 570  or snake.elements[0][1] < 30
    def check_wall(wall_points, snake_list):
        for wall_point in wall_points:
            for snake_point in snake_list:
                if wall_point[0] == snake_point[0] and wall_point[1] == snake_point[1]:
                    game_over()
    def game_over():
        screen.fill((255, 255, 255))
        txt = font.render('Game over', True, (25, 25, 112))
        my_score = font.render('Total score: ' + str(snake.score), True, (135,206,135))
        screen.blit(my_score, (300, 250))
        screen.blit(txt, (300, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
    wall_image = pygame.image.load("walls.png")
    snake = Snake() 
    food = Food()
    while run: 
        mil = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 5
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -5
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -5
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 5
        if is_in_walls():
            game_over()
            run = False
        collision()
        screen.fill((173, 255, 47))
        snake.move()
        snake.draw()
        #show_walls()
        
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (768, i))
            wall_points.append((i,0))
            wall_points.append((i, 570))
            wall_points.append((0, i))
            wall_points.append((768, i))
        check_wall(wall_points, snake.elements)
        food.draw()
        show_score(0, 0, snake.score)
        pygame.display.flip()

    pass

def hard():
    global run
    class Snake: 
        def __init__(self):
            self.size = 3
            self.radius = 10
            self.dx = 5
            self.dy = 0
            self.elements = [[100, 100], [120, 100], [140, 100]]
            self.score = 0
            self.is_add = False

        def draw(self): 
            for element in self.elements:
                pygame.draw.circle(screen, (139,69, 19), element, self.radius)
        def add_snake(self):
            self.size += 1
            self.score += 1
            self.elements.append([0, 0])
            self.is_add = False


        def move(self):
            if self.is_add:
                self.add_snake()
            for i in range(self.size -1, 0, -1):
                self.elements[i][0]=self.elements[i-1][0]
                self.elements[i][1]=self.elements[i-1][1]
            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy


    class Food:
        def __init__(self):
            self.x = random.randint(100, 700)
            self.y = random.randint(100, 500)
            self.image = pygame.image.load("apple.png")

        def draw(self):
            screen.blit(self.image, (self.x, self.y))


    def show_score(x, y, score):
        show = font1.render('Score' + str(score), True, (0,0,0),)
        screen.blit(show, (x, y))

    def collision():
        if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1]) ):
            snake.is_add = True 
            food.x = random.randint(100, 700)
            food.y = random.randint(100, 500)

    def show_walls():
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (770, i))

            screen.blit(wall_image, (i+500, 200))
            screen.blit(wall_image, (300, i+300))
            
    def check_wall(wall_points, snake_list):
        for wall_point in wall_points:
            for snake_point in snake_list:
                if wall_point[0] == snake_point[0] and wall_point[1] == snake_point[1]:
                    game_over()
    

    def is_in_walls():
        return snake.elements[0][0] > 770  or snake.elements[0][0] < 30 or  snake.elements[0][1] > 570  or snake.elements[0][1] < 30 
   
    def game_over():
        screen.fill((255, 255, 255))
        txt = font.render('Game over', True, (25, 25, 112))
        my_score = font.render('Total score: ' + str(snake.score), True, (135,206,135))
        screen.blit(my_score, (300, 250))
        screen.blit(txt, (300, 200))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
    wall_image = pygame.image.load("walls.png")
    snake = Snake() 
    food = Food()
    while run: 
        mil = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 5
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -5
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -5
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 5
        if is_in_walls():
            game_over()
            run = False
        collision()
        screen.fill((173, 255, 47))
        snake.move()
        snake.draw()
        #show_walls()
        for i in range(0, WIDTH, 25):
            screen.blit(wall_image, (i, 0))
            screen.blit(wall_image, (i, 570))
            screen.blit(wall_image, (0, i))
            screen.blit(wall_image, (770, i))
            screen.blit(wall_image, (i+500, 200))
            screen.blit(wall_image, (300, i+300))
            wall_points.append((i,0))
            wall_points.append((i, 570))
            wall_points.append((0, i))
            wall_points.append((768, i))
            wall_points.append((i+500, 200))
            wall_points.append((300, i+300))
        check_wall(wall_points, snake.elements)
        food.draw()
        show_score(0, 0, snake.score)
        pygame.display.flip()

    pass

#menu.add.text_input('Name :', default='John Doe')
menu = pygame_menu.Menu(300, 400, 'Welcome',theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('1 Player', op)
menu.add.button('2 players', tp)
menu.add.button('Easy', easy)
menu.add.button('Hard', hard)

menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
pygame.quit()