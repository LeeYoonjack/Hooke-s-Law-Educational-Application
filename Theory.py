import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess as s
import os
from tkinter.font import ITALIC

cont='Welcome! This tool allows you to explore the relationship between the force applied to a spring,the spring\n\
constant,and the subsequent deformation. The interface includes two different options for experimenting with\n\
Hooke’s Law:'

main_window = tk.Tk()
main_window.title("Read Theory")
main_window.geometry("1000x750")
main_window.resizable(width=False, height=False)

navy = tk.Frame(main_window, width=100, height=750, bg="#023047")
navy.place(x=0,y=0)
blue = tk.Frame(main_window, width=100, height=800, bg="#219EBC")
blue.place(x=100,y=0)
orange = tk.Frame(main_window, width=60, height=800, bg="#EE8434")
orange.place(x=200,y=0)

title=Label(main_window, text="Hooke's Law", font=('Times New Roman', 25))
title.place(x=580, y=10)

intro=Label(main_window, text="Introduction", font=('Times New Roman', 11, 'underline'))
intro.place(x=280,y =50)

introcontent1=Label(main_window, text=cont, font=('Times New Roman', 11), justify='left')
introcontent1.place(x=280,y=69)

springs=Label(main_window, text="1.Single Spring\n2.Two Springs in Parallel\n3. Two Springs in Series" ,font=('Times New Roman',11),justify='left')
springs.place(x=300,y=130)

introcontent2=Label(main_window, text="Hooke’s Law is a principle related to elasticity. It states that the force applied to a spring is directly proportional\n\
to the change in length or deformation of the spring.The given equation can be expressed by:", font=('Times new roman',11), justify='left')
introcontent2.place(x=280,y=190)

introcontent3=Label(main_window, text="F = kx", font=('Cambria',14, ITALIC),justify='center')
introcontent3.place(x=600,y=235)

introcontent4=Label(main_window, text="Where F refers to the force applied to the spring, k is the spring constant, and x is the displacement of the spring\n\
from its initial position.",font=('Times new roman',11),justify='left')
introcontent4.place(x=280,y=265)

equation1=Label(main_window, text="Equation\n",font=('times new roman',11,UNDERLINE))
equation1.place(x=280,y=326)

equationtitle1=Label(main_window, text='Single Spring :',font=('times new roman',11))
equationtitle1.place(x=280,y=345)


table1 = ttk.Treeview(main_window, columns=("col1", "col2", "col3"), show="headings", height=1)

table1.heading("col1", text="Spring Displacement, x",anchor='center')
table1.heading("col2", text="Force Applied, F",anchor='center')
table1.heading("col3", text="Spring Constant, k",anchor='center')

table1.column("col1", width=220,anchor='center')
table1.column("col2", width=220,anchor='center')
table1.column("col3", width=220,anchor='center')

table1.insert("", "end", values=("x = F/k", "F = kx", "k = F/x"))
table1.place(x=280, y=365)

equationtitle2=Label(main_window, text='Two Springs in Parallel :', font=('times new roman',11))
equationtitle2.place(x=280,y=425)

table2 = ttk.Treeview(main_window, columns=("col1", "col2", "col3"), show="headings", height=1)

table2.heading("col1", text="Spring Displacement, x",anchor='center')
table2.heading("col2", text="Force Applied, F",anchor='center')
table2.heading("col3", text="Spring Constant, k",anchor='center')

table2.column("col1", width=220,anchor='center')
table2.column("col2", width=220,anchor='center')
table2.column("col3", width=220,anchor='center')

table2.insert("", "end", values=("x1 = X2", "FTotal = k1 x1 + k2 x2", "kTotal = k1 + k2"))
table2.place(x=280, y=444)

equation2=Label(main_window, text='To find the spring displacement when two springs are parallel, we must understand that both springs are attached\n\
to the same weight.Therefore, the two springs will have the same displacement value. Hence, we can substitute\n\
the values of the force applied and the spring constant into the equation: FTotal = k1 x1 + k2 x2 ,\n\
to find the value of the springs.',font=('times new roman',11),justify='left')
equation2.place(x=280,y=490)

equationtitle3=Label(main_window, text='Two Springs in Series :', font=('Times new roman',11),justify='left')
equationtitle3.place(x=280,y=570)

table3 = ttk.Treeview(main_window, columns=("col1", "col2", "col3"), show="headings", height=1)

table3.heading("col1", text="Spring Displacement, x",anchor='center')
table3.heading("col2", text="Force Applied, F",anchor='center')
table3.heading("col3", text="Spring Constant, k",anchor='center')

table3.column("col1", width=220,anchor='center')
table3.column("col2", width=220,anchor='center')
table3.column("col3", width=220,anchor='center')

table3.insert("", "end", values=("x = FTotal / kTotal", "FTotal  = F1 = F2", "1/kTotal = 1/k 1 + 1/k2"))
table3.place(x=280, y=590)

equation3=Label(main_window, text='The displacement of the two springs in series is equal to the sum of their individual displacements( x1 and x2),\n\
and the applied total force is the same for both of the springs (FTotal). However for the equivalent spring\n\
constant, it is the reciprocal of the sum of the reciprocals the two separate spring constants (k1  and k2).',font=('times new roman',11,), justify='left')
equation3.place(x=280,y=639)

def backtomain():
    main_window.destroy()
    s.Popen(['python',"main_window.py"])
backtomain = tk.Button(main_window, text="🏠", font=('Arial', 15), command=backtomain)
backtomain.place(x=880, y=20)


main_window.mainloop()
