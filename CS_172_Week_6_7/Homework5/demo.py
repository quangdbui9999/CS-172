
class Node():
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, d):
        self.__data = d

    def setNext(self, n):
        self.__next = n

    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)

class LinkedList():
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    def remove(self, item):
        current = self.__head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # item was in the 1st node
        if previous == None:
            self.__head = current.getNext()
        else: # item somewhere after the first node
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def __getitem__(self, index): # used to support[]
        if index > len(self):
            raise IndexError

        current = self.__head

        for i in range(index):
            current = current.getNext()

        return current.getData()

    def __len__(self): # used to support len(myLinkedList)
        if self.__head == Node:
            return 0

        current = self.__head # list is not empty and has at least 1 element in the lisr
        counter = 1

        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter

    def __str__(self):
        mystr = ''
        current = self.__head

        while current != None:
            mystr += str(current.getData()) + " --> "
            current = current.getNext()

        return mystr


if __name__ == "__main__":
    print('Linked List Demo')
    print('----------------')

    # create a new linked list
    myLinkedList = LinkedList()
    print("Empty linked list: ")
    print(myLinkedList)

    # append a few elements to the list
    myLinkedList.append(10)
    myLinkedList.append(20)
    myLinkedList.append(30)
    myLinkedList.append(5)
    myLinkedList.append(12)
    myLinkedList.append(40)
    print('The current list after adding a few elements:')
    print(myLinkedList)
    print()

    # check if linked list is empty, if not print how many nodes there are
    if myLinkedList.isEmpty():
        print("This linked list is empty")
    else:
        print('There are', len(myLinkedList), ' elements in the list.')

    # access a node via the [] operator
    for index in range(0, len(myLinkedList)):
        print("At index", index, ": ", myLinkedList[index])
    print()

    # remove elements from the list
    print('Removing an element from the list')
    myLinkedList.remove(10)
    print(myLinkedList)
    print()

    # a better approach to removing items
    item = 200
    if myLinkedList.search(item):
        myLinkedList.remove(item)
        print(myLinkedList)
    else:
        print('No such element in the linked list')