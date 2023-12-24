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
    
def releaseGrab(_window):
    _window.grab_release()
    _window.destroy()

def OpenSecurityLogInWindow():
    securityLogInWindow = Toplevel(scanWindow)
    securityLogInWindow.title("PNC Security Log In")
    securityLogInWindow.geometry("397x400")
    securityLogInWindow.iconbitmap("PNCLogo.ico")
    securityLogInWindowCallImage=Image.open("securityLogInWindowBG.png")
    securityLogInWindowBackground= ImageTk.PhotoImage(securityLogInWindowCallImage)
    secLogWinBG = Label(securityLogInWindow, image=securityLogInWindowBackground)
    secLogWinBG.image = securityLogInWindowBackground
    secLogWinBG.grid(row=0, column=0)
    securityLogInWindow.resizable(False,False)

    loginText= Label(securityLogInWindow, text="SECURITY LOG IN",font="berlinsans",bg="darkgreen",width=20, height=1,)
    loginText.place(relx=0.27, rely=0.28,)
    def varTrace(var,index,mode):
        fieldContentLogic(pwVar, pwField)

    def fieldContentLogic(_var,_field):
        if _var.get() != "Password":
            _field.config(show="*")
        else:
            _field.config(show="")
        
    def usernameClearOnClick(event):
        usernameField.delete(0,END)
    def passwordClearOnClick(event):
        pwField.delete(0,END)
    
    def securityRegistration():
        OpenSecurityRegistration()
        securityLogInWindow.destroy()

    #entryfields
    usernameField= Entry(securityLogInWindow, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 10),width=17)
    usernameField.place(relx=0.37, rely=0.42)
    usernameField.insert(0,"Username")
    usernameField.bind("<Button-1>", usernameClearOnClick)

    pwVar = StringVar()
    pwVar.trace_add('write', varTrace)
    pwField= Entry(securityLogInWindow, textvariable = pwVar, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 10),width=17)
    pwField.place(relx=0.37, rely=0.52)
    pwField.insert(0,"Password")
    pwField.bind("<Button-1>", passwordClearOnClick)

    #buttons
    registerButton= Button(securityLogInWindow, text="REGISTER", bg="darkgreen" ,width=20, command=securityRegistration)
    registerButton.place(relx= 0.32, rely=0.78)

    loginButton= Button(securityLogInWindow, text="LOG IN", bg="darkgreen" ,width=20)
    loginButton.place(relx= 0.32, rely=0.68)

    securityLogInWindow.protocol("WM_DELETE_WINDOW",lambda: releaseGrab(securityLogInWindow))
    securityLogInWindow.grab_set()

    
def OpenSecurityRegistration():
    secRegWin = Toplevel(scanWindow)
    secRegWin.title("PNC Parking Security Account Registration")
    secRegWin.geometry("800x450")
    secRegWin.iconbitmap("PNCLogo.ico")
    secRegWinCallImage=Image.open("securityRegistrationBG.png")
    secRegWinBackground=ImageTk.PhotoImage(secRegWinCallImage)
    secRegWinBG=Label(secRegWin,image=secRegWinBackground)
    secRegWin.image = secRegWinBackground
    secRegWinBG.grid(row=0, column=0)
    secRegWin.resizable(False,False)

    def registerSecurity():
        return
    
    def dbquery():
        return
    
    def clearDB():
        return

    def varTrace(var, index, mode):
        fieldContentLogic(pwVar,pwField)
        fieldContentLogic(confirmVar,confirmPwField)

    def fNameClearOnClick(event):
        fNameField.delete(0,END)
    def lNameClearOnClick(event):
        lNameField.delete(0,END)
    def usernameClearOnClick(event):
        usernameField.delete(0,END)
    def pwClearOnClick(event):
        pwField.delete(0,END)
    def confirmClearOnClick(event):
        confirmPwField.delete(0,END)
    
    #text/labels
    loginText= Label(secRegWin, text="Security Registration",font="berlinsans",bg="darkgreen",width=30, height=1,)
    loginText.place(relx=0.31, rely=0.25,)


    #entry/fields
    fNameField= Entry(secRegWin, width=20,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
    fNameField.place(relx=0.3, rely=0.35)
    fNameField.insert(0,"First Name")
    fNameField.bind("<Button-1>",fNameClearOnClick)


    lNameField= Entry(secRegWin, width=20, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light",9))
    lNameField.place(relx=0.485, rely=0.35)
    lNameField.insert(0,"Last Name")
    lNameField.bind("<Button-1>",lNameClearOnClick)

    usernameField= Entry(secRegWin, width=40,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
    usernameField.place(relx=0.3, rely=0.42)
    usernameField.insert(0,"                            Username")
    usernameField.bind("<Button-1>",usernameClearOnClick)

    #put some logic for the show="*" para makita ung text
    pwVar = StringVar()
    pwVar.trace_add('write', varTrace)
    pwField= Entry(secRegWin, textvariable = pwVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
    pwField.place(relx=0.3, rely=0.49)
    pwField.insert(0,"                             Password")
    pwField.bind("<Button-1>",pwClearOnClick)

    confirmVar = StringVar()
    confirmVar.trace_add('write', varTrace)
    confirmPwField= Entry(secRegWin, textvariable = confirmVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
    confirmPwField.place(relx=0.3, rely=0.56)
    confirmPwField.insert(0,"                        Confirm Password")
    confirmPwField.bind("<Button-1>",confirmClearOnClick)

    #buttons
    PicHolder=Button(secRegWin, text="PHOTO HERE", bg="white", width=15,height=6)
    PicHolder.place(relx=0.3, rely=0.63)

    UploadButton= Button(secRegWin,text="Upload photo", bg="white", width=15)
    UploadButton.place(relx=0.49,rely=0.67)

    Reg_button= Button(secRegWin, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command = registerSecurity)
    Reg_button.place(relx= 0.46, rely=0.78)

    querybutton= Button(secRegWin, text="Query", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command = dbquery)
    querybutton.place(relx= 0.7, rely=0.78)

    clearDBbutton= Button(secRegWin, text="clear DB", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command = clearDB)
    clearDBbutton.place(relx= 0.85, rely=0.78)

    secRegWin.protocol("WM_DELETE_WINDOW", lambda: releaseGrab(secRegWin))
    secRegWin.grab_set()

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

OpenSecurityLogInWindow()
#scanWindow.protocol("WM_DELETE_WINDOW", lambda:releaseGrab(scanWindow))
scanWindow.mainloop()