import turtle, json, sys, os
import turtleCommands

if sys.version_info[0] == 2:
    from Tkinter import *
elif sys.version_info[0] == 3:
    from tkinter import *

class Application():
    def __init__(self):
        temp_synonymFile = open("..\\assets\\synonym.JSON")
        self.synonyms = json.load(temp_synonymFile)
        temp_synonymFile.close()
        print(self.synonyms["forwards"])

        self.root = Tk()
        self.root.wm_title("Command Input Window")
        self.root.resizable(0, 0)

        self.turtleCanvas = Canvas(self.root, width=600, height=400)
        self.turtle = turtle
        self.screen = self.turtle.TurtleScreen(self.turtleCanvas)
        self.myTurtle = self.turtle.Turtle()

        self.helpFile = "..\\assets\\helpFile.txt"

        self.stringToCommand = {"fwd": turtleCommands.forwards(self.myTurtle),
                                "bwd": turtleCommands.backwards(self.myTurtle),
                                "rt" : turtleCommands.rightTurn(self.myTurtle),
                                "lt" : turtleCommands.leftTurn(self.myTurtle),
                                "pd" : turtleCommands.penDown(self.myTurtle),
                                "pu" : turtleCommands.penUp(self.myTurtle)}

    def run(self):
       self.stringToCommand["pu"]()
       self.stringToCommand["bwd"](200)
       self.stringToCommand["pd"]()
       self.stringToCommand["fwd"](100)
       self.stringToCommand["rt"](45)
       self.stringToCommand["bwd"](141.42)
       self.stringToCommand["lt"](45)
       self.stringToCommand["fwd"](100)
       self.stringToCommand["pu"]()
       self.stringToCommand["fwd"](200)
       self.stringToCommand["pd"]()
       self.stringToCommand["fwd"](50)
       self.myTurtle.reset()

       self.output(string="Hello world")

       self.root.protocol("WM_DELETE_WINDOW", self.destroy)
       #self.turtleCanvas.protocol("WM_DELETE_WINDOW", self.destroy)
       self.root.mainloop()
       self.root.destroy()

    def createInputWindow(self):
        self.buttonsframe = Frame(self.root)
        #self.buttonsframe.master.geometry("100x208")
        self.buttonsframe.pack({"side": "right", "fill": "y"})

        self.entryframe = Frame(self.root)
        #self.entryframe.master.geometry("900x12")
        self.entryframe.pack({"side": "bottom", "fill": "x"})

        self.labelsframe = Frame(self.root)
        self.labelsframe.master.geometry("1000x277")
        self.labelsframe.pack({"side": "top", "fill": "both"})

        self.clear = Button(self.buttonsframe, text="Clear Screen", command=self.clearScreen, width=25, height=1)
        self.clear.pack({"side": "bottom"})

        self.p6 = Button(self.buttonsframe, text="Reset", command=self.reset, width=25, height=1)
        self.p6.pack({"side": "bottom"})

        self.p1 = Button(self.buttonsframe, text="Help File", command=self.openHelp, width=25, height=1)
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
            self.printToScreen(string)
            return
        else:
            if self.contents.get() == "":
                return
            # \x represents a hex value and 0a is the value for a carriage return
            self.rawInput = self.contents.get().replace("\x0a", "")
            self.lowerInput = self.rawInput.lower().strip()

        returned = self.process(self.lowerInput)
        if returned and returned != "clear":
            self.labels[0].forget()
            del self.labels[0]

            self.labels.append(Label(self.labelsframe, text=self.rawInput, height=1, pady=3))
            self.labels[-1].pack({"anchor": "sw"})

            self.clearEntry()
        elif returned and returned == "clear":
            pass
        else:
            self.printToScreen(self.rawInput)
            self.printToScreen("That is not a valid command")

    def printToScreen(self, string):
        self.labels[0].forget()
        del self.labels[0]

        self.labels.append(Label(self.labelsframe, text=string, height=1, pady=3))
        self.labels[-1].pack({"anchor": "sw"})

        self.clearEntry()

    def process(self, string):
        if string == "clear":
            self.clearScreen()
            return "clear"
        elif string == "exit":
            self.destroy()
            return "exit"
        elif string == "reset":
            self.reset()
            return "reset"
        else:
            space = string.find(" ")
            if space == -1:
                if string in self.synonyms:
                    if self.synonyms[string] == "pu" or self.synonyms[string] == "pd":
                        self.stringToCommand[self.synonyms[string]]()
                        return "command"
                    else:
                        self.printToScreen(self.rawInput)
                        self.printToScreen("Make sure you include an integer distance/angle after your command")
                        return "clear"
                return None

            elif "repeat" in string[:space]:
                self.printToScreen(self.rawInput+" Repeat")
                return "command"
            else:
                command = string[:space]
                try:
                    distance = int(string[space+1:])
                except ValueError :
                    self.printToScreen(self.rawInput)
                    self.printToScreen("Make sure you include an integer distance/angle after your command")
                    return "clear"

                if command in self.synonyms:
                    self.stringToCommand[self.synonyms[command]](distance)
                    return "command"
                return None

    def clearScreen(self):
        for i in self.labels:
            i.forget()
        del self.labels
        self.labels = []

        for i in range(10):
            self.labels.append(Label(self.labelsframe, text="", height=1, pady=3))
            self.labels[-1].pack({"anchor": "sw"})

        self.clearEntry()

    def reset(self):
        self.myTurtle.reset()
        self.clearScreen()

    def clearEntry(self):
        self.contents.set("")
        self.entry["textvariable"] = self.contents

    def destroy(self):
        self.buttonsframe.quit()
        self.entryframe.quit()
        self.labelsframe.quit()
        self.turtle.bye()
        self.root.destroy()
        sys.exit()

    def openHelp(self):
        os.startfile(self.helpFile)

app = Application()
app.createInputWindow()
app.run()
