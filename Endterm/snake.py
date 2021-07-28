import pygame, time, random
  
x = 600
y = 400
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
pink = pygame.Color(230, 50, 230)
snake_speed = 10

pygame.init()
pygame.display.set_caption('Snake Pygame PP2')
game_window = pygame.display.set_mode((x, y))
  
fps = pygame.time.Clock()
snake_position = [50, 50]
  
# defining first 4 blocks of snake body
snake_body = [[50, 50],[40, 50],[30, 50],[20, 50]]
# food posiiton
food_position = [random.randrange(1, (x//10)) * 10, 
                  random.randrange(1, (y//10)) * 10]

spawn_food = True
direction = 'RIGHT'
change_to = direction
score = 0
background = pygame.image.load('images/bg1.jpg')

def game_over():
    my_font = pygame.font.SysFont('Arial', 30)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
        
    game_over_rect = game_over_surface.get_rect()
      
    # setting position of the text
    game_over_rect.midtop = (x/2, y/4)
      
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
      
    # after 2 seconds we will quit the program
    time.sleep(2)
      
    # deactivating pygame library
    pygame.quit()
      
    # quit the program
    quit()


def show_score(choice, color, font, size):    
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
  

#MAIN
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
  
#Do not move to the different directions. For ex. up to down
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
  
#Snake moves
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
  
#body growing
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        print("Yummy!")
        spawn_food = False
    else:
        snake_body.pop()
          
    if not spawn_food:
        food_position = [random.randrange(1, (x//10)) * 10, 
                          random.randrange(1, (y//10)) * 10]
          
    spawn_food = True
    game_window.fill(black)
    game_window.blit(background,(0,0))
    
    for pos in snake_body:
        pygame.draw.rect(game_window, pink,
                         pygame.Rect(pos[0], pos[1], 10, 10))


#Game over if:
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
  
    if snake_position[0] < 0 or snake_position[0] > x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > y-10:
        game_over()
  
#Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            
    show_score(1, white, 'Arial', 20)
  
    # Refresh game screen
    pygame.display.update()
  
    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)





