import tkinter as tk
import os
import subprocess as s

root = tk.Tk()
root.geometry("500x180")
root.title("Credits")
root.resizable(False,False)

subtitle_text = "Pang Gui Rou \nEmmanuel Sipawol Lennon Egedius \nAlaa Elghifari \nLee Yoonjae \nBeverly Wong Zhi Wei"
subtitle_label = tk.Label(root, text=subtitle_text, font=("Arial", 31), fg="white", bg="turquoise")
subtitle_label.place(x=255,y=90, anchor="center")

def backtomenu():
    root.destroy()
backtomenuwindow = tk.Button(root, text="Exit", font=('Arial',15), command=backtomenu)
backtomenuwindow.place(x=430,y=140)


root.mainloop()