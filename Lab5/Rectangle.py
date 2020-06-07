import pygame
from Drawable import Drawable


class Rectangle(Drawable):
    def __init__(self, x=0, y=0, width = 0, height = 0, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, [location[0], location[1], self.__width, self.__height])
