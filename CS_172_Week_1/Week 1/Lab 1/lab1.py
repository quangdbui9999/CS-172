import sys
from spellchecker import spellchecker


def get_file():
    print("Welcome to Text File Spellchecker")
    flag = False # check file name is valid file
    fileName = input("Enter the name of the file to read: ")

    while(flag == False):
        try:
            file = open(fileName, "r")
            print("Opening file succesfull")
            flag = True
            return fileName
        except FileNotFoundError:
            print("Could not open file.")
            flag = False
            fileName = input("Please enter the file name: ")

def read_through_file():
    getFileName = get_file()
    obj_1 = spellchecker("english_words.txt")
    file = open(getFileName, "r")

    correct = 0
    inCorrect = 0
    countLine = 0
    countWord = 0

    for line in file:
        countLine += 1
        for word in line.split():
            countWord += 1
            checker = obj_1.check(word)
            if(checker):
                correct += 1
            else:
                inCorrect += 1
                print(f"Possible Spelling Error on line {countLine}: {word}")
    print("{:,} words passed spell checker".format(correct))
    print("{:,} word failed spell checker.".format(inCorrect))
    percentage = correct / countWord * 100
    print("%0.2f%% of the words passed" %(percentage))
    file.close()

read_through_file()