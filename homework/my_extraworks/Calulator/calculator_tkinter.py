from tkinter import *

root = Tk()
root.title("Aadhith's Calculator")

inputBox = Entry(root, width=45, borderwidth=15)
inputBox.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def click(number):
    currentNumber = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(currentNumber) + str(number))
    
def clr():
    inputBox.delete(0, END) 
     
def equal():
    second_number = inputBox.get()
    inputBox.delete(0, END)
    
    if math == 'addition':
        inputBox.insert(0, f_num + int(second_number))
    if math == 'multiplication':
        inputBox.insert(0, f_num * int(second_number))
    if math == 'division':
        inputBox.insert(0, f_num / int(second_number))
    if math == 'subtraction':
        inputBox.insert(0, f_num - int(second_number))


    
def add():
    first_number = inputBox.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    inputBox.delete(0, END)
    
def subtract():
    first_number = inputBox.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    inputBox.delete(0, END)
    
def multiply():
    first_number = inputBox.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    inputBox.delete(0, END)
    
def divide():
    first_number = inputBox.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    inputBox.delete(0, END)
    
    
    
    
    
    
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))

button_equal = Button(root, text='=', padx=40, pady=20, command=equal)
button_add = Button(root, text='+', padx=40, pady=20, command=add)
button_subtract = Button(root, text='-', padx=40, pady=20, command=subtract)
button_divide = Button(root, text='÷', padx=40, pady=20, command=divide)
button_multiply = Button(root, text='x', padx=40, pady=20, command=multiply)
button_clrScrn = Button(root, text='clr', padx=40, pady=20, command=clr)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_clrScrn.grid(row=4, column=0)

button_add.grid(row=3, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()