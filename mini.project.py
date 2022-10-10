import tkinter
import mysql.connector
probeq = tkinter.Tk()
probeq.geometry("500x500")
probeq.title(" Probeq Person Registration Portal")
tkinter.Label(probeq, text="Person details")
tkinter.Label(probeq, text="Name ")
tkinter.Label(probeq, text="Age")
tkinter.Label(probeq, text="Gender")
tkinter.Label(probeq, text="Email")
tkinter.Label(probeq, text="Mobile Number")

probeq.mainloop()