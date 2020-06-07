
class Room():
    # Constructor sets the description
    # All four doors should be set to None to start
    def __init__(self, description):
        # Description of the room to print out
        # These should be unique so the player knows where they are
        self.__description = description

        # These either tell us what room we get to if we go through the door
        # or they are None if the "door" can't be taken.
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None

    def getNorth(self):
        return self.__north

    def getSouth(self):
        return self.__south

    def getEast(self):
        return self.__east

    def getWest(self):
        return self.__west

    def __str__(self):
        result = ""
        result += f"{self.__description}."
        return result

    def setDescription(self, d):
        self.__description = d

    def setNorth(self, n):
        self.__north = n

    def setSouth(self, s):
        self.__south = s

    def setEast(self, e):
        self.__east = e

    def setWest(self, w):
        self.__west = w