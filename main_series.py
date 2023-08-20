import tkinter as tk
from tkinter import ttk
import subprocess as s

main_window = tk.Tk()
main_window.title("Hooke's Law Simulation")
main_window.geometry("1000x750")
main_window.resizable(width=False, height=False)

#defining colors and fonts
frame_color = "#EE8434"
frame2_color = "#219EBC"
bar_color = "#023047"
accent_color = "#FDF0D5"

font_big = ("Arial", 18, "bold")
font_small = ("Arial", 14)

#defining variables
original_length_a = 0.5
spring_constant_a = 5

original_length_b = 0.5
spring_constant_b = 5

applied_force = 5

extension_a = tk.StringVar()
extension_b = tk.StringVar()
extension = tk.StringVar()

total_length_a = tk.StringVar()
total_length_b = tk.StringVar()
total_length = tk.StringVar()

combined_spring_constant = tk.StringVar()

#defining functions for calculating the equivalent spring constant and the extension
def calculate_extension(original_length, spring_constant, applied_force):
    extension = original_length*applied_force/spring_constant
    return extension
    
#defining the spring visualization functions
center_canvas = tk.Canvas(main_window, width=520, height=600, bg=accent_color)
center_canvas.place(x=240, y=0)

default_spring_length = 150
default_spring_width = 100

weight_width = 140
weight_height = 70

spring_a = center_canvas.create_rectangle(210, 0, 210+default_spring_width, default_spring_length, width=3)
spring_b = center_canvas.create_rectangle(210, default_spring_length, 210+default_spring_width, default_spring_length*2, width=3, outline=frame_color)

weight = center_canvas.create_rectangle(190, default_spring_length*2, 190+weight_width, default_spring_length*2+weight_height, width=3, fill=frame2_color)
weight_label = center_canvas.create_text(190+(weight_width/2), default_spring_length*2+(weight_height/2), font=font_big, text="test")

def visualize_spring_series():
    global spring_a, spring_b, weight, weight_label
    center_canvas.delete(spring_a, spring_b, weight, weight_label)

    original_length_a = float(original_length_a_input.get())
    local_total_length_a = float(total_length_a.get())
    percent_length_a = local_total_length_a/original_length_a
    spring_length_a = default_spring_length*original_length_a*percent_length_a

    original_length_b = float(original_length_b_input.get())
    local_total_length_b = float(total_length_b.get())
    percent_length_b = local_total_length_b/original_length_b
    spring_length_b = default_spring_length*original_length_b*percent_length_a

    weight_label_text =  str(applied_force_input.get()) + "N"

    spring_a = center_canvas.create_rectangle(210, 0, 210+default_spring_width, spring_length_a, width=3)
    spring_b = center_canvas.create_rectangle(210, spring_length_a, 210+default_spring_width, spring_length_a+spring_length_b, width=3, outline=frame_color)
    weight = center_canvas.create_rectangle(190, spring_length_a+spring_length_b, 190+weight_width, spring_length_a+spring_length_b+weight_height, width=3, fill=frame2_color)
    weight_label = center_canvas.create_text(190+(weight_width/2), spring_length_a+spring_length_b+(weight_height/2), font=font_big, text=weight_label_text)

#defining update functions
def update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force):
    local_extension_a = calculate_extension(length_a, spring_constant_a, applied_force)
    local_total_length_a = length_a + local_extension_a

    local_extension_b = calculate_extension(length_b, spring_constant_b, applied_force)
    local_total_length_b = length_b + local_extension_b

    local_extension = local_extension_a + local_extension_b
    local_total_length = local_total_length_a + local_total_length_b

    local_combined_spring_constant = 1/((1/spring_constant_a)+(1/spring_constant_b))

    extension_a.set("{:.2f}".format(local_extension_a))
    extension_b.set("{:.2f}".format(local_extension_b))
    extension.set("{:.2f}".format(local_extension))

    total_length_a.set("{:.2f}".format(local_total_length_a))
    total_length_b.set("{:.2f}".format(local_total_length_b))
    total_length.set("{:.2f}".format(length_a + length_b + local_extension))

    combined_spring_constant.set("{:.2f}".format(local_combined_spring_constant))

    visualize_spring_series()

def update_original_length_a(length):
    length_a = float(length)
    length_b = float(original_length_b_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force_input.get())

    update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force)

def update_spring_constant_a(spring_constant):
    length_a = float(original_length_a_input.get())
    length_b = float(original_length_b_input.get())
    spring_constant_a = float(spring_constant)
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force_input.get())
    
    update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force)

def update_original_length_b(length):
    length_a = float(original_length_a_input.get())
    length_b = float(length)
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force_input.get())

    update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force)

def update_spring_constant_b(spring_constant):
    length_a = float(original_length_a_input.get())
    length_b = float(original_length_b_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant)
    applied_force = float(applied_force_input.get())

    update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force)

def update_applied_force(applied_force):
    length_a = float(original_length_a_input.get())
    length_b = float(original_length_b_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force)

    update(length_a, length_b, spring_constant_a, spring_constant_b, applied_force)

#defining GUI elements
bar = tk.Frame(main_window, width=1000, height=150, bg=bar_color)
bar.place(x=0, y=600)

left_frame = tk.Frame(main_window, width=240, height=240, bg=frame_color)
left_frame.place(x=0, y=0)

left_2ndframe = tk.Frame(main_window, width=240, height=240, bg=frame_color)
left_2ndframe.place(x=0, y=360)

left_3rdframe = tk.Frame(main_window, width=240, height=120, bg=frame2_color)
left_3rdframe.place(x=0, y=240)

left_input_label = tk.Label(main_window, text="Spring A Inputs", font=font_big, bg=frame_color)
left_input_label.place(x=47, y=0)

original_length_a_label = tk.Label(main_window, text="Original Length (m)", font=font_small, bg=frame_color)
original_length_a_label.place(x=50, y=45)

original_length_a_input = tk.Scale(orient="horizontal", from_=0.01, to=1.0, resolution=0.01, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_original_length_a)
original_length_a_input.set(original_length_a)
original_length_a_input.place(x=15, y=75)

spring_constant_a_label = tk.Label(main_window, text="Spring Constant (N/m)", font=font_small, bg=frame_color)
spring_constant_a_label.place(x=47, y=140)

spring_constant_a_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_a)
spring_constant_a_input.set(spring_constant_a)
spring_constant_a_input.place(x=15, y=170)

left_2ndinput_label = tk.Label(main_window, text="Spring B Inputs", font=font_big, bg=frame_color)
left_2ndinput_label.place(x=47, y=360)

original_length_b_label = tk.Label(main_window, text="Original Length (m)", font=font_small, bg=frame_color)
original_length_b_label.place(x=50, y=405)

original_length_b_input = tk.Scale(orient="horizontal", from_=0.01, to=1.0, resolution=0.01, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_original_length_b)
original_length_b_input.set(original_length_b)
original_length_b_input.place(x=15, y=435)

spring_constant_b_label = tk.Label(main_window, text="Spring Constant (N/m)", font=font_small, bg=frame_color)
spring_constant_b_label.place(x=43, y=500)

spring_constant_b_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_b)
spring_constant_b_input.set(spring_constant_b)
spring_constant_b_input.place(x=15, y=530)

applied_force_label = tk.Label(main_window, text="Applied Force (N)", font=font_small, bg=frame2_color)
applied_force_label.place(x=55, y=260)

applied_force_input = tk.Scale(orient="horizontal", from_=0, to=10, length=200, bg=frame2_color, troughcolor=accent_color, highlightthickness=0, command=update_applied_force)
applied_force_input.set(applied_force)
applied_force_input.place(x=15, y=290)

right_frame = tk.Frame(main_window, width=240, height=600, bg=frame2_color)
right_frame.place(x=760, y=0)

right_output_label = tk.Label(text="Spring Outputs", font=font_big, bg=frame2_color)
right_output_label.place(x=810, y=0)

extension_label = tk.Label(main_window, text="Total Extension (m)", font=font_small, bg=frame2_color)
extension_label.place(x=805, y=45)

extension_output = tk.Label(main_window, textvariable=extension, font = font_small, bg=accent_color, height=1, width=6, justify="center")
extension_output.place(x=845, y=75)

total_length_label = tk.Label(main_window, text="Total Length (m)", font=font_small, bg=frame2_color)
total_length_label.place(x=810, y=120)

total_length_output = tk.Label(main_window, textvariable=total_length, font = font_small, bg=accent_color, height=1, width=6, justify="center")
total_length_output.place(x=845, y=150)

combined_spring_constant_label = total_length_label = tk.Label(main_window, text="Combined\nSpring Constant", font=font_small, bg=frame2_color)
combined_spring_constant_label.place(x=810, y=190)

combined_spring_constant_output = tk.Label(main_window, textvariable=combined_spring_constant, font=font_small, bg=accent_color, height=1, width=6, justify="center")
combined_spring_constant_output.place(x=845, y=240)

extension_a_label = tk.Label(main_window, text="Extension A (m)", font=font_small, bg=frame2_color)
extension_a_label.place(x=810, y=280)

extension_a_output = tk.Label(main_window, textvariable=extension_a, font =font_small, bg=accent_color, height=1, width=6, justify="center")
extension_a_output.place(x=845, y=310)

total_length_a_label = tk.Label(main_window, text="Length A (m)", font=font_small, bg=frame2_color)
total_length_a_label.place(x=810, y=355)

total_length_a_output = tk.Label(main_window, textvariable=total_length_a, font =font_small, bg=accent_color, height=1, width=6, justify="center")
total_length_a_output.place(x=845, y=385)

extension_b_label = tk.Label(main_window, text="Extension B (m)", font=font_small, bg=frame2_color)
extension_b_label.place(x=815, y=430)

extension_b_output = tk.Label(main_window, textvariable=extension_b, font =font_small, bg=accent_color, height=1, width=6, justify="center")
extension_b_output.place(x=845, y=460)

total_length_b_label = tk.Label(main_window, text="Length B (m)", font=font_small, bg=frame2_color)
total_length_b_label.place(x=815, y=505)

total_length_b_output = tk.Label(main_window, textvariable=total_length_b, font =font_small, bg=accent_color, height=1, width=6, justify="center")
total_length_b_output.place(x=845, y=545)

def convert_seperate():
    main_window.destroy()
    s.Popen(['python','main_separate.py'])

to_separate = tk.Button(main_window, text="Seperate", font=('Arial',20),command=convert_seperate)
to_separate.place(x=320, y=660)

def convert_series():
    main_window.destroy()
    s.Popen(['python','main_series.py'])
to_series = tk.Button(main_window, text="Series",fg="orange" ,font=('Arial',20),command=convert_series)
to_series.place(x=453,y=660)

def convert_parallel():
    main_window.destroy()
    s.Popen(['python','main_parallel.py'])
to_parallel = tk.Button(main_window, text="Parallel", font=('Arial',20), command=convert_parallel)
to_parallel.place(x=560,y=660)

def backtomenu():
    main_window.destroy()
    s.Popen(['python','main_window.py'])
backtomenuwindow = tk.Button(main_window, text="🏠", font=('Arial',20), command=backtomenu)
backtomenuwindow.place(x=800,y=660)

#main window loop
main_window.mainloop()
