import pygame

pygame.init()

screen_width = 480
screen_hight = 640 
screen = pygame.display.set_mode((screen_width,screen_hight))


pygame.display.set_caption("song game")

clock =pygame.time.Clock()

background = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/무제.png")

character = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/images.jpeg")
character_size = character.get_rect().size 
character_width = character_size[0]
character_hight=character_size[1]
character_x_pos = screen_width/2-character_width/2
character_y_pos = screen_hight-character_hight

running = True 

to_x=0
to_y =0

character_speed = 0.6

enemy = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/enemy.jpeg")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_hight=enemy_size[1]
enemy_x_pos = screen_width/2-enemy_width/2
enemy_y_pos = (screen_hight/2)-(enemy_hight/2)

game_font = pygame.font.Font(None,40)

total_time = 10 
start_ticks = pygame.time.get_ticks()

while running:
    dt = clock.tick(60) #game 화면의 초당 프레임 수 

    #print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
               to_x -=character_speed 
            elif event.key ==pygame.K_RIGHT:
                to_x +=character_speed
            elif event.key ==pygame.K_UP:
                to_y -=character_speed
            elif event.key ==pygame.K_DOWN:
                to_y +=character_speed
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x =0
            if event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y =0

    character_x_pos +=to_x*dt
    character_y_pos +=to_y*dt

    if character_x_pos <0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width -character_width
    if character_y_pos <0:
        character_y_pos=0
    elif character_y_pos>screen_hight-character_hight:
        character_y_pos=screen_hight -character_hight
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("collision occurs")
        running = False
    screen.blit(background, (0,0))
    # screen.fill((0,0,255)) #rgb 값 주는것 

    screen.blit(character, (character_x_pos,character_y_pos))

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    pygame.display.update()

    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000

    timer = game_font.render(str(int(total_time-elapsed_time)),True,(0,0,255))
    screen.blit(timer,(10,10))
    if total_time - elapsed_time <=0:
        print("time out!")
        running = False
pygame.quit()