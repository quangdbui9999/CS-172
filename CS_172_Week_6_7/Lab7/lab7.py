
from room import Room
from maze import Maze

'''
This maze has three rooms. The player walks north from the start room 
gets to a middle room. The middle room leads to the exit. 
'''


my_rooms = []

my_rooms.append(Room("You are in room 1."))
my_rooms.append(Room("You are in room 2."))
my_rooms.append(Room("You are in room 3."))
my_rooms.append(Room("You are in room 4."))
my_rooms.append(Room("You are in room 5."))
my_rooms.append(Room("You are in room 6."))
my_rooms.append(Room("You are in room 7."))
my_rooms.append(Room("You are in room 8."))
my_rooms.append(Room("You are in room 9."))
my_rooms.append(Room("You are in room 10."))
my_rooms.append(Room("You are in room 11."))

my_rooms[0].setWest(my_rooms[1])
my_rooms[1].setEast(my_rooms[0])

my_rooms[1].setSouth(my_rooms[2])
my_rooms[2].setNorth(my_rooms[1])

my_rooms[2].setWest(my_rooms[3])
my_rooms[3].setEast(my_rooms[2])

my_rooms[3].setNorth(my_rooms[4])
my_rooms[4].setSouth(my_rooms[3])

my_rooms[5].setSouth(my_rooms[4])
my_rooms[4].setNorth(my_rooms[5])

my_rooms[5].setEast(my_rooms[6])
my_rooms[6].setWest(my_rooms[5])

my_rooms[6].setEast(my_rooms[7])
my_rooms[7].setWest(my_rooms[6])

my_rooms[7].setEast(my_rooms[8])
my_rooms[8].setWest(my_rooms[7])

my_rooms[8].setSouth(my_rooms[9])
my_rooms[9].setNorth(my_rooms[8])

my_rooms[9].setSouth(my_rooms[10])
my_rooms[10].setNorth(my_rooms[9])




'''#room 0 is south of room 1
my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
#Room 2 is east of room 1
my_rooms[1].setEast(my_rooms[2])
my_rooms[2].setWest(my_rooms[1])'''

#Make a maze!
#Set the start and exit rooms.

my_maze = Maze(my_rooms[0], my_rooms[10])

haveDirection = False

direction = input("Enter direction to move north west east south restart\n")

while my_maze.atExit() == False:
    if (direction == "reset"):
        my_maze.reset()
        print("You went back to the start!")

    if (direction == "north"):
        if my_maze.moveNorth() == True:
            haveDirection = True

    if (direction == "south"):
        if my_maze.moveSouth() == True:
            haveDirection = True

    if (direction == "east"):
        if my_maze.moveEast() == True:
            haveDirection = True

    if (direction == "west"):
        if my_maze.moveWest() == True:
            haveDirection = True

    if haveDirection == False:
        print("Direction invalid, try again.")


    print(my_maze.getCurrent())
    if(my_maze.atExit() == False):
        direction = input("Enter direction to move north west east south restart\n")
    else:
        print("You found the exit!")
    haveDirection = False