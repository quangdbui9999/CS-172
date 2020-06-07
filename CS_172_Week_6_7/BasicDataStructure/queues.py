
'''
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

class Customer():
    def __init__(self, name, seat):
        self.__name = name
        self.__seat = seat

    def __str__(self):
        #return "{0:16}: {1}".format(self.__name, self.__seat)
        return self.__name + " has seat # " + str(self.__seat)

    def __gt__(self, other):
        return self.__seat > other.__seat

def main():
    # let's create a few objects to place in our queue, stack, and priority stack
    julie = Customer("Julie", 18)
    harry = Customer("Harry", 20)
    marie = Customer("Marie", 15)

    #using the Python Queue class
    q = Queue()
    q.put(julie)
    q.put(harry)
    q.put(marie)

    print('Servicing customers in the order they arrived (FIFO):')
    while not q.empty():
        print(q.get())
    print()

    # using the Python Stack class --> LifoQueue
    s = LifoQueue()
    s.put(julie)
    s.put(harry)
    s.put(marie)

    print('Servicing customers starting with one that arrived last (LIFO):')
    while not s.empty():
        print(s.get())
    print()

    # using the Python priority queue class --> PriorityQueue
    p = PriorityQueue()
    p.put(julie)
    p.put(harry)
    p.put(marie)

    # ticket number is used as the priority: higher ticket number means lower priority
    print('Servicing customers by priority:')
    while not p.empty():
        print(p.get())
    print()

    # another example of priority queue with simple data added to the queue
    tasks = PriorityQueue()

    tasks.put((2, 'code'))
    tasks.put((1, 'eats'))
    tasks.put((3, 'sleep'))

    print('Here are tasks in the to-do list, in order of priority:')
    while not tasks.empty():
        next_item = tasks.get()
        print(next_item)

main()
'''

class MyQueue():
    def __init__(self):
        self.__theList = []

    def __str__(self):
        s = ''
        for i in range(0, len(self.__theList)):
            s = s + str(i) + ": " + str(self.__theList[i]) + "\n"
        return s

    def put(self, item):
        self.__theList.append(item)

    def get(self):
        a = self.__theList.pop(0)
        return a

    def clear(self):
        self.__theList = []

    def empty(self):
        if(self.clear() == 0):
            return True
        else:
            return False

    def __str__(self):
        s = ''
        for i in range(0, len(self.__theList)):
            s = s + str(i + 1) + ": " + str(self.__theList[i]) + "\n"
        return s


# Testing our queue implementation
if __name__ == '__main__':
    print('Testing our queue implementation')
    print('--------------------------------')

    # create a display a new queue
    line = MyQueue()
    print('Here is our Empty Queue: ')
    print(line)

    # enqueue a few values
    line.put("Mary")
    line.put("John")
    line.put("Rose")
    line.put("Bob")

    # display queue again
    print('Here is our queue after enqueing a few values:')
    print(line)

    # dequeue a value from the queue
    first = line.get() # get first value from the queue
    print("First in line: ", end = ' ')
    print(first)

    print('\nHere is our queue after dequeing first item:')
    print(line)