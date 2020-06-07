'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: The Block class inherits from Drawable and it will draw a square with a black outline
            at its current location.
            Block class will implement the draw() and get_rect() method in order to a the Ball.
            At the same time, I have created 3 size blocks: small, medium, and large.
'''

import pygame
from drawable import Drawable

class Block(Drawable):
    LIVING_CORAL = (255, 111, 97)
    ULTRAVIOLET = (107, 91, 149)
    GREENERY = (136, 176, 75)
    ROSE_QUARTZ = (247, 202, 201)
    MASRSALA = (149, 82, 81)

    def __init__(self, x=0, y=0, color=(0, 0, 0), visible = True):
        super().__init__(x, y, visible)
        self.__color = color

    def __str__(self):
        return "A block's location: " + super().__str__()

    def draw(self, surface):
        if super().getVisible():
            location = self.getLocation()
            pygame.draw.rect(surface, self.__color, [location[0] - 15, location[1] - 15, 30, 30])
            pygame.draw.rect(surface, (0, 0, 0), [location[0] - 15, location[1] - 15, 30, 30], 3)

    def get_rect(self):
        location = self.getLocation()
        return pygame.Rect([location[0] - 15, location[1] - 5, 30, 30])

    def smallBlock(self, drawables = [], x = 0, y = 0):
        newBlock1 = Block(x, y, Block.LIVING_CORAL)
        drawables.append(newBlock1)
        newBlock2 = Block(x - 30, y, Block.ULTRAVIOLET)
        drawables.append(newBlock2)
        newBlock3 = Block(x - 60, y, Block.GREENERY)
        drawables.append(newBlock3)
        newBlock4 = Block(x, y - 30, Block.LIVING_CORAL)
        drawables.append(newBlock4)
        newBlock5 = Block(x - 30, y - 30, Block.ULTRAVIOLET)
        drawables.append(newBlock5)
        newBlock6 = Block(x - 60, y - 30, Block.GREENERY)
        drawables.append(newBlock6)
        newBlock7 = Block(x, y - 60, Block.LIVING_CORAL)
        drawables.append(newBlock7)
        newBlock8 = Block(x - 30, y - 60, Block.ULTRAVIOLET)
        drawables.append(newBlock8)
        newBlock9 = Block(x - 60, y - 60, Block.GREENERY)
        drawables.append(newBlock9)

    def mediumBlock(self, drawables=[], x = 0, y = 0):
        self.smallBlock(drawables, x, y)
        newBlock1 = Block(x - 90, y - 90, Block.ROSE_QUARTZ)
        drawables.append(newBlock1)
        newBlock2 = Block(x - 90, y - 60, Block.ROSE_QUARTZ)
        drawables.append(newBlock2)
        newBlock3 = Block(x - 90, y - 30, Block.ROSE_QUARTZ)
        drawables.append(newBlock3)
        newBlock4 = Block(x - 90, y, Block.ROSE_QUARTZ)
        drawables.append(newBlock4)
        newBlock5 = Block(x, y - 90, Block.LIVING_CORAL)
        drawables.append(newBlock5)
        newBlock6 = Block(x - 60, y - 90, Block.GREENERY)
        drawables.append(newBlock6)
        newBlock7 = Block(x - 30, y - 90, Block.ULTRAVIOLET)
        drawables.append(newBlock7)


    def largeBlock(self, drawables=[], x = 0, y = 0):
        self.mediumBlock(drawables, x, y)
        newBlock1 = Block(x - 120, y, Block.MASRSALA)
        drawables.append(newBlock1)
        newBlock2 = Block(x - 120, y - 30, Block.MASRSALA)
        drawables.append(newBlock2)
        newBlock3 = Block(x - 120, y - 60, Block.MASRSALA)
        drawables.append(newBlock3)
        newBlock4 = Block(x - 120, y - 90, Block.MASRSALA)
        drawables.append(newBlock4)
        newBlock5 = Block(x - 120, y - 120, Block.MASRSALA)
        drawables.append(newBlock5)
        newBlock6 = Block(x - 90, y - 120, Block.ROSE_QUARTZ)
        drawables.append(newBlock6)
        newBlock7 = Block(x - 60, y - 120, Block.GREENERY)
        drawables.append(newBlock7)
        newBlock8 = Block(x - 30, y - 120, Block.ULTRAVIOLET)
        drawables.append(newBlock8)
        newBlock9 = Block(x, y - 120, Block.LIVING_CORAL)
        drawables.append(newBlock9)

