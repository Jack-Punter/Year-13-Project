from __future__ import print_function
import json
from dataStructures import Tree, Queue

temp_synonymFile = open("..\\assets\\synonym.json")
synonyms = json.load(temp_synonymFile)
temp_synonymFile.close()

temp_structureFile = open("..\\assets\\commandStructure.json")
commandStructure = json.load(temp_structureFile)
temp_structureFile.close()

def convertString(string):
    # REMEMBER TO CHECK BRACKETS USING MATCHER!!!
    stringList = string.replace("[", "").replace("]", " ]").split()
    stringQueue = Queue()

    for i in range(len(stringList)):
        if stringList[i] in synonyms:
            stringQueue.push(synonyms[stringList[i]])

        elif stringList[i].isdigit():
            stringQueue.push(int(stringList[i]))

        else:
            stringQueue.push(stringList[i])

    return stringQueue

def createTree(queue):
    tree = Tree()
    done = False
    while not done:
        try:
            item = queue.pop()
            if item == "]":
                tree.endRpt(tree.head)
            else:
                parameters = commandStructure[item][0]
                if parameters == 0:
                    tree.addNode(item, place=tree.head)
                else:
                    types = commandStructure[item][1:]
                    if parameters == 1:
                        value = queue.pop()
                        if types[0] == "int" and isinstance(value, int):
                            tree.addNode(item, value, place=tree.head)

                    elif parameters == 2:
                        value = queue.pop()
                        if types[0] == "int" and isinstance(value, int):
                            if types[1] == "commands":
                                tree.addNode("start", value, place=tree.head)
                                tree.addNode(item, value, place=tree.head)
        except IndexError:
            done = True
    return tree

def expandRpt(inQueue):
    tempList = []
    returnList = []
    done = False
    while not done:
        try:
            item  = inQueue.pop()
            if item.command == "rpt":
                print("itemvalue = "+str(item.value))
                for j in tempList:
                    print(j.command+":"+str(j.value))
                for value in range(item.value):
                    print("value = "+str(value))
                    for listItem in tempList:
                        #print(item.command+"-"+ str(item.value))
                        returnList.append(listItem)
                done = True
            elif item.command == "start":
                innerList = expandRpt(inQueue)
                for listItem in innerList:
                    tempList.append(listItem)

            else:
                tempList.append(item)
        except IndexError:
            done = True
    return returnList


def expandQueue(inQueue):
    outQueue = Queue()
    done = False
    while not done:
        try:
            item = inQueue.pop()
            #print(item)
            if item.command == "start":
                repeatList = expandRpt(inQueue)
                for listItem in repeatList:
                    outQueue.push(listItem)
            else:
                outQueue.push(item)
        except IndexError:
            done = True
    return outQueue

def process(string):
    stringTokens = convertString(string)
    commandTree = createTree(stringTokens)
    commandQueue = commandTree.produceQueue(commandTree.head)
    expandedQueue = expandQueue(commandQueue)
    return expandedQueue

# Testing Code
if __name__ == "__main__":
    inputString = "lt 180 pu forwards 200 rt 90 pd fwd 100 repeat 4 [repeat 3 [fwd 50 rt 90] lt 72 repeat 5 [fwd 10 lt 144] rt 162] rt 180 fwd 100"
    stringTokens = convertString(inputString)
    print(stringTokens.contents)
    for i in stringTokens.contents:
        print(i, end=" ")
    commandTree = createTree(stringTokens)
    commandTree.printTreeIn(commandTree.head)
    commandQueue = commandTree.produceQueue(commandTree.head)
    for i in commandQueue.contents:
        print("commandQueue: "+i.command+"-"+str(i.value))
    expandedQueue  = expandQueue(commandQueue)
    done = False
    count = 0
    while not done:
        try:
            node = expandedQueue.pop()
            count += 1
            print(node.command+"-"+str(node.value))
        except IndexError:
            done  = True
    print(count)

    raw_input("Press any enter to quit...")
