import tkinter as tk
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
font_small = ("Arial", 12)

#defining variables
original_length_a = 0.5
spring_constant_a = 5
applied_force_a = 5

original_length_b = 0.5
spring_constant_b = 5
applied_force_b = 5

extension_a = tk.StringVar()
total_length_a = tk.StringVar()

extension_b = tk.StringVar()
total_length_b = tk.StringVar()

#defining functions for calculating the extension
def calculate_extension_separate(original_length, spring_constant, applied_force):
    extension = original_length*applied_force/spring_constant
    return extension

#defining the spring visualization functions
center_canvas = tk.Canvas(main_window, width=520, height=600, bg=accent_color)
center_canvas.place(x=240, y=0)

default_spring_length = 300
default_spring_width = 100

weight_width = 140
weight_height = 70

spring_a = center_canvas.create_rectangle(100, 0, 100+default_spring_width, 0+default_spring_length, width=3)
spring_b = center_canvas.create_rectangle(420-default_spring_width, 0, 420, 0+default_spring_length, width=3)

weight_a = center_canvas.create_rectangle(80, default_spring_length, 80+weight_width, default_spring_length+weight_height, width=3, fill=frame2_color)
weight_b = center_canvas.create_rectangle(300, default_spring_length, 300+weight_width, default_spring_length+weight_height, width=3, fill=frame2_color)

weight_label_a = center_canvas.create_text(80+(weight_width/2), default_spring_length+(weight_height/2), font=font_big, text="test")
weight_label_b = center_canvas.create_text(300+(weight_width/2), default_spring_length+(weight_height/2), font=font_big, text="test")

def visualize_spring_a():
    global spring_a, weight_a, weight_label_a
    center_canvas.delete(spring_a, weight_a, weight_label_a)
    
    original_length = float(original_length_a_input.get())
    total_length = float(total_length_a.get())
    percent_length = total_length/original_length
    spring_length = default_spring_length*original_length*percent_length
    weight_label_text = str(applied_force_a_input.get()) + "N"

    spring_a = center_canvas.create_rectangle(100, 0, 100+default_spring_width, spring_length, width=3)
    weight_a = center_canvas.create_rectangle(80, spring_length, 80+weight_width, spring_length+weight_height, width=3, fill=frame2_color)
    weight_label_a = center_canvas.create_text(80+(weight_width/2), spring_length+(weight_height/2), font=font_big, text=weight_label_text)

def visualize_spring_b():
    global spring_b, weight_b, weight_label_b
    center_canvas.delete(spring_b, weight_b, weight_label_b)
    
    original_length = float(original_length_b_input.get())
    total_length = float(total_length_b.get())
    percent_length = total_length/original_length
    spring_length = default_spring_length*original_length*percent_length
    weight_label_text= str(applied_force_b_input.get()) + "N"
    
    spring_b = center_canvas.create_rectangle(420-default_spring_width, 0, 420, spring_length, width=3)
    weight_b = center_canvas.create_rectangle(400-default_spring_width, spring_length, 400-default_spring_width+weight_width, spring_length+weight_height, width=3, fill=frame2_color)
    weight_label_b = center_canvas.create_text(400-default_spring_width+(weight_width/2), spring_length+(weight_height/2), font=font_big, text=weight_label_text)

#defining update functions
def update_original_length_a(length):
    length = float(length)
    spring_constant = float(spring_constant_a_input.get())
    applied_force = float(applied_force_a_input.get())
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_a.set("{:.2f}".format(local_extension))
    total_length_a.set("{:.2f}".format(length + local_extension))
    visualize_spring_a()

def update_spring_constant_a(spring_constant):
    length = float(original_length_a_input.get())
    spring_constant = float(spring_constant)
    applied_force = float(applied_force_a_input.get())
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_a.set("{:.2f}".format(local_extension))
    total_length_a.set("{:.2f}".format(length + local_extension))
    visualize_spring_a()

def update_applied_force_a(applied_force):
    length = float(original_length_a_input.get())
    spring_constant = float(spring_constant_a_input.get())
    applied_force = float(applied_force)
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_a.set("{:.2f}".format(local_extension))
    total_length_a.set("{:.2f}".format(length + local_extension))
    visualize_spring_a()

def update_original_length_b(length):
    length = float(length)
    applied_force = float(applied_force_b_input.get())
    spring_constant = float(spring_constant_b_input.get())
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_b.set("{:.2f}".format(local_extension))
    total_length_b.set("{:.2f}".format(length + local_extension))
    visualize_spring_b()

def update_spring_constant_b(spring_constant):
    length = float(original_length_b_input.get())
    spring_constant = float(spring_constant)
    applied_force = float(applied_force_b_input.get())
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_b.set("{:.2f}".format(local_extension))
    total_length_b.set("{:.2f}".format(length + local_extension))
    visualize_spring_b()

def update_applied_force_b(applied_force):
    length = float(original_length_b_input.get())
    spring_constant = float(spring_constant_b_input.get())
    applied_force = float(applied_force)
    local_extension = calculate_extension_separate(length, spring_constant, applied_force)
    extension_b.set("{:.2f}".format(local_extension))
    total_length_b.set("{:.2f}".format(length + local_extension))
    visualize_spring_b()

#defining GUI elements
left_frame = tk.Frame(main_window, width=240, height=300, bg=frame_color)
left_frame.place(x=0, y=0)

left_2ndframe = tk.Frame(main_window, width=240, height=300, bg=frame2_color)
left_2ndframe.place(x=0, y=300)

right_frame = tk.Frame(main_window, width=240, height=300, bg=frame_color)
right_frame.place(x=760, y=0)

right_2ndframe = tk.Frame(main_window, width=240, height=300, bg=frame2_color)
right_2ndframe.place(x=760, y=300)

bar = tk.Frame(main_window, width=1000, height=150, bg=bar_color)
bar.place(x=0, y=600)

left_input_label = tk.Label(main_window, text="Spring A Inputs", font=font_big, bg=frame_color)
left_input_label.place(x=25, y=0)

left_output_label = tk.Label(main_window, text="Spring A Outputs", font=font_big, bg=frame2_color)
left_output_label.place(x=25, y=300)

original_length_a_label = tk.Label(main_window, text="Original Length (m)", font=("Arial", 14), bg=frame_color)
original_length_a_label.place(x=30, y=45)

spring_constant_a_label = tk.Label(main_window, text="Spring Constant (N/m)", font=("Arial", 14), bg=frame_color)
spring_constant_a_label.place(x=45, y=120)

applied_force_a_label = tk.Label(main_window, text="Applied Force (N)", font=("Arial", 14), bg=frame_color)
applied_force_a_label.place(x=45, y=200)

original_length_a_input = tk.Scale(orient="horizontal", from_=0.01, to=1.0, resolution=0.01, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_original_length_a)
original_length_a_input.set(original_length_a)
original_length_a_input.place(x=15, y=75)

spring_constant_a_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_a)
spring_constant_a_input.set(spring_constant_a)
spring_constant_a_input.place(x=15, y=150)

applied_force_a_input = tk.Scale(orient="horizontal", from_=0, to=10, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_applied_force_a)
applied_force_a_input.set(applied_force_a)
applied_force_a_input.place(x=15, y=230)

right_output = tk.Label(main_window, text="Spring B Outputs", font=font_big, bg=frame2_color)
right_output.place(x=785, y=300)

right_input = tk.Label(main_window, text="Spring B Inputs", font=font_big, bg=frame_color)
right_input.place(x=785, y=0)

original_length_b_label = tk.Label(main_window, text="Original Length (m)", font=("Arial", 14), bg=frame_color)
original_length_b_label.place(x=790, y=45)

spring_constant_b_label = tk.Label(main_window, text="Spring Constant (N/m)", font=("Arial", 14), bg=frame_color)
spring_constant_b_label.place(x=805, y=120)

applied_force_b_label = tk.Label(main_window, text="Applied Force (N)", font=("Arial", 14), bg=frame_color)
applied_force_b_label.place(x=805, y=200)

original_length_b_input = tk.Scale(orient="horizontal", from_=0.01, to=1.0, resolution=0.01, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_original_length_b)
original_length_b_input.set(original_length_b)
original_length_b_input.place(x=775, y=75)

spring_constant_b_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_b)
spring_constant_b_input.set(spring_constant_b)
spring_constant_b_input.place(x=775, y=150)

applied_force_b_input = tk.Scale(orient="horizontal", from_=0, to=10, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_applied_force_b)
applied_force_b_input.set(applied_force_b)
applied_force_b_input.place(x=775, y=230)

extension_a_label = tk.Label(main_window, text="Extension (m)", font=("Arial", 14), bg=frame2_color)
extension_a_label.place(x=55, y=350)

extension_a_output = tk.Label(main_window, textvariable=extension_a, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
extension_a_output.place(x=80, y=390)

total_length_a_label = tk.Label(main_window, text="Total Length (m)", font=("Arial", 14), bg=frame2_color)
total_length_a_label.place(x=50, y=430)

total_length_a_output = tk.Label(main_window, textvariable=total_length_a, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
total_length_a_output.place(x=80, y=480)

extension_b_label = tk.Label(main_window, text="Extension (m)", font=("Arial", 14), bg=frame2_color)
extension_b_label.place(x=815, y=350)

extension_b_output = tk.Label(main_window, textvariable=extension_b, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
extension_b_output.place(x=840, y=390)


total_length_b_label = tk.Label(main_window, text="Total Length (m)", font=("Arial", 14), bg=frame2_color)
total_length_b_label.place(x=810, y=430)

total_length_b_output = tk.Label(main_window, textvariable=total_length_b, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
total_length_b_output.place(x=840, y=480)

def convert_seperate():
    main_window.destroy()
    s.Popen(['python','main_separate.py'])

to_separate = tk.Button(main_window, text="Seperate",fg="orange", font=('Arial',20),command=convert_seperate)
to_separate.place(x=320, y=660)

def convert_series():
    main_window.destroy()
    s.Popen(['python','main_series.py'])
to_series = tk.Button(main_window, text="Series", font=('Arial',20),command=convert_series)
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


main_window.mainloop()
