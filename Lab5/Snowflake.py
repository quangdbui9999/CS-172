import pygame
from Drawable import Drawable


class Snowflake(Drawable):
    def __init__(self, x=0, y=0, width = 0, color=(0, 0, 0), max_y = 500):
        super().__init__(x, y)
        self.__width = width
        self.__color = color
        self.__max_y = max_y

    def getMaxY(self):
        return self.__max_y

    def setMaxY(self, new_value):
        if new_value < 0:
            self.__max_y = 500
        else:
            self.__max_y = new_value

    def draw(self, surface):
        location = self.getLoc()
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1]), ([location[0] + 5, location[1]]), self.__width)
        pygame.draw.line(surface, self.__color, (location[0], location[1] - 5), ([location[0], location[1] + 5]), self.__width)
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1] - 5), ([location[0] + 5, location[1] + 5]),
                         self.__width)
        pygame.draw.line(surface, self.__color, (location[0] - 5, location[1] + 5), ([location[0] + 5, location[1] - 5]),
                         self.__width)