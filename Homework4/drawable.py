'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: Create own version of the Drawable abstract base class
'''

# import abc to using the POLYMORPHISM
import abc

# Base class, parent class
class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x = 0, y = 0, visible = False):
        self.__x = x
        self.__y = y
        self.__visible = visible

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

    def getVisible(self):
        return self.__visible

    def setVisible(self, newVisible):
        self.__visible = newVisible

    def getVisible(self):
        return self.__visible

    def getLocation(self):
        return (self.__x, self.__y)

    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def __str__(self):
        return "Located at (" + str(self.__x) + "," + str(self.__y) + ")"

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass