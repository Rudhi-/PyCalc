from tkinter import *


def addNewDigit(currentNum, newDigit):
    return (currentNum * 10) + newDigit


class CalcGui:
    def __init__(self):
        self.val1 = NONE
        self.val2 = NONE
        self.result = NONE
        self.screen = NONE
        self.root = Tk()
        self.root.minsize(width=300, height=300)
        self.root.configure(bg="#4C4C43")
        self.setUp()

    def buttonHandler(self, b1Input=FALSE, b2Input=FALSE, b3Input=FALSE, b4Input=FALSE,
                      b5Input=FALSE, b6Input=FALSE, b7Input=FALSE, b8Input=FALSE,
                      b9Input=FALSE, b0Input=FALSE, bPlusInput=FALSE, bMinusInput=FALSE,
                      bMultInput=FALSE, bDivideInput=FALSE, bEqualsInput=FALSE, bClearInput=FALSE):
        if b1Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 1
                else:
                    self.val1 = addNewDigit(self.val1, 1)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 1
                else:
                    self.val2 = addNewDigit(self.val2, 1)
                self.screen.configure(text=self.val2)
        elif b2Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 2
                else:
                    self.val1 = addNewDigit(self.val1, 2)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 2
                else:
                    self.val2 = addNewDigit(self.val2, 2)
                self.screen.configure(text=self.val2)
        elif b3Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 3
                else:
                    self.val1 = addNewDigit(self.val1, 3)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 3
                else:
                    self.val2 = addNewDigit(self.val2, 3)
                self.screen.configure(text=self.val2)
        elif b4Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 4
                else:
                    self.val1 = addNewDigit(self.val1, 4)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 4
                else:
                    self.val2 = addNewDigit(self.val2, 4)
                self.screen.configure(text=self.val2)
        elif b5Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 5
                else:
                    self.val1 = addNewDigit(self.val1, 5)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 5
                else:
                    self.val2 = addNewDigit(self.val2, 5)
                self.screen.configure(text=self.val2)
        elif b6Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 6
                else:
                    self.val1 = addNewDigit(self.val1, 6)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 6
                else:
                    self.val2 = addNewDigit(self.val2, 6)
                self.screen.configure(text=self.val2)
        elif b7Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 7
                else:
                    self.val1 = addNewDigit(self.val1, 7)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 7
                else:
                    self.val2 = addNewDigit(self.val2, 7)
                self.screen.configure(text=self.val2)
        elif b8Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 8
                else:
                    self.val1 = addNewDigit(self.val1, 8)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 8
                else:
                    self.val2 = addNewDigit(self.val2, 8)
                self.screen.configure(text=self.val2)
        elif b9Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 9
                else:
                    self.val1 = addNewDigit(self.val1, 9)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 9
                else:
                    self.val2 = addNewDigit(self.val2, 9)
                self.screen.configure(text=self.val2)
        elif b0Input is TRUE:
            if self.result is NONE:  # user is entering first value
                if self.val1 is NONE:
                    self.val1 = 0
                else:
                    self.val1 = addNewDigit(self.val1, 0)
                self.screen.configure(text=self.val1)
            else:  # user is entering second value
                if self.val2 is NONE:
                    self.val2 = 0
                else:
                    self.val2 = addNewDigit(self.val2, 0)
                self.screen.configure(text=self.val2)
        elif bPlusInput is TRUE:
            self.result = "+"
            self.screen.configure(text="+")
        elif bMinusInput is TRUE:
            self.result = "-"
            self.screen.configure(text="-")
        elif bMultInput is TRUE:
            self.result = "x"
            self.screen.configure(text="x")
        elif bDivideInput is TRUE:
            self.result = "/"
            self.screen.configure(text="/")
        elif bEqualsInput is TRUE:
            if self.result is "+":
                self.result = (self.val1 + self.val2)
            elif self.result is "-":
                self.result = (self.val1 - self.val2)
            elif self.result is "x":
                self.result = (self.val1 * self.val2)
            elif self.result is "/":
                try:
                    self.result = (self.val1 / self.val2)
                except ZeroDivisionError:
                    self.result = "CANNOT DIVIDE BY ZERO!"
            self.screen.configure(text=str(self.result))
            if self.result is "CANNOT DIVIDE BY ZERO!":
                self.result = 0
            self.val1 = self.result
            self.val2 = NONE
            self.result = NONE
        elif bClearInput is TRUE:
            self.val1 = NONE
            self.val2 = NONE
            self.result = NONE
            self.screen.configure(text=0)
        else:
            self.screen.configure(text="NOPE")

    # Setting up Gui Loop
    def setUp(self):

        self.screen = Label(self.root, text="WELCOME TO CALC GUI!", font=('Helvetica', 16))
        self.screen.grid(row=0, column=0, columnspan=4, sticky='NSEW')

        # frame = Frame(root)
        b1 = Button(self.root, text="1", command=lambda: self.buttonHandler(b1Input=TRUE), font=('Helvetica', 16))
        b2 = Button(self.root, text="2", command=lambda: self.buttonHandler(b2Input=TRUE), font=('Helvetica', 16))
        b3 = Button(self.root, text="3", command=lambda: self.buttonHandler(b3Input=TRUE), font=('Helvetica', 16))
        b4 = Button(self.root, text="4", command=lambda: self.buttonHandler(b4Input=TRUE), font=('Helvetica', 16))
        b5 = Button(self.root, text="5", command=lambda: self.buttonHandler(b5Input=TRUE), font=('Helvetica', 16))
        b6 = Button(self.root, text="6", command=lambda: self.buttonHandler(b6Input=TRUE), font=('Helvetica', 16))
        b7 = Button(self.root, text="7", command=lambda: self.buttonHandler(b7Input=TRUE), font=('Helvetica', 16))
        b8 = Button(self.root, text="8", command=lambda: self.buttonHandler(b8Input=TRUE), font=('Helvetica', 16))
        b9 = Button(self.root, text="9", command=lambda: self.buttonHandler(b9Input=TRUE), font=('Helvetica', 16))
        b0 = Button(self.root, text="0", command=lambda: self.buttonHandler(b0Input=TRUE), font=('Helvetica', 16))

        b1.grid(row=1, column=0, sticky='NSEW')
        b2.grid(row=1, column=1, sticky='NSEW')
        b3.grid(row=1, column=2, sticky='NSEW')
        b4.grid(row=2, column=0, sticky='NSEW')
        b5.grid(row=2, column=1, sticky='NSEW')
        b6.grid(row=2, column=2, sticky='NSEW')
        b7.grid(row=3, column=0, sticky='NSEW')
        b8.grid(row=3, column=1, sticky='NSEW')
        b9.grid(row=3, column=2, sticky='NSEW')
        b0.grid(row=4, column=1, sticky='NSEW')

        operations = Frame()
        bPlus = Button(operations, text="+", command=lambda: self.buttonHandler(bPlusInput=TRUE),
                       font=('Helvetica', 16))
        bMinus = Button(operations, text="-", command=lambda: self.buttonHandler(bMinusInput=TRUE),
                        font=('Helvetica', 16))
        bTimes = Button(operations, text="x", command=lambda: self.buttonHandler(bMultInput=TRUE),
                        font=('Helvetica', 16))
        bDivide = Button(operations, text="/", command=lambda: self.buttonHandler(bDivideInput=TRUE),
                         font=('Helvetica', 16))
        bEquals = Button(operations, text="=", command=lambda: self.buttonHandler(bEqualsInput=TRUE),
                         font=('Helvetica', 16))
        bClear = Button(operations, text="C", command=lambda: self.buttonHandler(bClearInput=TRUE),
                        font=('Helvetica', 16))

        bPlus.grid(row=0, column=0, sticky='NSEW')
        bMinus.grid(row=1, column=0, sticky='NSEW')
        bTimes.grid(row=2, column=0, sticky='NSEW')
        bDivide.grid(row=3, column=0, sticky='NSEW')
        bEquals.grid(row=4, column=0, sticky='NSEW')
        bClear.grid(row=5, column=0, sticky="NSEW")

        operations.grid(row=1, column=3, rowspan=4, sticky='NSEW')

        operations.grid_rowconfigure(0, weight=1)
        operations.grid_rowconfigure(1, weight=1)
        operations.grid_rowconfigure(2, weight=1)
        operations.grid_rowconfigure(3, weight=1)
        operations.grid_rowconfigure(4, weight=1)
        operations.grid_rowconfigure(5, weight=1)
        operations.grid_columnconfigure(0, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)


gui = CalcGui()
gui.root.mainloop()
