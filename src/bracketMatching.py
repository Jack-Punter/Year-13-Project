from dataStructures import Queue, Stack

def matchBrackets(string):
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

# Test sctipt. Only runs if you run this module directly
if __name__ == "__main__":
    inputString = "[AA[BB]CC[DD[EE[FF]GG]HH]II]"
    #inputString = "fwd 1000 rpt 4 [rpt 3 [fwd 500 rt 90] lt 72 rpt 5 [fwd 100 lt 144] rt 18] rt 180 fwd 1000"
    lis = matchBrackets(inputString).returnContents()

    print(lis)
    for i in lis:
        print(inputString[i[0]:i[1]+1])
