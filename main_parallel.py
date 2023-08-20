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
original_length = 0.5

spring_constant_a = 5
spring_constant_b = 5

applied_force = 5

extension = tk.StringVar()
total_length = tk.StringVar()
combined_spring_constant = tk.StringVar()

#defining functions for calculating the equivalent spring constant and the extension
def calculate_combined_spring_constant_parallel(spring_constant_a, spring_constant_b):
    local_combined_spring_constant = spring_constant_a + spring_constant_b
    combined_spring_constant.set("{:.2f}".format(local_combined_spring_constant))
    return local_combined_spring_constant

def calculate_extension_parallel(original_length, spring_constant_a, spring_constant_b, applied_force):
    combined_spring_constant = calculate_combined_spring_constant_parallel(spring_constant_a, spring_constant_b)
    extension = original_length*applied_force/combined_spring_constant
    return extension

#definine the spring visualization functions
center_canvas = tk.Canvas(main_window, width=520, height=600, bg=accent_color)
center_canvas.place(x=240, y=0)

default_spring_length = 300
default_spring_width = 100

weight_width = 360
weight_height = 70

spring_a = center_canvas.create_rectangle(100, 0, 100+default_spring_width, 0+default_spring_length, width=3)
spring_b = center_canvas.create_rectangle(420-default_spring_width, 0, 420, 0+default_spring_length, width=3)

weight = center_canvas.create_rectangle(80, default_spring_length, 80+weight_width, default_spring_length+weight_height, width=3, fill=frame2_color)
weight_label = center_canvas.create_text(80+(weight_width/2), default_spring_length+(weight_height/2), font=font_big, text="test")

def visualize_spring_parallel():
    global spring_a, spring_b, weight, weight_label
    center_canvas.delete(spring_a, spring_b, weight, weight_label)

    original_length = float(original_length_input.get())
    local_total_length = float(total_length.get())
    percent_length = local_total_length/original_length
    spring_length = default_spring_length*original_length*percent_length
    weight_label_text = str(applied_force_input.get()) + "N"

    spring_a = center_canvas.create_rectangle(100, 0, 100+default_spring_width, spring_length, width=3)
    spring_b = center_canvas.create_rectangle(420-default_spring_width, 0, 420, spring_length, width=3)
    weight = center_canvas.create_rectangle(80, spring_length, 80+weight_width, spring_length+weight_height, width=3, fill=frame2_color)
    weight_label = center_canvas.create_text(80+(weight_width/2), spring_length+(weight_height/2), font=font_big, text=weight_label_text
                                             )

#defining update functions
def update_original_length(length):
    length = float(length)
    length = float(original_length_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force_input.get())

    local_extension =  calculate_extension_parallel(length, spring_constant_a, spring_constant_b, applied_force)
    extension.set("{:.2f}".format(local_extension))
    total_length.set("{:.2f}".format(length + local_extension))
    visualize_spring_parallel()
    
def update_spring_constant_a(spring_constant):
    length = float(original_length_input.get())
    spring_constant_a = float(spring_constant)
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force_input.get())

    local_extension =  calculate_extension_parallel(length, spring_constant_a, spring_constant_b, applied_force)
    extension.set("{:.2f}".format(local_extension))
    total_length.set("{:.2f}".format(length + local_extension))
    visualize_spring_parallel()

def update_spring_constant_b(spring_constant):
    length = float(original_length_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant)
    applied_force = float(applied_force_input.get())

    local_extension =  calculate_extension_parallel(length, spring_constant_a, spring_constant_b, applied_force)
    extension.set("{:.2f}".format(local_extension))
    total_length.set("{:.2f}".format(length + local_extension))
    visualize_spring_parallel()

def update_applied_force(applied_force):
    length = float(original_length_input.get())
    spring_constant_a = float(spring_constant_a_input.get())
    spring_constant_b = float(spring_constant_b_input.get())
    applied_force = float(applied_force)

    local_extension =  calculate_extension_parallel(length, spring_constant_a, spring_constant_b, applied_force)
    extension.set("{:.2f}".format(local_extension))
    total_length.set("{:.2f}".format(length + local_extension))
    visualize_spring_parallel()

#defining GUI elements
bar = tk.Frame(main_window, width=1000, height=150, bg=bar_color)
bar.place(x=0, y=600)

left_frame = tk.Frame(main_window, width=240, height=200, bg=frame_color)
left_frame.place(x=0, y=0)

left_2ndframe = tk.Frame(main_window, width=240, height=200, bg=frame_color)
left_2ndframe.place(x=0, y=400)

left_3rdframe = tk.Frame(main_window, width=240, height=200, bg=frame2_color)
left_3rdframe.place(x=0, y=200)

left_input_label = tk.Label(main_window, text="Spring A Inputs", font=font_big, bg=frame_color)
left_input_label.place(x=47, y=0)

spring_constant_a_label = tk.Label(main_window, text="Spring Constant (N/m)", font=("Arial", 14), bg=frame_color)
spring_constant_a_label.place(x=46, y=45)

spring_constant_a_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_a)
spring_constant_a_input.set(spring_constant_a)
spring_constant_a_input.place(x=15, y=75)

left_2ndinput_label = tk.Label(main_window, text="Spring B Inputs", font=font_big, bg=frame_color)
left_2ndinput_label.place(x=47, y=400)

spring_constant_b_label = tk.Label(main_window, text="Spring Constant (N/m)", font=("Arial", 14), bg=frame_color)
spring_constant_b_label.place(x=45, y=445)

spring_constant_b_input = tk.Scale(orient="horizontal", from_=0.5, to=10.0, resolution=0.5, length=200, bg=frame_color, troughcolor=accent_color, highlightthickness=0, command=update_spring_constant_b)
spring_constant_b_input.set(spring_constant_a)
spring_constant_b_input.place(x=15, y=475)

original_length_label = tk.Label(main_window, text="Original Length (m)", font=("Arial", 14), bg=frame2_color)
original_length_label.place(x=55, y=215)

original_length_input = tk.Scale(orient="horizontal", from_=0.01, to=1.0, resolution=0.01, length=200, bg=frame2_color, troughcolor=accent_color, highlightthickness=0, command=update_original_length)
original_length_input.set(original_length)
original_length_input.place(x=15, y=245)

applied_force_label = tk.Label(main_window, text="Applied Force (N)", font=("Arial", 14), bg=frame2_color)
applied_force_label.place(x=60, y=315)

applied_force_input = tk.Scale(orient="horizontal", from_=0, to=10, length=200, bg=frame2_color, troughcolor=accent_color, highlightthickness=0, command=update_applied_force)
applied_force_input.set(applied_force)
applied_force_input.place(x=15, y=345)

right_frame =  tk.Frame(main_window, width=240, height=600, bg=frame2_color)
right_frame.place(x=760, y=0)

right_output_label = tk.Label(text="Spring Outputs", font=font_big, bg=frame2_color)
right_output_label.place(x=790, y=0)

extension_label = tk.Label(main_window, text="Extension (m)", font=("Arial", 14), bg=frame2_color)
extension_label.place(x=825, y=45)

extension_output = tk.Label(main_window, textvariable=extension, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
extension_output.place(x=845, y=75)

total_length_label = tk.Label(main_window, text="Total Length (m)", font=("Arial", 14), bg=frame2_color)
total_length_label.place(x=817, y=140)

total_length_output = tk.Label(main_window, textvariable=total_length, font = ("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
total_length_output.place(x=845, y=170)

combined_spring_constant_label = total_length_label = tk.Label(main_window, text="Combined\nSpring Constant\n(N/m)", font=("Arial", 14), bg=frame2_color)
combined_spring_constant_label.place(x=816, y=225)

combined_spring_constant_output = tk.Label(main_window, textvariable=combined_spring_constant, font=("Arial", 14), bg=accent_color, height=1, width=6, justify="center")
combined_spring_constant_output.place(x=845, y=285)

def convert_seperate():
    main_window.destroy()
    s.Popen(['python','main_separate.py'])

to_separate = tk.Button(main_window, text="Seperate", font=('Arial',20),command=convert_seperate)
to_separate.place(x=320, y=660)

def convert_series():
    main_window.destroy()
    s.Popen(['python','main_series.py'])
to_series = tk.Button(main_window, text="Series", font=('Arial',20),command=convert_series)
to_series.place(x=453,y=660)

def convert_parallel():
    main_window.destroy()
    s.Popen(['python','main_parallel.py'])
to_parallel = tk.Button(main_window, text="Parallel",fg="orange", font=('Arial',20), command=convert_parallel)
to_parallel.place(x=560,y=660)

def backtomenu():
    main_window.destroy()
    s.Popen(['python','main_window.py'])
backtomenuwindow = tk.Button(main_window, text="🏠", font=('Arial',20), command=backtomenu)
backtomenuwindow.place(x=800,y=660)

#main window loop
main_window.mainloop()
