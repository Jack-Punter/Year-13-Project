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
        self.contents = []

    def push(self, data):
        self.contents.append(data)

    def pop(self):
        return self.contents.popleft()

    def returnContents(self):
        return self.contents

    def length(self):
        return len(self.contents)

def matchBracketsToProcess(string):
    stack = Stack()
    queue = Queue()
    error = Queue()

    for index in range(len(string)):
        if string[index] == "[":
            stack.push(index)

        elif string[index] == "]":
            if stack.length() == 0:
                error.push("Error: Unopened Bracket")

            else:
                queue.push([stack.pop(), index])

    if stack.length() != 0:
        error.push("Error: Brackets not closed")

    if error.length() == 0:
        return queue
    else:
        return error

print(matchBracketsToProcess("[[[[][][]]]]").returnContents())
