
'''
Full Name: Quang Bui
Drexel ID: 14392331
Purpose of the file: "linkedlist.py" is the most important file will carry out entirely of Employee programm,
    include: add new employee (DO NOT ACCEPT 2 SAME ID), calculate weekly wages, display payroll,
            update employee hourly rate, and remove employee from payroll
'''

from node import Node
from employee import Employee

class LinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None

    def getHead(self):
        return self.__head

    def getTail(self):
        return self.__tail

    def checkEmplyLinkedList(self): # does list if empty (return True) of not (return False)
        flag = False
        if self.__head is None or self.__tail is None:
            flag = True
        else:
            flag = False
        return flag

    def getListSize(self): # count how many node in the Linked List
        count = 0

        if self.__head is None:
            count = 0
        else:
            currentNode = self.__head
            while currentNode is not None:
                count += 1
                currentNode = currentNode.getNextNode()
        return count

    def traverseList(self): #traverse the list print the information of all Employees in the list
        if self.__head is None:
            print("List has no element")
            return
        else:
            currentNode = self.__head
            while currentNode is not None:
                print(currentNode.getItem())
                currentNode = currentNode.getNextNode()

    def findEmployeeID(self, whatID): #traverse the list and return the node that contain the Employee ID of whatID
        current = self.__head
        while current is not None:
            if current.getItem().getEmployeeID() == whatID:
                return current
            else:
                current = current.getNextNode()
        return None

    def removeHead(self):  # remove element at the beginning of the list
        if(self.__head is None):
            return
        self.__head = self.__head.getNextNode()

    def removeTail(self): # remove element at the end of the list
        if (self.__head is None):
            return
        if(self.__head.getNextNode() is None):
            self.removeHead()
        k = self.__head
        while k is not None:
            if k.getNextNode() == self.__tail:
                k.setNextNode(None)
                self.__tail = k
            k = k.getNextNode()


    def removeEmployee(self, whatID):
        currentNode = self.findEmployeeID(whatID)
        if currentNode is None or self.__head is None:
            return None

        # ID at head
        if self.__head.getItem().getEmployeeID() == whatID:
            self.removeHead()
        # ID at tail
        if self.__tail.getItem().getEmployeeID() == whatID:
            self.removeTail()

        # ID at any position in the range [head + 1 position to end - 1 position]
        g = self.__head
        k = self.__head
        while k is not None:
            if k == currentNode:
                g.setNextNode(k.getNextNode())

            g = k
            k = k.getNextNode()

    def addElement(self, newNode): # add element to the end of the list
        if self.checkEmplyLinkedList():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNextNode(newNode)
            self.__tail = newNode

    def addTail(self): # add Employee at the end of the list
        newID = input("Enter the new employee ID: ")
        newHourlyRate = float(input("Enter the hourly rate:  "))
        newNode = Node(Employee(newID, newHourlyRate))

        if(self.getListSize() == 0): # if the list is empty
            self.addElement(newNode) # simple, to add the first element in the list
        else:
            currentNode = self.__head
            while currentNode is not None: # traverse the list
                # check 2 ID Employee is same or not
                if newNode.getItem().getEmployeeID() == currentNode.getItem().getEmployeeID(): # if 2 ID is the same occurs
                    print(f"OOPS! The employee ID {newNode.getItem().getEmployeeID()} is existed in the list. Can you try another one, please?")
                    return
                else: # if, add Employee to the end of the list
                    self.addElement(newNode)
                    return

    def enterHoursWorked(self): #traverse the list and update hours work of all Employee in the list
        currentNode = self.__head
        while currentNode is not None:
            newHoursWorked = float(input(f"Enter hours worked for employee {currentNode.getItem().getEmployeeID()} : "))
            currentNode.getItem().setHourWorked(newHoursWorked)
            currentNode = currentNode.getNextNode()

    def updateHourlyRate(self): #traverse the list and update hourly rate of a particular ID of Employee in the list
        employeeID = input("Enter the employeeID to update hourly rate: ")
        node_update = self.findEmployeeID(employeeID)

        if node_update is not None:
            newHourlyRate = float(input(f"Enter New Hourly Rate for emloyee ID {employeeID}: "))
            node_update.getItem().setHourlyRate(newHourlyRate)
            return
        else:
            print(f"Employee ID {employeeID} was not found in the list.")