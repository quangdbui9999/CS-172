#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list

class Stack:
    # Create a New Empty Stack
    def __init__(self):
        self.__S = []

    # Display the Stack
    def __str__(self):
        return str(self.__S)

    # Add a new element to top of stack
    def push(self, x):
        self.__S.append(x)

    # Remove the top element from stack
    def pop(self):
        return self.__S.pop()

    # See what element is on top of stack
    # Leaves stack unchanged
    def top(self):
        return self.__S[-1]

    def postFixMath(self, exp):
        data = exp.split()
        for i in data:
            if i == "+" or i == "-" or i == "*" or i == "/":
                value1 = self.pop()
                value2 = self.pop()
                computation = eval(value2 + i + value1)
                self.push(str(computation))
            else:
                self.push(i)
        return float(self.top())


if __name__ == "__main__":
    obj = Stack()
    with open("input.txt", "r") as fileInput:
        allPostfix = fileInput.readlines()
        for eachPostfix in allPostfix:
            print("Expression: " + eachPostfix, end = "")
            print("Answer: " + str(obj.postFixMath(eachPostfix)) + "\n")

    '''print("Welcome to Postfix Calculator.\nEnter exit to quit.")
    string_exp = input("Enter expression: \n")
    while(string_exp != "exit"):
        obj = Stack()
        print(obj.postFixMath(string_exp))
        string_exp = input("Enter expression: \n")'''
