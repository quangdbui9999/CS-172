
import random
from BST import BST
import time
import matplotlib.pyplot as plt


def populate(n, listN, tree):
    myList = []
    if n <= 0:
        return (0, 0)
    else:
        for i in range(0, n):
            k = random.randrange(0, n + 1, 1)
            myList.append(k)
            tree.append(k)
        return (myList, tree)

def countFrequencyList(listN):
    copyList = listN.copy()
    copyList = list(dict.fromkeys(copyList))

    for i in copyList:
        value = i
        count = 0
        for j in listN:
            if j == value:
                count += 1
        print(f"Number {value} appears {count} times.")

def searchKey(listN, tree):
    for i in listN:
        value = i
        foundValue = tree.isin(value)


if __name__ == "__main__":
    myTree = BST()
    myList = []
    randomList, random_BST = populate(12, myList, myTree)
    print(randomList)
    random_BST.inorder()

    startList = time.time()
    countFrequencyList(randomList)
    endList = time.time()

    differentTimeList = endList - startList
    print("List Search Time: " + str(differentTimeList))

    startBST = time.time()
    searchKey(randomList, random_BST)
    endBST = time.time()

    differentTimeBST = endBST - startBST
    print("Binary Search Time: " + str(differentTimeBST))

    listX = []
    listY = []
    BST_x = []
    BST_y = []

    for i in range(1, 10001, 1000):
        myList, myTree = populate(i, myList, myTree)

        # 1: list, 2: BST
        start1 = time.time()
        countFrequencyList(myList)
        end1 = time.time()
        different1 = end1 - start1

        listX.append(i)
        listY.append(different1)

        start2 = time.time()
        searchKey(myList, myTree)
        end2 = time.time()
        different2 = end2 - start2

        BST_x.append(i)
        BST_y.append(different2)

    plt.plot(listX, listY, label = "List")
    plt.plot(BST_x, BST_y, label = "Binary")
    plt.legend()
    plt.show()