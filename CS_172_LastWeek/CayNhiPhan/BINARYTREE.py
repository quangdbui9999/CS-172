
class Node():
    def __init__(self, data):
        self.__value = data
        self.__left = None
        self.__right = None

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def getValue(self):
        return self.__value

    def setLeft(self, l):
        self.__left = l

    def setRight(self, r):
        self.__right = r

    def setValue(self, newValue):
        self.__value = newValue

    def insert(self, data):
        if self.getValue() == data:
            return False  # As BST cannot contain duplicate data

        elif data < self.getValue():
            if self.getLeft():
                return self.getLeft().insert(data)
            else:
                self.setLeft(Node(data))
                return True

        else:
            if self.getRight():
                return self.getRight().insert(data)
            else:
                self.setRight(Node(data))
                return True

    def search(self, data):
        if self.__value == data:
            return True
        elif data < self.getValue():
            if self.getLeft():
                return self.getLeft().search(data)
            else:
                return False
        else:
            if self.getRight():
                return self.getRight().search(data)
            else:
                return False

    def findMinValue(self, node):
        current = node

        while (current.getLeft() is not None):
            current = current.getLeft()

        return current

    def deleteNode(self, data):
        if self.getValue() is None:
            return None

        if data < self.getValue():
            self.setLeft(self.getLeft().deleteNode(data))
        elif data > self.getValue():
            self.setRight(self.getRight().deleteNode(data))
        else:
            if self.getLeft() is None:
                temp = self.getRight()
                self.setValue(None)
                return temp
            elif self.getRight() is None:
                temp = self.getLeft()
                self.setValue(None)
                return temp

            temp = self.findMinValue(self.getRight())
            self.setValue(temp.getValue())
            self.setRight(self.getRight().deleteNode(temp.getValue()))

        return self

    def preorder(self):
        if self:
            print(str(self.getValue()), end=' ==> ')
            if self.getLeft():
                self.getLeft().preorder()
            if self.getRight():
                self.getRight().preorder()

    def inorder(self):
        if self:
            if self.getLeft():
                self.getLeft().inorder()
            print(str(self.getValue()), end=' ==> ')
            if self.getRight():
                self.getRight().inorder()

    def postorder(self):
        if self:
            if self.getLeft():
                self.getLeft().postorder()
            if self.getRight():
                self.getRight().postorder()
            print(str(self.getValue()), end=' ==> ')


class BST():
    def __init__(self):
        self.__root = None

    def setRoot(self, r):
        self.__root = r

    def insert(self, value):
        if self.__root:
            return self.__root.insert(value)
        else:
            self.setRoot(Node(value))
            return True
        '''node = Node(value)

        if self.__root == None:
            self.__root = node
            return

        current = self.__root
        while True:
            if value <= current.getValue():
                if current.getLeft() == None:
                    current.setLeft(node)
                    return
                else:
                    current = current.getLeft()
            else:
                if current.getRight() == None:
                    current.setRight(node)
                    return
                else:
                    current = current.getRight()'''

    '''def search(self, value):
        if self.__root == None:
            return False
        current = self.__root
        while current is not None:
            if current.getValue() == value:
                return True
            elif value < current.getValue():
                current = current.getLeft()
            else:
                current = current.getRight()
        return False'''

    def delete(self, value):
        if self.__root is not None:
            if(self.__root.search(value)):
                print(f"\nDelete the node {value} out of the list")
                return self.__root.deleteNode(value)
            else:
                print(f"\nElement {value} is not exist in the list.")

    def preorder(self):
        if self.__root is not None:
            print()
            print('Preorder: ')
            self.__root.preorder()

    def inorder(self):
        print()
        if self.__root is not None:
            print('Inorder: ')
            self.__root.inorder()

    def postorder(self):
        print()
        if self.__root is not None:
            print('Postorder: ')
            self.__root.postorder()




if __name__ == "__main__":
    tree = BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)

    tree.preorder()

    tree.delete(2)
    tree.inorder()

    tree.delete(3)
    tree.postorder()

    tree.delete(124)
    tree.postorder()

    tree.delete(5)
    tree.preorder()