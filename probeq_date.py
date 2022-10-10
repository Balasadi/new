import tkinter  as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("300x140")
from time import strftime
def my_time(): # On button click
    time_string = strftime('%H:%M:%S %p')
    e1_str.set(time_string)  # adding time to Entry

l1 = tk.Label(my_w,  text='Add Time', width=10 )
l1.grid(row=1,column=1,padx=10,pady=30)
e1_str=tk.StringVar()
e1 = tk.Entry(my_w, textvariable=e1_str,width=15) #  Entry box
e1.grid(row=1,column=2)

b1 = tk.Button(my_w, text='Update', width=8,bg='yellow',
     command=lambda: my_time())
b1.grid(row=1,column=3)

my_w.mainloop()