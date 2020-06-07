
'''
Full Name: Quang Bui
Drexel ID: 14392331
Purpose of the file: "node.py" will create a Node in order to use in Linked List
    A node will include an Employee data and nextNode to pointer to the next Employee
'''


from employee import Employee

class Node():
    def __init__(self, data = Employee(), nextNode = None):
        self.__data = data
        self.__nextNode = nextNode

    def getNextNode(self):
        return self.__nextNode

    def getItem(self):
        return self.__data

    def setData(self, newData):
        self.__data = newData

    def setNextNode(self, newNextNode):
        self.__nextNode = newNextNode

    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)