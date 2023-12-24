from tkinter import *
from tkinter import ttk, messagebox
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

Database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'registeredParkingUsersDatabase',
)
cursorMain = Database.cursor()
cursorMain.execute("CREATE DATABASE IF NOT EXISTS registeredParkingUsersDatabase")

def checkUserToDatabase():
    sqlCommand = "SELECT * FROM registeredUsers WHERE studentNumber = %s" 
    scannedStdnNo = scanIDfield.get()
    stdnNumber = (scannedStdnNo, )
    cursorMain.execute(sqlCommand, stdnNumber)
    result = cursorMain.fetchone()

    #checker lang to. Trash this
    if result:
        print("data exist")
    else: #data does not exist
        #open registration Window
        #put message box and additional ifelse logic here
        OpenParkingRegistrationWindow()
        print("data doesnt exist")

def dbquery(): #temporary function
    dataQuery = Tk()
    dataQuery.title("registered Query")
    dataQuery.geometry('800x600')
    cursorMain.execute("SELECT * FROM registeredUsers")
    result = cursorMain.fetchall()
    for index, tableRow in enumerate(result):
        num = 0
        for tableColumn in tableRow:
            dataQueryLabel = Label(dataQuery,text=tableColumn) 
            dataQueryLabel.grid(row=index, column=num, padx=5)
            num += 1
    
def releaseGrab(_window):
    _window.grab_release()
    _window.destroy()
    scanWindow.destroy()

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

    DB = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'password123',
        database = 'sercurityAccountDatabase',
    )

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
    
    def accountLogIn():
        cursor = DB.cursor()
        sqlCommand = "SELECT * FROM registeredSecurity WHERE username = %s AND password = %s"
        usernameInput = usernameField.get()
        passwordInput = pwField.get()
        account = (usernameInput, passwordInput)
        cursor.execute(sqlCommand, account)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Security Log-In","Account successfully logged in")
            securityLogInWindow.destroy()
        else:
            messagebox.showinfo("Security Log-In", "Account not found")

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

    loginButton= Button(securityLogInWindow, text="LOG IN", bg="darkgreen" ,width=20, command=accountLogIn)
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

    DB = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'password123',
        database = 'sercurityAccountDatabase',
    )
    cursor = DB.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS sercurityAccountDatabase")
    cursor.execute("CREATE TABLE IF NOT EXISTS registeredSecurity(\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255),\
        lastName VARCHAR(255),\
        username VARCHAR(255),\
        password VARCHAR(255))")
    '''
    idagdag to kapag nacode na ung file handling ng pictures
    userPhoto VARCHAR(255)
    '''

    def registerSecurity():
        password = pwField.get() 
        confirm = confirmPwField.get()
        if password == confirm:
            sqlCommand = "INSERT INTO registeredSecurity (firstName, lastName, username, password) VALUES (%s, %s, %s, %s)"
            values = (fNameField.get(), lNameField.get(), usernameField.get(), pwField.get())
            cursor.execute(sqlCommand, values)
            DB.commit()
            messagebox.showinfo("Security Account Registration","Account Successfully Registered")
            OpenSecurityLogInWindow()
            secRegWin.destroy()
        else:
            messagebox.showinfo("Security Account Registration", "password and confirm password must be the same")

    def fieldContentLogic(_var, _field):
        if _field == pwField:
            if _var.get() !="                             Password":
                _field.config(show="*")
            else:
                pwField.config(show="")
        elif _field == confirmPwField:
            if _var.get() != "                        Confirm Password":
                _field.config(show="*")
            else:
                _field.config(show="")

    def dbquery(): #temporary function
        dataQuery = Tk()
        dataQuery.title("Security account Query")
        dataQuery.geometry('800x600')
        cursor.execute("SELECT * FROM registeredSecurity")
        result = cursor.fetchall()
        for index, tableRow in enumerate(result):
            num = 0
            for tableColumn in tableRow:
                dataQueryLabel = Label(dataQuery,text=tableColumn) 
                # add index to x to get the specific field u want (eg x[0] would give you the 0th column of the database which is the first name) 
                dataQueryLabel.grid(row=index, column=num, padx=5)
                num += 1
    
    def clearDB(): #temporary function
        cursor.execute('DELETE FROM registeredSecurity')
        DB.commit()
    
    def backToLogin():
        secRegWin.destroy()
        OpenSecurityLogInWindow()

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

    backButton= Button(secRegWin, text="Go Back", bg="gray" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command = backToLogin)
    backButton.place(relx= 0.85, rely=0.88)

    secRegWin.protocol("WM_DELETE_WINDOW", lambda: releaseGrab(secRegWin))
    secRegWin.grab_set()

def OpenParkingRegistrationWindow():
    parkRegWin = Toplevel(scanWindow)
    parkRegWin.title("PNC Parking Registration")
    parkRegWin.geometry("800x450")
    parkRegWin.iconbitmap("PNCLogo.ico")
    parkRegWinCallImage=Image.open("registrationWindowBG.png")
    parkRegWinBackground=ImageTk.PhotoImage(parkRegWinCallImage)
    parkRegWinBG=Label(parkRegWin,image=parkRegWinBackground)
    parkRegWin.image = parkRegWinBackground
    parkRegWinBG.grid(row=0, column=0)
    parkRegWin.resizable(False,False)

    DB = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'password123',
        database = 'registeredParkingUsersDatabase',
    )
    cursor = DB.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS registeredParkingUsersDatabase")
    cursor.execute("CREATE TABLE IF NOT EXISTS registeredUsers (\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        studentNumber INT(20), \
        department VARCHAR(255), \
        vehicleType VARCHAR(255))")

    '''
        idagdag to kapag na-code na ung file handling for pictures
        userPhoto VARCHAR(255), \ # gumamit ng VARCHAR kasi ififile handle ung name ng image file
        vechiclePhoto VARCHAR(255)\
        '''
    
    def registerUser():
        cursor.execute("CREATE DATABASE IF NOT EXISTS registeredParkingUsersDatabase")
        #table
        cursor.execute("CREATE TABLE IF NOT EXISTS registeredUsers (\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        studentNumber INT(20), \
        department VARCHAR(255), \
        vehicleType VARCHAR(255))")

        sqlCommand = "INSERT INTO registeredUsers (firstName, lastName, studentNumber, department, vehicleType) VALUES (%s, %s, %s, %s, %s)"
        values = (fNameField.get(), lNameField.get(), StudentNoField.get(), deptOptionsDrpDwn.get(), vehicleOptionsDrpDwn.get())
        cursor.execute(sqlCommand, values)
        DB.commit()
        messagebox.showinfo("Parking registration", "Registration Sucessful")

    def goToScanWindow():
        parkRegWin.destroy()

    def dbquery(): #this function is temporary. This just shows all data in the table
        dataQuery = Tk()
        dataQuery.title("Parking registered users Query")
        dataQuery.geometry('800x600')
        cursor.execute("SELECT * FROM registeredUsers")
        result = cursor.fetchall()
        for index, tableRow in enumerate(result):
            num = 0
            for tableColumn in tableRow:
                dataQueryLabel = Label(dataQuery,text=tableColumn) 
                # add index to x to get the specific field u want (eg x[0] would give you the 0th column of the database which is the first name) 
                dataQueryLabel.grid(row=index, column=num, padx=5)
                num += 1

    def clearDB(): #temporary function
        cursor.execute('DELETE FROM registeredUsers')
        DB.commit()

    def fNameClearOnClick(event):
        fNameField.delete(0,END)
    def lNameClearOnClick(event):
        lNameField.delete(0,END)
    def studentNoClearOnClick(event):
        StudentNoField.delete(0,END)

    #text/labels
    heading = Label(parkRegWin, text="Registration Form",bg="darkgreen", font=("Microsoft YaHei UI Light", 15,"bold"),width=40)
    heading.place(relx=0.2, rely=0.2)

    LineLang=  Label(parkRegWin, text="   ",bg="black", font=("Microsoft YaHei UI Light", 1,"bold"),width=240)
    LineLang.place(relx=0.2,rely=0.625)

    Vehicle= Label(parkRegWin, text="  VEHICLE  ",font=("Microsoft YaHei UI Light", 12,"bold"),width=14)
    Vehicle.place(relx=0.2,rely=0.675)

    #input/entry
    fNameField= Entry(parkRegWin, width=20,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 10))
    fNameField.place(relx=0.4, rely=0.3)
    fNameField.insert(0,"First Name")
    fNameField.bind("<Button-1>",fNameClearOnClick)

    lNameField= Entry(parkRegWin, width=20, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light",10))
    lNameField.place(relx=0.6, rely=0.3)
    lNameField.insert(0,"Last Name")
    lNameField.bind("<Button-1>",lNameClearOnClick)

    StudentNoField= Entry(parkRegWin, width=43, fg="black", border=2, bg="white",font=("Microsoft YaHei UI Light",10))
    StudentNoField.place(relx=0.4,rely=0.425)
    StudentNoField.insert(0,"Faculty / Student No.")
    StudentNoField.bind("<Button-1>",studentNoClearOnClick)

    #Combo Boxes
    deptOptionsDrpDwn = ttk.Combobox(parkRegWin, value = ["Select Department","College of Engineering", "College of Education", "College of Arts and Sciences", "College of Allied Health and Sciences", "College of Business Administration and Accountancy", "College of Computing Studies"])
    deptOptionsDrpDwn.current(0)
    deptOptionsDrpDwn.place(relx=0.4, rely=0.525, width=305)

    vehicleOptionsDrpDwn = ttk.Combobox(parkRegWin, value = ["Select Type of Vehicle","Bike", "E-Bike", "Motorcycle"," Car"])
    vehicleOptionsDrpDwn.current(0)
    vehicleOptionsDrpDwn.place(relx=0.4,rely=0.672)

    #Buttons
    PicHolder= Button(parkRegWin, text="PHOTO HERE", bg="white", width=20,height=8)
    PicHolder.place(relx=0.2, rely=0.3)

    VehiclePDF= Button(parkRegWin, text="Upload Vehicle PDF", bg="white", width=20)
    VehiclePDF.place(relx=0.6, rely=0.672)

    Reg_button = Button(parkRegWin, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command=registerUser)
    Reg_button.place(relx= 0.4, rely=0.85)

    backButton = Button(parkRegWin, text="Go Back", bg="gray" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command=goToScanWindow)
    backButton.place(relx= 0.7, rely=0.85)

    #temporary buttons
    test_button = Button(parkRegWin, text="Query", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command=dbquery)
    test_button.place(relx= 0.4, rely=0.75)

    cleardb_button = Button(parkRegWin, text="Clear database", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=12, command=clearDB)
    cleardb_button.place(relx= 0.65, rely=0.75)

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
scanWindow.mainloop()