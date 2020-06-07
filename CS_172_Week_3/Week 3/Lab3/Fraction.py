class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.__numerator = numerator

        if denominator == 0:
            self.__denominator = 1
        else:
            self.__denominator = denominator

    def checkValidFraction(self):
        if self.__denominator == 0:
            return False
        return True

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def setNumerator(self, newNumerator):
        self.__numerator = newNumerator

    def setDenominator(self, newDenominator):
        if newDenominator == 0:
            self.__denominator = 1
        else:
            self.__denominator = newDenominator

    def gcd(self, a, b):
        if(a < 0):
            a = a * -1
        if(b < 0):
            b = b * -1

        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    def simpleFraction(self):
        greatestCommonDivisor = self.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // greatestCommonDivisor
        self.__denominator = self.__denominator // greatestCommonDivisor
        return self

    def __add__(self, other):
        if(isinstance(other, int)):
            return Fraction(self.__numerator * 1 + self.__denominator * other, self.__denominator * 1)
            #return Fraction(self.__numerator * 1 + self.__denominator * other, self.__denominator * 1).simpleFraction()

        if isinstance(other, Fraction):
            newNumerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
            newDenominator = self.__denominator * other.__denominator
            #return Fraction(newNumerator, newDenominator).simpleFraction()
            return Fraction(newNumerator, newDenominator)

    def __sub__(self, other):
        if (isinstance(other, int)):
            return Fraction(self.__numerator * 1 - self.__denominator * other, self.__denominator * 1).simpleFraction()

        if isinstance(other, Fraction):
            newNumerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
            newDenominator = self.__denominator * other.__denominator
            return Fraction(newNumerator, newDenominator).simpleFraction()

    def __mul__(self, other):
        if (isinstance(other, int)):
            return Fraction(self.__numerator * other, self.__denominator * 1).simpleFraction()

        if isinstance(other, Fraction):
            newNumerator = self.__numerator * other.__numerator
            newDenominator = self.__denominator * other.__denominator
            return Fraction(newNumerator, newDenominator).simpleFraction()

    def __truediv__(self, other):
        if (isinstance(other, int)):
            return Fraction(self.__numerator * 1, self.__denominator * other).simpleFraction()

        if isinstance(other, Fraction):
            newNumerator = other.__denominator
            newDenominator = other.__numerator
            return Fraction(newNumerator, newDenominator).__mul__(self)

    def __str__(self):
        result = ""

        if self.checkValidFraction() == False:
            result += "Fraction is invalid, please check again"
        else:
            #result += "Output Fraction's Information:\n"

            if (self.__denominator < 0):
                self.__numerator *= -1
                self.__denominator *= -1

            self.simpleFraction()

            if self.__denominator == 1:
                result += "{}".format(int(self.getFractionResult()))
            else:
                result += "{}/{}".format(int(self.__numerator), int(self.__denominator))
                #result += "Fraction: {}/{}\n".format(int(self.__numerator), int(self.__denominator))

        return result

    def getFractionResult(self):
        return self.__numerator / self.__denominator

    def __lt__(self, other):
        if self.getFractionResult() < other.getFractionResult():
            return True
        return False

    def __le__(self, other):
        if self.getFractionResult() <= other.getFractionResult():
            return True
        return False

    def __gt__(self, other):
        if self.getFractionResult() > other.getFractionResult():
            return True
        return False

    def __ge__(self, other):
        if self.getFractionResult() >= other.getFractionResult():
            return True
        return False

    def __eq__(self, other):
        if self.getFractionResult() == other.getFractionResult():
            return True
        return False

    def __ne__(self, other):
        if self.getFractionResult() != other.getFractionResult():
            return True
        return False

    def __pow__(self, exp):
        if(exp > 0):
            newNumerator = self.__numerator ** exp
            newDenominator = self.__denominator ** exp
            return Fraction(newNumerator, newDenominator)
        elif(exp < 0):
            exp = exp * -1
            newNumerator = self.__denominator ** exp
            newDenominator = self.__numerator ** exp
            return Fraction(newNumerator, newDenominator)
        elif exp == 0:
            return Fraction(1, 1)
