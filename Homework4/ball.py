'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: The Ball class inherits from Drawable and it will draw a circle or display an image circel
                    at its current location.
                    Ball class will implement the draw() and get_rect() method in order to create some Blocks.
'''

import pygame
from drawable import Drawable


class Ball(Drawable):
    def __init__(self, x = 0, y = 0, color = (0, 0, 0), visible = False):
        super().__init__(x, y, visible)
        self.__color = color

    def __str__(self):
        return "A ball's location: " + super().__str__()

    '''def draw(self, surface):
        if self.getVisible() == True:
            location = self.getLocation()
            pygame.draw.circle(surface, self.__color, [location[0], location[1]], 10)'''

    def draw(self, surface):
        if super().getVisible():
            location = list(self.getLocation())
            location[1] = super().getY() - 10
            ballImage = pygame.image.load("pokeball.png")
            surface.blit(ballImage, location)

    def get_rect(self):
        location = super().getLocation()
        return pygame.Rect([location[0], location[1], 25, 25])