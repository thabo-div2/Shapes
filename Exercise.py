# Importing from tkinter

from tkinter import *


root = Tk()

root.geometry("500x500")
root.title("Area of shapes")


class Triangle:

    myresult = StringVar()

    def __init__(self, master):
        self.frame = LabelFrame(master, text="Triangle")
        self.frame.pack(side=BOTTOM)
        self.lab1 = Label(self.frame, text="Please enter height: ")
        self.lab1.pack()
        self.lab2 = Label(self.frame, text="Please enter base: ")
        self.lab2.pack()
        self.lab3 = Label(self.frame, text="", width="50", textvariable=self.myresult)
        self.lab3.pack()
        self.myentry1 = Entry(self.frame)
        self.myentry1.pack()
        self.myentry2 = Entry(self.frame)
        self.myentry2.pack()
        self.btn_area = Button(self.frame, text="Calculate Area", command=self.area_of_triangle)
        self.btn_area.pack()

    def area_of_triangle(self):
        result = 0.5 * int(self.myentry1.get()) * int(self.myentry2.get())
        self.myresult.set(result)


class Rectangle:

    myresult = StringVar()

    def __init__(self, master):
        self.frame = LabelFrame(master, text="Rectangle")
        self.frame.pack(side=TOP)
        self.lab1 = Label(self.frame, text="Please enter length: ")
        self.lab1.pack()
        self.lab2 = Label(self.frame, text="Please enter width: ")
        self.lab2.pack()
        self.lab3 = Label(self.frame, text="", width="50", textvariable=self.myresult)
        self.lab3.pack()
        self.myentry1 = Entry(self.frame)
        self.myentry1.pack()
        self.myentry2 = Entry(self.frame)
        self.myentry2.pack()
        self.btn_area = Button(self.frame, text="Calculate Area", command=self.area_of_rectangle)
        self.btn_area.pack()

    def area_of_rectangle(self):
        result = int(self.myentry1.get()) * int(self.myentry2.get())
        self.myresult.set(result)


class Circle:

    myresult = StringVar()

    def __init__(self, master):
        self.frame = LabelFrame(master, text="Circle")
        self.frame.pack(side=RIGHT)
        self.lab1 = Label(self.frame, text="Please enter radius: ")
        self.lab1.pack()
        self.myentry = Entry(self.frame)
        self.myentry.pack()
        self.lab2 = Label(self.frame, text="", width="50", textvariable=self.myresult)
        self.lab2.pack()
        self.btn_area = Button(self.frame, text="Calculate Area", command=self.area_of_circle)
        self.btn_area.pack()

    def area_of_circle(self):
        result = 3.14 * (int(self.myentry.get())**2)
        self.myresult.set(result)


x = Circle(root)
y = Rectangle(root)
z = Triangle(root)

root.mainloop()
