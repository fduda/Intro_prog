import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.geometry("300x300")    #size of frame, made it constant

        self.pack()
        self.create_widgets()
        self.master.title("My Simple Calculator") #title of frame

        #init the result list of [number, action, number]
        self.result = ["NA", "ACTION", "NA"]


    #create all widgets/ buttons
    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.reset = tk.Button(self)
        self.reset["text"] = "RESET button\n(Click me to do so)"
        self.reset["command"] = self.reset_pressed
        # print(self.reset.keys())
        self.reset.pack(side="top")

        self.create_numbers()
        self.create_actions()


    #Create the numbers buttons
    def create_numbers(self):
        #make all digits
        for i in range(10):
            self.button = tk.Button(self)
            self.button["text"] = str(i)
            self.button["command"] = self.press_numbers(i)
            self.button.pack(side="left")

    #action buttons including "="
    def create_actions(self):
        self.button = tk.Button(self)
        self.button["text"] = "="
        self.button["command"] = self.press_action("=")
        self.button.pack(side="bottom")

        self.button = tk.Button(self)
        self.button["text"] = "+"
        self.button["command"] = self.press_action("+")
        self.button.pack(side="bottom")

        self.button = tk.Button(self)
        self.button["text"] = "-"
        self.button["command"] = self.press_action("-")
        self.button.pack(side="bottom")

        self.button = tk.Button(self)
        self.button["text"] = "*"
        self.button["command"] = self.press_action("*")
        self.button.pack(side="bottom")

        self.button = tk.Button(self)
        self.button["text"] = "/"
        self.button["command"] = self.press_action("/")
        self.button.pack(side="bottom")

    def reset_pressed(self):
        self.result = ["NA", "ACTION", "NA"]

    #returns a function of pressing numbers
    def press_numbers(self, n):
        #When the user presses the numbers buttons, add the number to it's right place in the list of calculations
        def pressed():
            #no numbers input yet
            if self.result[0] == "NA":
                self.result[0] = n
            #added numbers but no action- so continue the first number
            elif self.result[1] == "ACTION":
                self.result[0] = int(str(self.result[0])+ str(n))
            #entered the action but no second number yet
            elif self.result[2] == "NA":
                self.result[2] = n
            #entered number and started the second number so add to it
            else:
                self.result[2] = int(str(self.result[2]) + str(n))

            print(self)

        return pressed

    def press_action(self, ac):
        def pressed_ac():
            #for the result
            if (ac == "="):
                #if there was enough input for calculations
                if (type(self.result[0]) == int) and (self.result[1] != "ACTION") and (type(self.result[2]) == int):
                    #should have been "switch/ case"
                    if self.result[1] == "-":
                        print(self, "=")
                        print(self.result[0]-self.result[2])
                    elif self.result[1] == "+":
                        print(self, "=")
                        print(self.result[0]+self.result[2])
                    elif self.result[1] == "*":
                        print(self, "=")
                        print(self.result[0]*self.result[2])
                    elif self.result[1] == "/":
                        #no dividing 0
                        if self.result[2] == 0:
                            print("MATH ERROR")
                        else:
                            print(self, "=")
                            print(self.result[0]/self.result[2])

                #Reset the calculations
                self.reset_pressed()

                ##in case you want to quit the frame when finished
                # self.master.destroy()

            #if there was no action yet (and not "=")
            elif self.result[1] == "ACTION":
                self.result[1] = ac
                print(self)
        return pressed_ac

    #An str function, to print the values saved until the current point
    def __str__(self):
        s = ''
        if type(self.result[0]) == int:
            s += str(self.result[0])
            if self.result[1] != "ACTION":
                s += self.result[1]
                if type(self.result[2]) == int:
                    s += str(self.result[2])
        return s

root = tk.Tk()
app = Application(master=root)
app.mainloop()