from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import csv


#window
root = Tk()
root.title("PNC Parking")
root.geometry("1440x810")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("homeWindowBg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#label
ScanID= Label(root,text="Security Scanner Home Page", bg="gray", font=("Segoe",15), width=24, height=3)
ScanID.place(relx=0.001,rely=0.2)

#ExpExcButton
EXPButton= Button(root, text="Export    Excel", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3)
EXPButton.place(relx=0.000,rely=0.3)

#ScannedIDButton
scIDButton= Button(root, text="Scanned    ID", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3)
scIDButton.place(relx=0.000,rely=0.4)

#ScRegButton
ScRegButton= Button(root, text="Security    Registration", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3)
ScRegButton.place(relx=0.000,rely=0.5)

#STRegButton
STRegButton= Button(root, text="Student    Registration", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3)
STRegButton.place(relx=0.000,rely=0.6)


#DateLabel
DayLabel= Label(root,text="29", bg="#ccd6dd", font=("Segoe",50,"italic","bold"), width=2, height=1)
DayLabel.place(relx=0.76,rely=0.1975)

MonthLabel= Label(root,text="DECEMBER", bg="#ccd6dd", font=("Segoe",20,"italic"), width=10, height=1)
MonthLabel.place(relx=0.82,rely=0.18)

YearLabel= Label(root,text="2023", bg="#ccd6dd", font=("Segoe",20,"italic"), width=4, height=1)
YearLabel.place(relx=0.82,rely=0.22)

TimeLabel= Label(root,text="03:12:23 PM",fg="darkgreen",bg="#ccd6dd", font=("Segoe",20,"italic"), width=10, height=1)
TimeLabel.place(relx=0.82,rely=0.26)

#fullNameLabel
FNlabel=Label(root,text="SURNAME, First Name, MI.",fg="white", bg="#167237", font=("Segoe",25), width=25, height=1)
FNlabel.place(relx=0.675, rely=0.025)


root.mainloop()