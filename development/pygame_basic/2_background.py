import pygame

pygame.init()

screen_width = 480
screen_hight = 640 
screen = pygame.display.set_mode((screen_width,screen_hight))


pygame.display.set_caption("song game")

background = pygame.image.load("/Users/kimsong/Desktop/python/development/pygame_basic/무제.png")

running = True 
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    # screen.fill((0,0,255)) #rgb 값 주는것 

    pygame.display.update()
pygame.quit()