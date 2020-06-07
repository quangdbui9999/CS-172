import pygame
import abc


class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def getLocation(self):
        return (self.__x, self.__y)

    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def moveRight(self):
        self.__x += 1

    def __str__(self):
        return "Located at (" + str(self.__x) + "," + str(self.__y) + ")"

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRectangle(self):
        pass

class House(Drawable):
    def __init__(self, x = 0, y = 0, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__color = color

    def __str__(self):
        return "A house " + super().__str__()

    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.rect(surface, self.__color, [location[0] - 15, location[1] - 10, 30, 20])
        pygame.draw.polygon(surface, self.__color, [(location[0] - 15, location[1] - 10), (location[0] + 15, location[1] - 10), (location[0], location[1] - 20)])

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect([location[0] - 10, location[1] - 20, 30, 30])

class Snowman(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color

    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.circle(surface, self.__color, [location[0], location[1]], 20)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 20], 15)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 40], 10)

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect([location[0] - 20, location[1] - 45, 40, 90])



class Text(Drawable):
    def __init__(self, message = "Pygame", x = 0, y = 9, color = (0,0,0)):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 26)
        self.__surface = fontObj.render(message, True, color)

    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    def getRectangle(self):
        return self.__surface.get_rect()

pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My Drawable Objects")
fpsclock = pygame.time.Clock()

drawables = []
newHouse = House(100, 100, (255, 128, 0))
drawables.append(newHouse)
newCircle = Snowman(200, 100, (255, 255, 255))
drawables.append(newCircle)
newText = Text("Python and Pygame!", 75, 200, (0,0,255))
drawables.append(newText)

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()

    surface.fill((204, 229, 255))
    for drawable in drawables:
        drawable.draw(surface)

        #animation
    surface.fill((204, 229, 0))
    for drawable in drawables:
        drawable.moveRight()
        drawable.draw(surface)

    pygame.display.update()
    fpsclock.tick(30)