# TODO: Import math module
import math

def quadratic_formula(a, b, c):
    # TODO: Compute the quadratic formula results in variables x1 and x2
    delta = math.pow(b, 2) - (4 * a * c)
    
    # flag: what is delta's value
    # 0: we have two same values
    # -1: no solution
    # 1: two seperate solution
    flag = 0
    
    if(delta < 0):
        flag = -1
        return flag
    elif(delta >= 0):
        square_root_delta = math.sqrt(delta)
        
        if(delta == 0):
            flag = 0
            x_double = -b / (2 * a)
            return (x_double, flag)
        else:
            flag = 1
            
            if(a + b + c == 0):
                x1 = 1
                x2 = c / a
            elif(a - b + c == 0):
                x1 = -1
                x2 = -c / a
            else:
                x1 = (-b + square_root_delta) / (2 * a)
                x2 = (-b - square_root_delta) / (2 * a)
            return (x1, x2, flag)
    

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefix_str, number))
    else:
        print("{}{:.2f}".format(prefix_str, number))
    

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0]) # 1 -5 -6
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    if(solution == -1):
        print('No solution')
    elif(solution[1] == 0):
        print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
        print_number(solution[0], "x1 = x2 = ")
    else:
        print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
        print_number(solution[0], "x1 = ")
        print_number(solution[1], "x2 = ")