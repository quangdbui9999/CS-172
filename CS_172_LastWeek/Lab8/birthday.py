
class Birthday():
    def __init__(self, birth_day, birth_month, birth_year):
        self.__birth_day = birth_day
        self.__birth_month = birth_month
        self.__birth_year = birth_year

    def __str__(self):
        result = ""
        result += "{:2d}/{:2d}/{:4d}".format(self.__birth_month, self.__birth_day, self.__birth_year)
        return result

    def __hash__(self):
        rule_hash = (self.__birth_day + self.__birth_month + self.__birth_year) % 12
        return rule_hash

    def getDay(self):
        return self.__birth_day

    def getMonth(self):
        return self.__birth_month

    def getYear(self):
        return self.__birth_year

    def getValue(self):
        result = (self.__birth_day + self.__birth_month + self.__birth_year) % 12
        return result

    def __eq__(self, other):
        flag = False
        if((self.__birth_year == other.getYear()) and (self.__birth_month == other.getMonth()) and (self.__birth_day == other.getDay())):
            flag = True
        else:
            flag = False
        return flag