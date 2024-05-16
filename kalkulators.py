from tkinter import *

mansLogs = Tk()
mansLogs.title('kalkulators')

def btnClick(number):
    current = e.get()
    newNumber = str(current) + str(number)
    e.delete(0, END)
    e.insert(0, newNumber)

def btnPlus():
    global num1
    global mathOp
    mathOp = "+"
    num1 = int(e.get())
    e.delete(0, END)

def btnC():
    e.delete(0, END)

def btnMinus():
    global num1
    global mathOp
    mathOp = "-"
    num1 = int(e.get())
    e.delete(0, END)

def btnTimes():
    global num1
    global mathOp
    mathOp = "*"
    num1 = int(e.get())
    e.delete(0, END)

def btnDal():
    global num1
    global mathOp
    mathOp = "/"
    num1 = int(e.get())
    e.delete(0, END)

def btnIr():
    num2 = int(e.get())
    result = 0
    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        if num2 != 0:  # Avoid division by zero
            result = num1 / num2
        else:
            result = "Error"
    else:
        result = 0
    e.delete(0, END)
    e.insert(0, str(result))

e = Entry(mansLogs, width=15, bd=10, font=("Arial", 20), justify="right")

btn0 = Button(mansLogs, text='0', padx=40, pady=20, command=lambda: btnClick(0))
btn1 = Button(mansLogs, text='1', padx=40, pady=20, command=lambda: btnClick(1))
btn2 = Button(mansLogs, text='2', padx=40, pady=20, command=lambda: btnClick(2))
btn3 = Button(mansLogs, text='3', padx=40, pady=20, command=lambda: btnClick(3))
btn4 = Button(mansLogs, text='4', padx=40, pady=20, command=lambda: btnClick(4))
btn5 = Button(mansLogs, text='5', padx=40, pady=20, command=lambda: btnClick(5))
btn6 = Button(mansLogs, text='6', padx=40, pady=20, command=lambda: btnClick(6))
btn7 = Button(mansLogs, text='7', padx=40, pady=20, command=lambda: btnClick(7))
btn8 = Button(mansLogs, text='8', padx=40, pady=20, command=lambda: btnClick(8))
btn9 = Button(mansLogs, text='9', padx=40, pady=20, command=lambda: btnClick(9))

btnPlus = Button(mansLogs, text='+', padx=40, pady=20, command=btnPlus, bg="light blue")
btnC = Button(mansLogs, text='C', padx=40, pady=20, command=btnC, bg="light blue")
btnMinus = Button(mansLogs, text='-', padx=40, pady=20, command=btnMinus, bg="light blue")
btnTimes = Button(mansLogs, text='*', padx=40, pady=20, command=btnTimes, bg="light blue")
btnDal = Button(mansLogs, text='/', padx=40, pady=20, command=btnDal, bg="light blue")
btnIr = Button(mansLogs, text='=', padx=40, pady=20, command=btnIr, bg="light blue")

e.grid(row=0, column=0, columnspan=4)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnPlus.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnMinus.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btnTimes.grid(row=3, column=3)

btn0.grid(row=4, column=0)
btnC.grid(row=4, column=1)
btnIr.grid(row=4, column=2)
btnDal.grid(row=4, column=3)

mansLogs.mainloop()