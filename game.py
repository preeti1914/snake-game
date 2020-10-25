import pygame
import random

pygame.mixer.init()

x = pygame.init()
#colors
white=(255,255,255)
red=(255,0,0) 
black=(0,0,0)
green=(124,252,0)
#creating window
screen_width=700
screen_height=1200
gameWindow=pygame.display.set_mode((screen_height,screen_width))
# Game title
pygame.display.set_caption("SNAKE")
pygame.display.update()
#font
font =pygame.font.SysFont(None, 55, bold=False, italic=False)
#score
score=0
#clock
clock= pygame.time.Clock()



#plotting snake
def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
         pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

#score bar
def score_screen(text,color,x,y):
    screen_score= font.render(text,True,color)
    gameWindow.blit(screen_score,[x,y])


#  game loop iske undar kam se kam processing krni hai so that game fast bane 
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    #reading  high score
    with open("highscore.txt","r") as f:
      highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            score_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<25 and abs(snake_y - food_y)<25:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length +=5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            score_screen("Score: " + str(score)+"highscore:"+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, green, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()

