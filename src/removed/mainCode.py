import turtle, json, sys
import turtleCommands#, inputWindow
from Tkinter import *

class Application():
    def __init__(self, root):
        self.buttonsframe = Frame(root)
        #self.buttonsframe.master.geometry("100x208")
        self.buttonsframe.pack({"side": "right", "fill": "y"})

        self.entryframe = Frame(root)
        #self.entryframe.master.geometry("900x12")
        self.entryframe.pack({"side": "bottom", "fill": "x"})

        self.labelsframe = Frame(root)
        self.labelsframe.master.geometry("1000x277")
        self.labelsframe.pack({"side": "top", "fill": "both"})

        self.clear = Button(self.buttonsframe, text="Clear", command=self.clearScreen, width=25, height=1)
        self.clear.pack({"side": "bottom"})

        self.p6 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p6.pack({"side": "bottom"})

        self.p1 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p1.pack({"side": "bottom"})

        self.p2 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p2.pack({"side": "bottom"})

        self.p3 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p3.pack({"side": "bottom"})

        self.p4 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p4.pack({"side": "bottom"})

        self.p5 = Button(self.buttonsframe, text="placeholder", command=None, width=25, height=1)
        self.p5.pack({"side": "bottom"})

        self.quit = Button(self.buttonsframe, text="Exit", command=self.destroy, width=25, height=1)
        self.quit.pack({"side": "bottom"})

        self.contents = StringVar()
        self.contents.set("")

        self.entry = Entry(self.entryframe)
        self.entry["textvariable"] = self.contents
        self.entry.bind("<Key-Return>", self.output)
        self.entry.pack({"side": "bottom", "fill": "x", "ipady": 3})

        self.labels = []

        for i in range(10):
            self.labels.append(Label(self.labelsframe, text="", height=1, pady=3))
            self.labels[-1].pack({"anchor": "sw"})

    def output(self, event=None, string=None):
        #IF statement and (^^) defaul parameter values allows me to programatically write stuff to the screen
        if string:
            rawInput = string
            lowerInput = rawInput.lower()
        else:
            # \x represents a hex value and 0a is the value for a carriage return
            rawInput = self.contents.get().replace("\x0a", "")
            lowerInput = rawInput.lower()

        if lowerInput == "clear":
            self.clearScreen()
        elif lowerInput == "exit":
            self.destroy()

        else:
            self.labels[0].forget()
            del self.labels[0]

            self.labels.append(Label(self.labelsframe, text=rawInput, height=1, pady=3))
            self.labels[-1].pack({"anchor": "sw"})

            self.clearEntry()

    def clearScreen(self):
        for i in self.labels:
            i.forget()

        del self.labels
        self.labels = []

        for i in range(10):
            self.labels.append(Label(self.labelsframe, text="", height=1, pady=3))
            self.labels[-1].pack({"anchor": "sw"})

        self.clearEntry()

    def clearEntry(self):
        self.contents.set("")
        self.entry["textvariable"] = self.contents

    def destroy(self):
        self.buttonsframe.quit()
        self.entryframe.quit()
        self.labelsframe.quit()

synonymFile = open("synonym.JSON")
synonyms = json.load(synonymFile)
synonymFile.close()
print(synonyms["forwards"])

root = Tk()
root.wm_title("Command input window")
root.resizable(0, 0)

turtleCanvas = Canvas(root, width=800, height=100)
screen = turtle.TurtleScreen(turtleCanvas)
myTurtle = turtle.Turtle()

inputbox = Application(root)

stringToCommand = {"fwd": turtleCommands.forwards(myTurtle),
                   "bwd": turtleCommands.backwards(myTurtle),
                   "rt" : turtleCommands.rightTurn(myTurtle),
                   "lt" : turtleCommands.leftTurn(myTurtle),
                   "pd" : turtleCommands.penDown(myTurtle),
                   "pu" : turtleCommands.penUp(myTurtle)}

stringToCommand["pu"]()
stringToCommand["bwd"](200)
stringToCommand["pd"]()
stringToCommand["fwd"](100)
stringToCommand["rt"](45)
stringToCommand["bwd"](141.42)
stringToCommand["lt"](45)
stringToCommand["fwd"](100)
stringToCommand["pu"]()
stringToCommand["fwd"](200)
stringToCommand["pd"]()
stringToCommand["fwd"](50)

inputbox.output(string="Hello world")

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()
root.destroy()
