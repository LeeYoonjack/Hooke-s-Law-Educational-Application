import tkinter
import tkinter as tk
import os
import subprocess as s

root = tk.Tk()
root.geometry("1000x750")
root.title("Test Yourself!")
root.resizable(False,False)

def gobactomain():
    root.destroy()
    s.Popen(['python', 'main_window.py'])
gomain = tk.Button(root,text="🏠",command=gobactomain)
gomain.place(x=630,y=30)

score=0

navy = tk.Frame(root, width=100, height=750, bg="#023047")
navy.place(x=900,y=0)
blue = tk.Frame(root, width=100, height=800, bg="#219EBC")
blue.place(x=800,y=0)
orange = tk.Frame(root, width=60, height=800, bg="#EE8434")
orange.place(x=750,y=0)

header= tk.Label(root, text='Time to Test Yourself',font=("Bradley Hand", 30))
header.place(x=30,y=10)

def submit_answer():
    global score

    if var1.get() == 1:
        message_1.config(text="Ans: Correct✅")
        score+=1
    else:
        message_1.config(text="Ans Incorrect❗")

    if var2.get() == 4:
        message_2.config(text="Ans: Correct✅")
        score+=1
    else:
        message_2.config(text="Ans: Incorrect❗")

    if var3.get() == 2:
        message_3.config(text="Ans: Correct✅")
        score+=1
    else:
        message_3.config(text="Ans: Incorrect❗️")

    if var4.get() == 2:
        message_4.config(text="Ans: Correct✅")
        score+=1
    else:
        message_4.config(text="Ans: Incorrect❗")

    if var5.get() == 3:
        message_5.config(text="Ans: Correct✅")
        score+=1
    else:
        message_5.config(text="Ans: Incorrect❗")

def total_mark():
    global score
    total_score.config(text=f"You scored {score} out of 5 questions!")

submit_all = tk.Button(root, text='Submit all', command=lambda:[submit_answer(), total_mark()])
submit_all.place(x=550, y=570)

total_score = tk.Label(root, text="", font=("Arial", 25))
total_score.place(x=300, y=660)

# First Question
first_question = tk.Label(root, text=" 1. Determine the spring constant if a force of 100 N is stretching a spring by 0.8 m.")
first_question.place(x=20,y=70)

var1 = tk.IntVar()
answer1_1 = tk.Radiobutton(root, text="125", variable=var1, value=1, padx=20, pady=5)
answer1_2 = tk.Radiobutton(root, text="80", variable=var1, value=2, padx=20, pady=3)
answer1_3 = tk.Radiobutton(root, text="12.5", variable=var1, value=3, padx=20, pady=3)

answer1_1.place(x=32,y=90)
answer1_2.place(x=30.5,y=115)
answer1_3.place(x=30,y=140)

message_1 = tk.Label(root, text="")
message_1.place(x=465,y=140)

# Second Question
second_question = tk.Label(root, text=" 2. If F is force, k is spring constant and x is extension, Hooke's Law tells us that:")
second_question.place(x=20,y=170)

var2 = tk.IntVar()
answer2_1 = tk.Radiobutton(root, text="F=k/x", variable=var2, value=1, padx=20, pady=5)
answer2_2 = tk.Radiobutton(root, text="k=Fx", variable=var2, value=2, padx=20, pady=3)
answer2_3 = tk.Radiobutton(root, text="F=kx", variable=var2, value=3, padx=20, pady=3)

answer2_1.place(x=32,y=190)
answer2_2.place(x=30.5,y=215)
answer2_3.place(x=30.5,y=240)

message_2 = tk.Label(root, text="")
message_2.place(x=465,y=240)


# Third Question
third_question = tk.Label(root, text=" 3. What is the spring constant of a spring that needs a force of 3 N to becompressed from 40 cm to 35 cm?")
third_question.place(x=20,y=270)

var3 = tk.IntVar()
answer3_1 = tk.Radiobutton(root, text="-60 N", variable=var3, value=1, padx=20, pady=5)
answer3_2 = tk.Radiobutton(root, text="60 N/m", variable=var3, value=2, padx=20, pady=3)
answer3_3 = tk.Radiobutton(root, text="0.6 N/m", variable=var3, value=3, padx=20, pady=3)

answer3_1.place(x=32,y=290)
answer3_2.place(x=30.5,y=315)
answer3_3.place(x=30.5,y=340)

message_3 = tk.Label(root, text="")
message_3.place(x=465,y=340)


# Fourth Question
fourth_question = tk.Label(root, text=" 4. Will a weak spring have a big or small constant?")
fourth_question.place(x=20,y=370)

var4 = tk.IntVar()
answer4_1 = tk.Radiobutton(root, text="Big", variable=var4, value=1, padx=20, pady=5)
answer4_2 = tk.Radiobutton(root, text="Small", variable=var4, value=2, padx=20, pady=3)

answer4_1.place(x=32,y=390)
answer4_2.place(x=30.5,y=415)

message_4 = tk.Label(root, text="")
message_4.place(x=465,y=415)

#Fifth Question
fifth_question= tk.Label(root, text=" 5. A spring extends 1.5m under load 10N. What is its spring constant?")
fifth_question.place(x=20,y=445)

var5= tk.IntVar()
answer5_1 = tk.Radiobutton(root, text="15N/m", variable=var5, value=1, padx=20, pady=5)
answer5_2 = tk.Radiobutton(root, text="0.15N/m", variable=var5, value=2, padx=20, pady=3)
answer5_3 = tk.Radiobutton(root, text="6.7N/m", variable=var5, value=3, padx=20, pady=3)

answer5_1.place(x=32,y=465)
answer5_2.place(x=30.5,y=490)
answer5_3.place(x=30.5,y=515)


message_5= tk.Label(root, text="")
message_5.place(x=465,y=515)

#https://reviewgamezone.com/mc/candidate/test/?test_id=41480
#https://quizizz.com/admin/quiz/5804e7b6f877a9664f636365/hooke's-law-(ww)?ctaSource=show-answers&fromPage=admin-quizType-id-slug

def restart_window():
    root.destroy()
    s.Popen(['python',"Python Hooke's Law Q&A.py"])
retry_button = tk.Button(root, text="Retry", command=restart_window)
retry_button.place(x=550, y=600)


def show_answers():
    # create a new window to display the answers
    answer_window = tk.Toplevel(root)
    answer_window.title("Answers")
    answer_window.geometry("500x600")

    navy = tk.Frame(answer_window, width=90, height=600, bg="#023047")
    navy.place(x=410,y=0)
    blue = tk.Frame(answer_window, width=75, height=600, bg="#219EBC")
    blue.place(x=340,y=0)
    orange = tk.Frame(answer_window, width=60, height=600, bg="#EE8434")
    orange.place(x=280,y=0)

    solution = tk.Label(answer_window, text="Solutions", font=("Times New Roman",50))
    solution.grid(row=0, column=0, columnspan=8, padx=20)


    first_answer = tk.Label(answer_window, text="1.  F= 100N    x=0.8m\n100= k(0.8)\nk = 125N/M\n", font=("Times New Roman",24))
    first_answer.grid(row=1, column=0, sticky="w")

    second_answer = tk.Label(answer_window, text="2.  F = kx\n", font=("Times New Roman",24))
    second_answer.grid(row=2, column=0, sticky="w")

    third_answer = tk.Label(answer_window, text="3.  F= 3N      x= 0.05m\n3= k(0.05)\nk = 60N/M\n", font=("Times New Roman",24))
    third_answer.grid(row=3, column=0, sticky="w")

    fourth_answer = tk.Label(answer_window, text="4. Small\n", font=("Times New Roman",24))
    fourth_answer.grid(row=4, column=0, sticky="w")

    fifth_answer = tk.Label(answer_window, text="5.  F= 10N     x= 1.5m\n10= k(1.5)\nk = 6.7N/M\n", font=("Times New Roman",24))
    fifth_answer.grid(row=5, column=0, sticky="w")


#create a button to show the answers
answer = tk.Button(root, text="Show Answers", command=show_answers)
answer.place(x=550, y=630)



root.mainloop()
