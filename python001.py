from tkinter import *
import ttkbootstrap as ttk

# function
def myconvert():
    miles_input = txt_int.get()
    kilo_output = miles_input * 1.61
    lbl_strint.set(kilo_output)


# Creating mainframe
win = ttk.Window(themename = "darkly")
win.title("Miles to Kilometer")
win.geometry("350x199")

# Title
lbl_title = Label(win, text="Convert Miles to Kilometer", font="calibra 18 bold")
lbl_title.pack()

# Frame
sub_frame = Frame(win)
sub_frame.pack(pady=12)

# Int & string variable
txt_int = IntVar()
lbl_strint = StringVar()

# text entry and a button
txt_entry = ttk.Entry(sub_frame, width="30", font="bold", textvariable=txt_int)
txt_entry.pack(pady="5")

btn_button = ttk.Button(win, text="Convert", width="12", command=myconvert)
btn_button.pack()

# label for results
lbl_result = Label(win, text="results", font="calibra 15 bold", textvariable=lbl_strint)
lbl_result.pack(pady="25")

# Run function
mainloop()
