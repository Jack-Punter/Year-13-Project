# Imports a Queue data struckture which i am using in my custom class
from collections import deque

class Stack():
    def __init__(self):
        self.contents = []

    def push(self, data):
        self.contents.append(data)

    def pop(self):
        return self.contents.pop()

    def returnContents(self):
        return self.contents

    def length(self):
        return len(self.contents)

class Queue():
    def __init__(self):
        self.contents = deque()

    def push(self, data):
        self.contents.append(data)

    def pop(self):
        data = self.contents.popleft()
        return data

    def returnContents(self):
        return self.contents

    def length(self):
        return len(self.contents)

# Test sctipt for Queues and Stacks. Only runs if you run this module directly
if __name__ == "__main__":
    q = Queue()
    q.push("Line 1")
    q.push("Line 2")
    print(q.pop())
    print(q.pop())

class BinaryTreeNode():
    def __init__(self, command, value):
        """Node for our comand tree that contains the command of the node and
        the value liked to it (so distance, angle or number of times to repeat).
        It also contains a completed atribute that will be either None (for any
        node that isnt a repeat) or True or Flase (should only be false when the
        tree is being constructed as it is used to determine if the next node
        goes right or left)."""
        self.command = command
        self.value = value
        if command == "rpt":
            self.completed = False
        else:
            self.completed = None

        self.rightChild = None
        self.leftChild = None

    def nodeCommand(self):
        return self.command

    def out(self):
        print(self.command+", "+str(self.value)+", "+str(self.completed))

    def insertLeft(self, data, value):
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(data, value)
        else:
            temp = BinaryTreeNode(data, value)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, data, value):
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(data, value)
        else:
            temp = BinaryTreeNode(data, value)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def returnNode(self):
        return self

class Tree():
    def __init__(self):
        self.head = None

    def setHead(self, command, value):
        self.head = BinaryTreeNode(command, value)
    # def run(self):
    #     self.head.insertRight("Mango")
    #     self.head.insertLeft("Apple")
    #     self.printTreeIn(self.head)
    #     print("\n")
    #     self.addNode("Grape", self.head)
    #     self.addNode("Zebra", self.head)
    #     self.addNode("Gorilla", self.head)
    #     self.addNode("Xander", self.head)
    #     #print("Added")
    #     print("\n")
    #     self.printTreeIn(self.head)

    # def addNode(self, data, place):
    #     if place == None:
    #         place = BinaryTreeNode(data)
    #     elif data < place.data:
    #         if place.leftChild == None:
    #             place.insertLeft(data)
    #         else:
    #             self.addNode(data, place.leftChild)
    #     elif data > place.data:
    #         if place.rightChild == None:
    #             place.insertRight(data)
    #         else:
    #             self.addNode(data, place.rightChild)

    def addNode(self, command, value=None, place=None):
        if place == None:
            self.head = BinaryTreeNode(command, value)

        elif place.command == "rpt" and place.completed == False:
            if place.leftChild == None:
                place.insertLeft(command, value)

            else:
                self.addNode(command, value, place.leftChild)

        else:
            if place.rightChild == None:
                place.insertRight(command, value)

            else:
                self.addNode(command, value, place.rightChild)

    def endRpt(self, place):
        returnValue = False
        if place != None:
            returnValue = self.endRpt(place.leftChild)
            if place.command == "rpt" and place.completed == False and returnValue == False:
                place.completed = True
                returnValue = True
            else:
                returnValue = self.endRpt(place.rightChild)
        return returnValue

    def produceQueue(self, tree, queue=Queue()):
        if tree != None:
            self.produceQueue(tree.leftChild, queue)
            queue.push(tree.returnNode())
            self.produceQueue(tree.rightChild, queue)
            return queue

    def printTreePre(self, tree):
        if tree != None:
            tree.out()
            self.printTreePre(tree.leftChild)
            self.printTreePre(tree.rightChild)

    def printTreeIn(self, tree):
        if tree != None:
            self.printTreeIn(tree.leftChild)
            tree.out()
            self.printTreeIn(tree.rightChild)

    def printTreePost(self, tree):
        if tree != None:
            self.printTreePost(tree.leftChild)
            self.printTreePost(tree.rightChild)
            tree.out()
