from Fraction import Fraction

class FractionProblems:
    def __init__(self, n = 0):

        valid = False
        while not valid:
            try:
                n = input("Enter Number of iterations (integer>0): ")
                x = int(n)
                if (x < 0):
                    valid = False
                    print("Bad Input")
                else:
                    valid = True
                    self.__n = x
            except ValueError as e:
                valid = False
                print("Bad Input")
                #n = int(input("Enter Number of iterations (integer>0): "))



    def __str__(self):
        result = "";
        result += str(self.__n)
        return result

    def HarmonicSeries(self):
        result = Fraction(0, 1)
        for i in range(1, self.__n + 1):
            result = result + Fraction(1, i)
        return result

    def Two(self):
        result = Fraction(0, 1)
        for i in range(0, self.__n + 1):
            x = Fraction(1, 2) ** i
            result = result + (x)
        return result

    def Zero(self):
        result = Fraction(0, 1)
        for i in range(0, self.__n + 1):
            x = Fraction(1, 2) ** i
            result = result + (x)
        return result * (-1) + 2

    def PartialRiemannZeta(self, b):
        result = Fraction(0, 1)
        for i in range(1, self.__n + 1):
            x = Fraction(1, i) ** b
            result = result + x
        return result

    def getN(self):
        return self.__n


if __name__ == "__main__":
    number = FractionProblems()
    H = number.HarmonicSeries()
    print(f"H({number.getN()}) = {H}")
    print("H({}) = {:.8f}".format(number.getN(), H.getFractionResult()))

    T = number.Two()
    print(f"T{number.getN()}) = {T}")
    print("T({}) = {:.8f}".format(number.getN(), T.getFractionResult()))

    Z = number.Zero()
    print(f"Z({number.getN()}) = {Z}")
    print("Z({}) = {:.8f}".format(number.getN(), Z.getFractionResult()))

    b = 8
    for i in range(2, b + 1):
        R = number.PartialRiemannZeta(i)
        print(f"R({number.getN()}, {i}) = {R}")
        print("R({}, {}) = {:.8f}".format(number.getN(), i, R.getFractionResult()))