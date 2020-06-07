import pygame

#initialization
pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!") # give Window a title

#main game loop
while True:
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q)):
            pygame.quit()
            exit()
    pygame.display.update()