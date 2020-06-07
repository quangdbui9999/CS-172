'''
Full name: Quang Bui
Drexel user ID: 14392331
Purpose of the file: FileProcessing class will readFile, writeFile, and get the maximum Score
                    and total Score to print on the Graphic
'''

import re # re is very helpful to use regular expression

class FileProcessing:
    def __init__(self, fileName = "highScore.txt"):
        self.__fileName = fileName

    # check File Name is valid or not valid
    def get_file(self):
        flag = False  # check file name is valid file

        while (flag == False):
            try:
                file = open(self.__fileName, "r")
                flag = True
                return flag
            except FileNotFoundError:
                print(f"File name: \"{self.__fileName}\" does not exist.")
                flag = False
                return flag

    # Print the maximum and total Scores:
    def getMaxScore(self):
        max_score = 0
        if self.get_file():
            with open(self.__fileName, "r+") as file:
                data = file.readlines()  # read text file
                for line in data:
                    number = re.findall("\d+", line) # read only digit numbers
                    number = int(number[0])

                    if(max_score < number):
                        max_score = number
        return int(max_score)

    def getTotlaScore(self):
        total_score = 0

        if self.get_file():
            with open(self.__fileName, "r+") as file:
                data = file.readlines()  # read text file
                for line in data:
                    number = re.findall("\d+", line) # read only digit numbers
                    number = int(number[0])
                    total_score += number
        return total_score

    # Write file when you finish the GAME or you QUIT the GAME
    def writeFile(self, what_score):
        f = open(self.__fileName, "a")
        f.write(f"High Score: {int(what_score)}")
        f.write("\n")
        f.close()