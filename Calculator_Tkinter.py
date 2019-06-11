import tkinter as tk
from tkinter import messagebox
import sys
mainWindow = tk.Tk()
mainWindow.title("Calculator")

first_number_label = tk.Label(mainWindow, text="Enter first number")
first_number_label.pack()
first_number_entry = tk.Entry(mainWindow)
first_number_entry.pack()

second_number_label = tk.Label(mainWindow, text="Enter second number")
second_number_label.pack()
second_number_entry = tk.Entry(mainWindow)
second_number_entry.pack()




def addition():
    first , second = takeValueInput()
    result = first + second
    print("Result is: ", result)
    result_label.config(text="Result is:" + str(result))
def sub():
    first , second = takeValueInput()
    result=first-second
    print("Result is :",result)
    result_label.config(text="Result is:"+ str(result))

def div():
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))
def mul():
    first , second =takeValueInput()
    result=first*second
    print("Result is :",result)
    result_label.config(text="Result is:"+ str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Only intergers are allowed")

        quit(0)

operations_label = tk.Label(mainWindow, text="Operations")
operations_label.pack()

add_button = tk.Button(mainWindow, text="+",command=lambda :addition())
add_button.pack()

minus_button = tk.Button(mainWindow, text="-",command=lambda: sub())
minus_button.pack()

multiply_button = tk.Button(mainWindow, text="*",command=lambda : mul())
multiply_button.pack()

divide_button = tk.Button(mainWindow, text="/",command=lambda:div())
divide_button.pack()

result_label = tk.Label(mainWindow, text="Operation result is:")
result_label.pack()
mainWindow.mainloop()