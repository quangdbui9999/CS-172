
from room import Room

class Maze():
    # Inputs: Pointer to start room and exit room
    # Sets current to be start room
    def __init__(self, st = None, ex = None):
        # Room the player starts in
        self.__start_room = st
        # If the player finds this room they win
        self.__exit_room = ex
        # What room is the player currently in
        self.__current = st

    def getStartRoom(self):
        return self.__start_room

    def getExitRoom(self):
        return self.__exit_room

    def getCurrent(self):
        return self.__current

    def setCurrent(self, newCurrent):
        self.__current = newCurrent

    # The next four all have the same idea
    # See if there is a room in the direction
    # If the direction is None, then it is impossible to go that way
    # in this case return false
    # If the direction is not None, then it is possible to go this way
    # Update current to the new move (move the player)
    # then return true so the main program knows it worked.
    def moveNorth(self):
        flag = False
        if(self.getCurrent().getNorth() == None):
            flag = False
        else:
            print("You went North")
            self.setCurrent(self.getCurrent().getNorth())
            flag = True
        return flag

    def moveSouth(self):
        flag = False
        if (self.getCurrent().getSouth() == None):
            flag = False
        else:
            print("You went South")
            self.setCurrent(self.getCurrent().getSouth())
            flag = True
        return flag

    def moveEast(self):
        flag = False
        if (self.getCurrent().getEast() == None):
            flag = False
        else:
            print("You went East")
            self.setCurrent(self.getCurrent().getEast())
            flag = True
        return flag

    def moveWest(self):
        flag = False
        if (self.getCurrent().getWest() == None):
            flag = False
        else:
            print("You went West")
            self.setCurrent(self.getCurrent().getWest())
            flag = True
        return flag

    # If the current room is the exit,
    # then the player won! return true
    # otherwise return false
    def atExit(self):
        flag = False
        if(self.getCurrent() == self.getExitRoom()):
            flag = True
        else:
            flag = False

        return flag

    # If you get stuck in the maze, you should be able to go
    # back to the start
    # This sets current to be the start_room
    def reset(self):
        self.setCurrent(self.__start_room)