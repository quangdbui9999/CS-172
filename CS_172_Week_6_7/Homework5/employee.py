
'''
Full Name: Quang Bui
Drexel ID: 14392331
Purpose of the file: "employee.py" will create an Employee class with attribute: employeeID, number hours
    of worked, hourly rate, and gross wages. We do not accept the hourly rate less than 6.0, we also do
    not accept with number of hours worked with negative number.
    We have some method:
    - getEmployeeID(self): LinkedList can access the employeID attribute of Employee class
    - getHourWorked(self): LinkedList can access the hour_worked attribute of Employee class
    - getHourlyRate(self): LinkedList can access the hourly_rate attribute of Employee class
    - setHourWorked(self, newHourWorked): LinkedList can update the hour_worked attribute of Employee class
    - setHourlyRate(self, newHourlyRate): LinkedList can update the hourly_rate attribute of Employee class
'''

class Employee:
    def __init__(self, employeID = "None", hourly_rate = 0.0, hour_worked = 0.0, gross_wage = 0.0):
        self.__employeID = employeID

        if (hourly_rate >= 6.0):
            self.__hourly_rate = hourly_rate
        else:
            self.__hourly_rate = 0.0

        if (hour_worked > 0.0):
            self.__hour_worked = hour_worked
        else:
            self.__hour_worked = 0.0

        self.__gross_wage = (self.__hour_worked * self.__hourly_rate)

    def __str__(self):
        result = ""
        result += f"Employee ID:  {self.__employeID}\n"
        result += "Hourly Rate:  {}\n".format(self.__hourly_rate)
        result += "Hours Worked: {}\n".format(self.__hour_worked)
        result += "Gross Wages:  {}\n".format(self.__gross_wage)
        return result

    def getGrossWages(self):
        return self.__gross_wage

    def getEmployeeID(self):
        return self.__employeID

    def getHourWorked(self):
        return self.__hour_worked

    def getHourlyRate(self):
        return self.__hourly_rate

    def setEmployeeID(self, newEmployeeID):
        self.__employeID = newEmployeeID

    def setHourWorked(self, newHourWorked):
        if(newHourWorked > 0):
            self.__hour_worked = newHourWorked
        else:
            self.__hour_worked = 0
        self.__gross_wage = self.__hour_worked * self.__hourly_rate

    def setHourlyRate(self, newHourlyRate):
        if(newHourlyRate >= 6.0):
            self.__hourly_rate = newHourlyRate
        else:
            self.__hourly_rate = 6.0
        self.__gross_wage = self.__hour_worked * self.__hourly_rate