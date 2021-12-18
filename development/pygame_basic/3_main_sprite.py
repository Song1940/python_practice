import pygame

pygame.init()

screen_width = 480
screen_hight = 640 
screen = pygame.display.set_mode((screen_width,screen_hight))


pygame.display.set_caption("song game")

background = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/무제.png")

character = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/images.jpeg")
character_size = character.get_rect().size 
character_width = character_size[0]
character_hight=character_size[1]
character_x_pos = screen_width/2-character_width/2
character_y_pos = screen_hight-character_hight

running = True 
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    # screen.fill((0,0,255)) #rgb 값 주는것 

    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update()


pygame.quit()