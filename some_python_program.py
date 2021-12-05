# What this program does is that it is a calculator that you can
# be able to use. You can be able to add, subtract, multiply, and divide.
# This calculator is a great code to be able to help with simple math equations.
# Updated on: 11 - 30 - 21
# Updated by: Alexander and Conner and Vanessa
#
#
# What these lines of code means is that it is importing the tkinter to be able
# to create the calculator. Then it was able to give it the tile of Simple
# Calculator.
from tkinter import *

root = Tk()

root.title("Simple Calculator")

# What these lines of code does is that it is able to create the calculator shape.
# It is able to create the different boxes within it and the box to display
# the numbers.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# What these codes do is that they are able to display the numbers
# on the screen when you click those numbers. Depending on the certain ones that you pick,
# it is able to display them.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# What these lines of codes are able to do is to make the clear button that you made
# work. It is to delete the numbers on the screen when you hit the clear button to get rid of it.
def button_clear():
    e.delete(0, END)

# What the following lines of code do here is that it is able to delete the number off
# the screen when you press one of the operators and display the second number you pick
# and it is able to clear them all when you hit equal. It is able to remember each
# number that you pick to be able to find the answer to the problem that you choose.
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# What the following lines of code do here is able to show the equation to use
# when you choose a certain operator. It is able to find the answer of the problem
# that you give it by using the certain one since of the button that you hit. This
# is a major part since this is the code that does the work of finding each answer to
# each of the following operators that you choose.

# you might want to consider adding documentation on a line by line basis since
# this is a critical function for the program
def button_equal():
    second_number = e.get() # This is going to pull the first number.
    e.delete(0, END) # This is going to delete the other numbers off the screen.
    if num_operator == '+': # This shows if the button you click is the add one it will choose this formula
        e.insert(0, f_num + int(second_number)) # This shows the formula to find the answer.
    elif num_operator == '*': # This shows if the button you click is multiplication it will choose this formula
        e.insert(0, f_num * int(second_number)) # This shows the formula to find the answer.
    elif num_operator == '/': # This shows if the button you click is division it will choose this formula.
        e.insert(0, f_num / int(second_number)) # This shows the formula to find the answer.
    elif num_operator == '-': # This shows if the button you click is subtraction it will choose this formula.
        e.insert(0, f_num - int(second_number)) # This shows the formula to find the answer.
    else: # This is if you choose a different number or symbol not on there.
        e.insert(0, "Invalid!!!") # It will display this answer.

# What the following lines so is that they are able to create the
# certain buttons for the calculator. They are able to click on them
# and to display the name for them.
#
# NOTE: We did not cover Lambda functins in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# What these lines are able to do is that they are able to display the button that
# you create for the calculator you are making. It is able to display the certain name that
# you give them. You can also show how big you want to make the button as well.

# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# What these lines of codes show is where each of the following
# numbers and signs are going to be on the calculator. It is able to put certain
# numbers and different signs where you want to put them.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# What the following line of code do here is to run the following
# function first. It is able to display the calculator. It is going
# to run that function first since you type that function first.

root.mainloop()