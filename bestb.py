from tkinter import *
import ttkbootstrap as ttk


def convert():
    miles_input = txt_int.get()
    kilo_output = miles_input * 1.61
    lbl_output_string.set(kilo_output)


# Creating main window
win = Tk()
win.title("Convert Miles to Kilometers")
win.geometry("320x200")

# Title
lbl_title = Label(win, text="Miles to Kilometers", font="calibri 20 bold")
lbl_title.pack()

# Creating a Frame
lbl_frame = Frame(win)
lbl_frame.pack(pady="14")

# Int Variable()
txt_int = IntVar()
# A string var to hold the output values
lbl_output_string = StringVar()

# entry & a button
txt_entry = ttk. Entry(lbl_frame, width=24, textvariable=txt_int)
txt_entry.pack(side="left", padx=10)

btn_button = ttk.Button(lbl_frame, text="submit", command=convert)
btn_button.pack(side="left")

# Output Label
lbl_output = Label(win, text="Output", font="calibri 20 bold", textvariable=lbl_output_string)
lbl_output.pack(pady="6")

# Run function
win.mainloop()
