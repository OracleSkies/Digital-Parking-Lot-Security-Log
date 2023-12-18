from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import csv

secLogWindow = Tk()
secLogWindow.title("PNC Parking")
secLogWindow.geometry("800x450")
secLogWindow.iconbitmap("PNCLogo.ico")
image_0=Image.open("main_securitywindow_bg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(secLogWindow,image=bck_end)
lbl.grid(row=0, column=0)

def openSecurityRegisterWindow():
    messagebox.showinfo("Sign Up", "SIGN UP")
    secLogWindow.destroy()
    with open('securityLoginWindow.py', 'r') as file:
        pythonCode = file.read()
        exec(pythonCode)

'''
def openRegisterWindow():
    regWindow = Tk()
    regWindow.title("PNC Parking Registration")
    regWindow.geometry("800x450")
    regWindow.iconbitmap("PNCLogo.ico")
    image_0=Image.open("main_regwindow_bg.png")
    bck_end=ImageTk.PhotoImage(image_0)
    lbl=Label(root,image=bck_end)
    lbl.grid(row=0, column=0)
    root.resizable(False,False)
'''
def newWindowTest(): #this window is only temporary TRASH THIS LATER
    ''''
    newWindow = Tk()
    newWindow.title("New Window")
    newWindow.geometry("800x450")
    newWindow.iconbitmap("PNCLogo.ico")
    image_1=Image.open("main_regwindow_bg.png")
    bck_end=ImageTk.PhotoImage(image_1)
    registerButton = Button(newWindow, text="Register", command=openRegisterWindow)
    registerButton.grid(row=0, column=1, padx=10,pady=10)
    '''
    with open('registrationWindow.py', 'r') as file:
        pythonCode = file.read()
        exec(pythonCode)
    

def closeLogInWindow():
    #maglagay ng logic later for the login

    #

    secLogWindow.destroy()
    newWindowTest() #change this to parking log window

#text/labels
loginText= Label(secLogWindow, text="SECURITY LOG IN",font="berlinsans",bg="darkgreen",width=20, height=1,)
loginText.place(relx=0.39, rely=0.35,)

#entryfields
usernameField= Entry(secLogWindow, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 8),width=17)
usernameField.place(relx=0.44, rely=0.47)
usernameField.insert(0,"Username")

pwField= Entry(secLogWindow, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 8),width=17)
pwField.place(relx=0.44, rely=0.59)
pwField.insert(0,"Password")

#buttons
'''
forgotPwButton= Button(root, text="Forgot Password?",bg="white")
forgotPwButton.place(relx=0.495, rely=0.68)
'''
loginButton= Button(secLogWindow, text="LOG IN", bg="darkgreen" ,width=20, command=closeLogInWindow)
loginButton.place(relx= 0.41, rely=0.73)

signUpButton= Button(secLogWindow, text="SIGN UP", bg="darkgreen" ,width=20, command=openSecurityRegisterWindow)
signUpButton.place(relx= 0.41, rely=0.8)

secLogWindow.mainloop()