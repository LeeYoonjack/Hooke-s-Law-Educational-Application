import os.path
import tkinter as tk
from PIL import ImageTk, Image
import subprocess as s

main_window = tk.Tk()
main_window.title("Hooke's Law")
main_window.geometry("1000x750")
main_window.resizable(width=False, height=False)

left_frame = tk.Frame(main_window, width=400, height=750, bg="turquoise")
left_frame.place(x=0, y=0)

right_frame = tk.Frame(main_window, width=600, height=750, bg="white")
right_frame.place(x=400, y=0)

title_label = tk.Label(left_frame, text="Hooke's Law", font=("Arial", 50), fg="white", bg="turquoise")
title_label.place(relx=0.5, rely=0.3, anchor="center")

image_file = "Hooke.jpg"
img = Image.open(image_file)
img = img.resize((600, 800))
photo = ImageTk.PhotoImage(img)

image_label = tk.Label(right_frame, image=photo, bg="white")
image_label.place(relx=0.5, rely=0.5, anchor="center")
image_label.photo = photo


def openquiz():
    main_window.destroy()
    s.Popen(['python',"Python Hooke's Law Q&A.py"])
quiz_button = tk.Button(left_frame, text="Quiz", font=("Arial", 20), bg="white", fg="turquoise",command=openquiz)
quiz_button.place(relx=0.5, rely=0.7, anchor="center")

quit = main_window.destroy
quit_button = tk.Button(left_frame, text="Exit", font=("Arial", 20), bg="white", fg="turquoise", command=quit)
quit_button.place(relx=0.5, rely=0.9, anchor="center")

def openseriesexperiment():
    main_window.destroy()
    s.Popen(['python',"main_separate.py"])
experiment_button = tk.Button(left_frame, text="Simulation", font=("Arial", 20), bg="white", fg="turquoise",command=openseriesexperiment)
experiment_button.place(relx=0.5, rely=0.6, anchor="center")

def opentheory():
    main_window.destroy()
    s.Popen(['python',"Theory.py"])
learn_button = tk.Button(left_frame, text="Learn Theory", font=("Arial", 20), bg="white", fg="turquoise",command=opentheory)
learn_button.place(relx=0.5, rely=0.5, anchor="center")

def opencredit():
    s.run(["python",os.path.realpath(os.path.dirname(__file__))+"/Credit part.py"])
credit_button = tk.Button(left_frame, text="Credits",font=("Arial", 20), bg="white", fg="turquoise",command=opencredit)
credit_button.place(relx=0.5, rely=0.8,anchor="center")





main_window.mainloop()
