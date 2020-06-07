import pygame
import random
from Rectangle import Rectangle
from Snowflake import Snowflake

if __name__ == "__main__":

    y_coordination = 0
    pygame.init()
    surface = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption('Snowflake Wonderland')
    fpsclock = pygame.time.Clock()

    drawables = []
    newRectangle1 = Rectangle(0, 0, 1000, 450, (0, 0, 255))
    drawables.append(newRectangle1)
    newRectangle2 = Rectangle(0, 450, 1000, 350, (0, 255, 128))
    drawables.append(newRectangle2)

    spaceBar = True

    newSnowflake = Snowflake(0, 0, 1, (255, 255, 255), 500)
    ground = random.randint(475, 525)
    newSnowflake.setMaxY(ground)
    drawables.append(newSnowflake)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and (event.__dict__['key'] == pygame.K_SPACE):
                spaceBar = not spaceBar
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()

        if spaceBar:
            for drawable in drawables:
                drawable.draw(surface)
                if isinstance(drawable, Snowflake):
                    location = drawable.getLoc()
                    if location[1] != drawable.getMaxY():
                        drawable.moveDown()

        x_location = random.randint(0, 1000)
        newSnowflake = Snowflake(x_location, 0, 1, (255, 255, 255))
        ground = random.randint(475, 525)
        newSnowflake.setMaxY(ground)
        drawables.append(newSnowflake)
        pygame.display.update()
        fpsclock.tick(80)