'''
Full Name: Quang Bui
Drexel ID: 14392331
Purpose of the file: "main.py" will carry out entirely of Employee programm, include: print Menu, add new employee,
    calculate weekly wages, display payroll, update employee hourly rate, remove employee from payroll
'''
from employee import Employee
from node import Node
from linkedList import LinkedList

def menuLinkedList():
    print("*** CS 172 Payroll Simulator ***")
    print("a. Add New Employee")
    print("b. Calculate Weekly Wages")
    print("c. Display Payroll")
    print("d. Update Employee Hourly Rate")
    print("e. Remove Employee from Payroll")
    print("f. Exit the program\n")


def print_menu():
    obj = LinkedList()
    menu_option = ""
    menuLinkedList()

    while menu_option != "f":
        menu_option = input("Enter your choice: ")
        if menu_option == "a":
            obj.addTail()
            print()
            menuLinkedList()
        elif menu_option == "b":
            obj.enterHoursWorked()
            print()
            menuLinkedList()
        elif menu_option == "c":
            print("\n *** Payroll ***")
            obj.traverseList()
            print("\n")
            menuLinkedList()
        elif menu_option == "d":
            obj.updateHourlyRate()
            menuLinkedList()
        elif menu_option == "e":
            whatID = input("Enter the ID of the employee to remove from payroll: ")
            obj.removeEmployee(whatID)
            print("Done.\n\n")
            menuLinkedList()
        elif menu_option == "f":
            print("Good-Bye!")
            break

if __name__ == "__main__":
    print()
    print_menu()