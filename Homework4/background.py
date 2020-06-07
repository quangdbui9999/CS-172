'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: BackgroundEnvironment created an environment for the PyGame
'''

import pygame


class BackgroundEnvironment():
    def __init__(self, image_file = "background.jpg", location = (0, 0)):
        self.__image = pygame.image.load(image_file)
        self.__location = location

    def getImage(self):
        return self.__image

    def getLocation(self):
        return self.__location