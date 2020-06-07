from stack import Stack

def add(x, y):
    answer = x + y
    return answer

def subtract(x, y):
    answer = x - y
    return answer

def multiple(x, y):
    answer = x * y
    return answer

def divide(x, y):
    answer = x / y
    return answer

operators = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}

def postfix(expression):
    myStack = Stack()
    expression = expression.replace("\n", "")
    components = expression.split(" ")

    for index in components:
        if index in operators:
            value1 = myStack.pop()
            value2 = myStack.pop()
            #tempResult = operators[index](value2, value1)
            tempResult = eval(value2 + index + value1)
            myStack.push(tempResult)
        else:
            myStack.push(index)
    result = myStack.top()
    return float(result)

if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")
    expression = input("Enter Expression:\n")
    while expression != "exit":
        result = postfix(expression)
        print("Result: %.1f" % result)
        expression = input("Enter Expression:\n")