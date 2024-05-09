from tkinter import*

mansLogs=Tk()
mansLogs.title('kalkulators')

def btnClick(number):
 current=e.get()
 newNumber=str(current)+str(number)
 e.insert(0,newNumber)
 return 0

def btnCommand(command):
 global number
 global num1
 global mathOp
 mathOp=command
 num1=int(e.get())
 e.delete(0,END)
 return 0




e=Entry(mansLogs,Width=15,bd=10,font=("Arial",20),justify="right")

btn0=Button(mansLogs,text=0, padx='40',pady='20')
btn1=Button(mansLogs,text=1, padx='40',pady='20')
btn2=Button(mansLogs,text=2, padx='40',pady='20')
btn3=Button(mansLogs,text=3, padx='40',pady='20')
btn4=Button(mansLogs,text=4, padx='40',pady='20')
btn5=Button(mansLogs,text=5, padx='40',pady='20')
btn6=Button(mansLogs,text=6, padx='40',pady='20')
btn7=Button(mansLogs,text=7, padx='40',pady='20')
btn8=Button(mansLogs,text=8, padx='40',pady='20')
btn9=Button(mansLogs,text=9, padx='40',pady='20')

e.grid(row=0,column=0,columnspan=3)

btn7.grid(row=1,colomn=0)
btn8.grid(row=1,colomn=1)
btn9.grid(row=1,colomn=2)


btn4.grid(row=2,colomn=0)
btn5.grid(row=2,colomn=1)
btn6.grid(row=2,colomn=2)

btn1.grid(row=3,colomn=0)
btn2.grid(row=3,colomn=1)
btn3.grid(row=3,colomn=2)


mansLogs.mainloop()