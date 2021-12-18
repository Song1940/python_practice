import pygame

pygame.init()

screen_width = 480
screen_hight = 640 
screen = pygame.display.set_mode((screen_width,screen_hight))

pygame.display.set_caption("song game")

running = True 
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

pygame.quit()