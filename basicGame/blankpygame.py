import pygame, sys
from pygame.locals import *

'''
# top left corner (10, 20), 200 px wide, 300 px tall
spamRect = pygame.Rect(10, 20, 200, 300)
print(spamRect)
print(spamRect == (10,20,200,300))
print(spamRect.top)
print(spamRect.right)
print(spamRect.bottom)
print(spamRect.left)
spamRect.right = 350
print(spamRect.left)
'''

'''
#print(pygame.Color(255, 0, 0))
myColor = pygame.Color(255, 0, 0, 128)
print(myColor == (255,0,0,128.0))
'''

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300)) # set_mode with arguments is a tuple, not int
anotherSurface = DISPLAYSURF.convert_alpha()
print(DISPLAYSURF)
pygame.display.set_caption('Hello World! Game')
while True:
    for event in pygame.event.get():
        
        #event handling, constantly checkong and re-checking many times 
        #a second for any new events that have happened
        #it returns a list of pygame.event.Event
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() # dras the Surface object returned by pygame.display.set_mode()
