from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import csv
#scanWindow is root
scanWindow = Tk()
scanWindow.title("PNC Parking Scan")
scanWindow.geometry("400x315")
scanWindow.iconbitmap("PNCLogo.ico")
scanWindowCallImage=Image.open("scanWindowBG.png")
scanWindowBackEnd=ImageTk.PhotoImage(scanWindowCallImage)
scanWindowBG=Label(scanWindow,image=scanWindowBackEnd)
scanWindowBG.grid(row=0, column=0)
scanWindow.resizable(False,False)

def checkUserToDatabase():
    return print("check")

def dbquery():
    return print("query")

def securityLogInWindow():
    securityLogInWindow = Tk()
    securityLogInWindow.title("PNC Security Log In")
    securityLogInWindow.geometry("397x400")
    securityLogInWindow.iconbitmap("PNCLogo.ico")
    securityLogInWindowCallImage=Image.open("securityLogInWindowBG.png")
    securityLogInWindowBackEnd=ImageTk.PhotoImage(securityLogInWindowCallImage)
    lbl=Label(securityLogInWindow, image=securityLogInWindowBackEnd)
    lbl.grid(row=0, column=0)
    securityLogInWindow.resizable(False,False)

#label
ParkingLotScan= Label(scanWindow, text="Parking Lot Scanner",font="berlinsans",bg="darkgreen",width=20, height=1,)
ParkingLotScan.place(relx=0.27, rely=0.32,)


#text
ScanID= Label(scanWindow,text="Scan ID", font="berlinsans", width=12, height=1)
ScanID.place(relx=0.258,rely=0.47)


#entry/field
scanIDfield= Entry(scanWindow, width=20,border=2, bg="white")
scanIDfield.place(relx=0.33,rely=0.54)


#Button
confirmButton= Button(scanWindow, text="Confirm", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10, command=checkUserToDatabase)
confirmButton.place(relx=0.4,rely=0.7)

#temporary button. trash this later
queryButton= Button(scanWindow, text="query", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10, command=dbquery)
queryButton.place(relx=0.4,rely=0.8)

securityLogInWindow()
scanWindow.mainloop()