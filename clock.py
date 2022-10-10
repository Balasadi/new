from tkinter import *
from tkinter.ttk import *
import fontstyle
from time import strftime
root = Tk()
root.title("Probeq Clock")

def time():
    #string = strftime("%H:%M:%S")
    string = strftime('%H:%M:%S %p \n %A \n %x')
    label.config(text=string)
    label.after(1000, time)
#time_string = strftime('%H:%M:%S %p \n %x')
#clock = Tkinter.Label(window, font=(‘digital-7′, 140,), bg=’black’, fg = ‘green’)

#label = Label(root, font=("ds-digital", 50), background="black", foreground="cyan")
label = Label(root, font = ('calibri', 20, 'bold'),background = 'purple',foreground = 'white')
label.pack(anchor="center")
time()

mainloop()