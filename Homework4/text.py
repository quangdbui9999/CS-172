'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: The Text class inherits from Drawable and it will be used to display the player’s score.
                    Text class will implement the draw() and get_rect() method in order to create some Text.
'''


import pygame
from drawable import Drawable


class Text(Drawable):
    def __init__(self, message="Pygame", x = 0, y = 0, color = (0, 0, 0), fontSize = 26, score = 0):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontSize = fontSize
        fontObj = pygame.font.Font("freesansbold.ttf", self.__fontSize)
        self.__surface = fontObj.render(self.__message, True, color)
        self.__score = score

    def getMessage(self):
        return self.__message

    def setMessage(self, newMessage, newFontSize):
        self.__message = newMessage
        self.__fontSize = newFontSize
        fontObj = pygame.font.Font("freesansbold.ttf", self.__fontSize)
        self.__surface = fontObj.render(self.__message, True, self.__color)

    def getScore(self):
        return self.__score

    def setScore(self, newScore):
        self.__score = newScore

    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    def get_rect(self):
        return self.__surface.get_rect()