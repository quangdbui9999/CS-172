# Python program to demonstrate insert operation in binary search tree

# A utility class that represents an individual node in a BST

'''
class Node():
    def __init__(self, key):
        self.__left = None
        self.__right = None
        self.__data = key

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getData(self):
        return self.__data

    def setLeft(self, l):
        self.__left = l

    def setRight(self, r):
        self.__right = r

    def setData(self, d):
        self.__data = d

    def insert(self, newData):
        if self.__data:
            if newData < self.__data:
                if self.__left is None:
                    self.__left = Node(newData)
                else:
                    self.__left.insert(newData)
            elif newData > self.__data:
                if self.__right is None:
                    self.__right = Node(newData)
                else:
                    self.__right.insert(newData)
        else:
            self.__data = newData

    def __str__(self):
        result = ""
        result += f"{self.__data}\n"
        return result

    def printTree(self):
        if self.__left:
            self.__left.printTree()
        print(self.__data)
        if self.__right:
            self.__right.printTree()


if __name__ == "__main__":
    root = Node(50)
    root.insert(20)
    root.insert(30)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    print("In order traversal of the given tree")
    #root.deleteNode(80)
    root.printTree()
'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):
    #base case
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else: # If key is same as root's key, then this is the node to be deleted
        # node with only 1 child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #node with 2 children
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

'''
print
"\nDelete 20"
root = deleteNode(root, 20)
print
"Inorder traversal of the modified tree"
inorder(root)

print
"\nDelete 30"
root = deleteNode(root, 30)
print
"Inorder traversal of the modified tree"
inorder(root)

print
"\nDelete 50"
root = deleteNode(root, 50)
print
"Inorder traversal of the modified tree"
inorder(root)
'''

if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder(root)
    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)