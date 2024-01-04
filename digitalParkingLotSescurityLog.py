from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk,Image
from datetime import datetime
import time
import io
import mysql.connector
import csv

homeWindow = Tk()
homeWindow.title("PNC Parking")
homeWindow.geometry("1440x810")
homeWindow.iconbitmap("PNCLogo.ico")
homeWindowCallImage=Image.open("homeWindowBg.png")
homeWindowBackground=ImageTk.PhotoImage(homeWindowCallImage)
homeWindowBG=Label(homeWindow,image=homeWindowBackground)
homeWindowBG.image = homeWindowBackground
homeWindowBG.grid(row=0, column=0)
homeWindow.resizable(False,False)

globalTime = datetime.now()
timeNow = globalTime.strftime("%H:%M")
fullTimeNow = globalTime.strftime("%I:%M:%S %p")
dateNow = globalTime.strftime("%b %d, %Y")
dayNow = globalTime.strftime("%d")
monthNow = globalTime.strftime("%B")
yearNow = globalTime.strftime("%Y")

currSecUID = (0,)
secOnDutyFullName = ""

Database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)
cursorMain = Database.cursor()
cursorMain.execute("CREATE DATABASE IF NOT EXISTS digitalParkingLotSecurityLogDatabase")

dbase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'digitalParkingLotSecurityLogDatabase',
)
cursorDbase = dbase.cursor()

def updateClock():
    global timeNow
    rawTime = datetime.now()
    updateTime = rawTime.strftime("%I:%M:%S %p")
    timeNow = rawTime.strftime("%H:%M")
    TimeLabel.config(text = updateTime)
    TimeLabel.after(1000,updateClock)

def releaseGrab(_window):
    _window.grab_release()
    _window.destroy()
    homeWindow.destroy()

def OpenScanWindow():
    scanWindow = Toplevel(homeWindow)
    scanWindow.title("PNC Parking Scan")
    scanWindow.geometry("400x314")
    scanWindow.iconbitmap("PNCLogo.ico")
    scanWindowCallImage=Image.open("scanWindowBGupdated.png")
    scanWindowBackEnd=ImageTk.PhotoImage(scanWindowCallImage)
    scanWindowBG=Label(scanWindow,image=scanWindowBackEnd)
    scanWindowBG.image = scanWindowBackEnd
    scanWindowBG.grid(row=0, column=0)
    scanWindow.resizable(False,False)
    
    def updateClock():
        rawTime = datetime.now()
        scanTime = rawTime.strftime("%I:%M %p")
        DTholder.config(text = dateNow +" | " + scanTime)
        DTholder.after(1000,updateClock)

    def checkUserToDatabase():
        DB = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'password123',
            database = 'digitalParkingLotSecurityLogDatabase',
        )
        cursor = DB.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS parkedUsers (\
            userID INT AUTO_INCREMENT PRIMARY KEY,\
            firstName VARCHAR(255), \
            lastName VARCHAR(255), \
            studentNumber INT(20), \
            department VARCHAR(255), \
            vehicleType VARCHAR(255), \
            date VARCHAR(255),\
            timeIn VARCHAR(255), \
            timeOut VARCHAR(255),\
            parkStatus VARCHAR(10))")
        

        sqlCommand = "SELECT * FROM registeredUsers WHERE studentNumber = %s" 
        scannedStdnNo = scanIDfield.get()
        stdnNumber = (scannedStdnNo, )
        cursor.execute(sqlCommand, stdnNumber)
        result = cursor.fetchone()
        if result:
            sqlSearch = "SELECT * FROM parkedUsers WHERE studentNumber = %s"
            cursor.execute(sqlSearch,stdnNumber)
            isUserParked = cursor.fetchone()
            if not isUserParked: #park going in
                global timeNow
                sqlFName = "SELECT firstName FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlFName,stdnNumber)
                resultFName = cursor.fetchone()
                sqlLName = "SELECT lastName FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlLName, stdnNumber)
                resultLName = cursor.fetchone()
                firstName = resultFName[0]
                lastName = resultLName[0]
                resultName = firstName + " " + lastName
                sqlDept = "SELECT department FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlDept, stdnNumber)
                resultDept = cursor.fetchone()
                sqlTOV = "SELECT vehicleType FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlTOV, stdnNumber)
                resultTOV = cursor.fetchone()
                parkStatus = "in"
                timeOut = ""

                #for photos
                sqlPhoto = "SELECT userPhoto FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlPhoto, stdnNumber)
                resultPhoto = cursor.fetchone()
                getPhoto = resultPhoto[0]
                callPhoto = Image.open(io.BytesIO(getPhoto))
                newSize = (150,150)
                profilePicNewSize = callPhoto.resize(newSize)
                profilePic = ImageTk.PhotoImage(profilePicNewSize)

                #insertion to parkeduser table
                sqlCommand2 = "INSERT INTO parkedUsers (firstName, lastName, studentNumber, department, vehicleType, date, timeIn, parkStatus) VALUES (%s, %s, %s, %s, %s, %s ,%s, %s)"
                values = (str(resultFName[0]), str(resultLName[0]), int(stdnNumber[0]), str(resultDept[0]), str(resultTOV[0]), dateNow, timeNow, parkStatus)
                cursor.execute(sqlCommand2,values)
                DB.commit()

                #display of info
                OpenParkingStatusWindow(resultName,resultDept[0],stdnNumber,resultTOV, profilePic,timeNow,timeOut)

            else: #park going out
                sqlFName = "SELECT firstName FROM parkedUsers WHERE studentNumber = %s"
                cursor.execute(sqlFName,stdnNumber)
                resultFName = cursor.fetchone()
                sqlLName = "SELECT lastName FROM parkedUsers WHERE studentNumber = %s"
                cursor.execute(sqlLName, stdnNumber)
                resultLName = cursor.fetchone()
                firstName = resultFName[0]
                lastName = resultLName[0]
                resultName = firstName + " " + lastName
                sqlDept = "SELECT department FROM parkedUsers WHERE studentNumber = %s"
                cursor.execute(sqlDept, stdnNumber)
                resultDept = cursor.fetchone()
                sqlTOV = "SELECT vehicleType FROM parkedUsers WHERE studentNumber = %s"
                cursor.execute(sqlTOV, stdnNumber)
                resultTOV = cursor.fetchone()
                sqlTimeIn = "SELECT timeIn FROM parkedUsers WHERE studentNumber = %s"
                cursor.execute(sqlTimeIn,stdnNumber)
                resultTimeIn = cursor.fetchone()
                parkStatus = "out"
                sqlTimeOut = "UPDATE parkedUsers SET timeOut = %s WHERE studentNumber = %s"
                cursor.execute(sqlTimeOut, (timeNow, int(stdnNumber[0])))
                sqlParkStatus = "UPDATE parkedUsers SET parkStatus = %s WHERE studentNumber = %s"
                cursor.execute(sqlParkStatus, (str(parkStatus),int(stdnNumber[0])))

                #for image
                sqlPhoto = "SELECT userPhoto FROM registeredUsers WHERE studentNumber = %s"
                cursor.execute(sqlPhoto, stdnNumber)
                resultPhoto = cursor.fetchone()
                getPhoto = resultPhoto[0]
                callPhoto = Image.open(io.BytesIO(getPhoto))
                newSize = (150,150)
                profilePicNewSize = callPhoto.resize(newSize)
                profilePic = ImageTk.PhotoImage(profilePicNewSize)
                DB.commit()

                OpenParkingStatusWindow(resultName,resultDept[0],stdnNumber,resultTOV, profilePic, resultTimeIn, timeNow)

        else: #data does not exist
            response = messagebox.askquestion("Student number not recognized", "Would you like to register a new student?")
            if response == "yes":
                OpenParkingRegistrationWindow()

    DTholder= Label(scanWindow,text= " ", font=("Segoe",10),bg="#f8faf7", width=25, height=1)
    DTholder.place(relx=0.53, rely=0.02)

    #label
    ParkingLotScan= Label(scanWindow, text="Parking Lot Scanner",font="berlinsans",bg="darkgreen",width=21, height=1,)
    ParkingLotScan.place(relx=0.249, rely=0.35,)

    #text
    ScanID= Label(scanWindow,text="Scan ID", font="berlinsans", width=12, height=1)
    ScanID.place(relx=0.258,rely=0.47)

    #entry/field
    scanIDfield= Entry(scanWindow, width=20,border=2, bg="white")
    scanIDfield.place(relx=0.33,rely=0.54)

    #Button
    confirmButton= Button(scanWindow, text="Confirm", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10, command=checkUserToDatabase)
    confirmButton.place(relx=0.4,rely=0.7)
    
    updateClock()

def OpenParkingStatusWindow(_name,_dept,_stdNum,_TOV,_photo,_timeIn,_timeOut):
    parkStatWin = Toplevel(homeWindow)
    parkStatWin.title("PNC Parking")
    parkStatWin.geometry("800x450")
    parkStatWin.iconbitmap("PNCLogo.ico")
    parkStatWinCallImage=Image.open("parkingStatusWindowBG.png")
    parkStatWinBackground=ImageTk.PhotoImage(parkStatWinCallImage)
    parkStatWinBG=Label(parkStatWin,image=parkStatWinBackground)
    parkStatWinBG.image = parkStatWinBackground
    parkStatWinBG.grid(row=0, column=0)
    parkStatWin.resizable(False,False)

    def parkStatWinDone():
        parkStatWin.destroy()

    #label
    StudentInfo=Label(parkStatWin, text="Student Information",font=("berlinsans",20,"bold"),bg="darkgreen",width=47, height=2,)
    StudentInfo.place(relx=0.001, rely=0.001,)

    StudentName=Label(parkStatWin,text="Name:", font=("berlinsans",15),bg="lightgreen" ,width=8, height=1)
    StudentName.place(relx=0.258,rely=0.25)

    StudentNameFill=Label(parkStatWin,text=_name , font=("berlinsans",15),bg="lightgreen" ,width=30, height=1)
    StudentNameFill.place(relx=0.35,rely=0.25)

    StudentDepartment=Label(parkStatWin,text="Department:", font=("berlinsans",15),bg="lightgreen" ,width=12, height=1)
    StudentDepartment.place(relx=0.258,rely=0.35)

    StudentDepartmentFill=Label(parkStatWin,text=_dept, font=("berlinsans",15),bg="lightgreen" ,width=30, height=1)
    StudentDepartmentFill.place(relx=0.43,rely=0.35)

    StudentNo=Label(parkStatWin, text="Student No.",font=("berlinsans",15),bg="lightgreen" ,width=10, height=1)
    StudentNo.place(relx=0.03, rely=0.52)

    StudentNoFill=Label(parkStatWin, text=_stdNum,font=("berlinsans",15),bg="lightgreen" ,width=20, height=1)
    StudentNoFill.place(relx=0.17, rely=0.52)

    RegisteredVehicle= Label(parkStatWin, text="Type of Vehicle:",font=("berlinsans",15),bg="lightgreen" ,width=13, height=1)
    RegisteredVehicle.place(relx=0.03, rely=0.62)

    RegisteredVehicleFill= Label(parkStatWin, text=_TOV,font=("berlinsans",15),bg="lightgreen" ,width=18, height=1)
    RegisteredVehicleFill.place(relx=0.21, rely=0.62)

    TimeIn=Label(parkStatWin, text="Time in:",font=("berlinsans",15),bg="gray" ,width=7, height=1)
    TimeIn.place(relx=0.03,rely=0.75)

    TimeOut=Label(parkStatWin, text="Time out:",font=("berlinsans",15),bg="gray" ,width=8, height=1)
    TimeOut.place(relx=0.3,rely=0.75)

    TimeInFill=Label(parkStatWin, text=_timeIn,font=("berlinsans",15),bg="lightgreen" ,width=9, height=1)
    TimeInFill.place(relx=0.03,rely=0.85)

    TimeOutFill=Label(parkStatWin, text=_timeOut,font=("berlinsans",15),bg="lightgreen" ,width=10, height=1)
    TimeOutFill.place(relx=0.3,rely=0.85)

    #for picture
    PicHolder=Label(parkStatWin, image = _photo)
    PicHolder.image = _photo
    PicHolder.place(relx=0.03, rely=0.16)
    
    #button
    DoneButton=Button(parkStatWin, text="Done", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=12, command=parkStatWinDone)
    DoneButton.place(relx=0.48,rely=0.9)

def OpenSecurityLogInWindow():
    securityLogInWindow = Toplevel(homeWindow)
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
        database = 'digitalParkingLotSecurityLogDatabase',
    )

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
        global currSecUID
        cursor = DB.cursor()
        sqlCommand = "SELECT * FROM registeredSecurity WHERE username = %s AND password = %s"
        usernameInput = usernameField.get()
        passwordInput = pwField.get()
        account = (usernameInput, passwordInput)
        cursor.execute(sqlCommand, account)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Security Log-In","Account successfully logged in")
            sqlUID = "SELECT userID FROM registeredSecurity WHERE username = %s AND password = %s"
            cursor.execute(sqlUID, account)
            resultUID = cursor.fetchone()
            currSecUID = resultUID
            SecurityOnDutySetUp()
            securityLogInWindow.destroy()
        else:
            messagebox.showinfo("Security Log-In", "Account not found")

    loginText= Label(securityLogInWindow, text="SECURITY LOG IN",font="berlinsans",bg="darkgreen",width=20, height=1,)
    loginText.place(relx=0.27, rely=0.28,)

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
    secRegWin = Toplevel(homeWindow)
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
        database = 'digitalParkingLotSecurityLogDatabase',
    )
    cursor = DB.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS registeredSecurity(\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255),\
        lastName VARCHAR(255),\
        username VARCHAR(255),\
        password VARCHAR(255),\
        photo MEDIUMBLOB)")

    currentFileName = ""
    def registerSecurity():
        password = pwField.get() 
        confirm = confirmPwField.get()
        with open(currentFileName,"rb") as file:
            photo = file.read()

        if password == confirm:
            sqlCommand = "INSERT INTO registeredSecurity (firstName, lastName, username, password, photo) VALUES (%s, %s, %s, %s,%s)"
            values = (fNameField.get(), lNameField.get(), usernameField.get(), pwField.get(), photo)
            cursor.execute(sqlCommand, values)
            DB.commit()
            messagebox.showinfo("Security Account Registration","Account Successfully Registered")
            secRegWin.destroy()
        else:
            messagebox.showinfo("Security Account Registration", "password and confirm password must be the same")
    
    def uploadPhoto():
        nonlocal currentFileName
        filePath = filedialog.askopenfilename(title = "Select an image")
        currentFileName = filePath
        #display pic in registration
        displayPicCallImage = Image.open(filePath)
        newSize = (110,110)
        displayPicNewSize = displayPicCallImage.resize(newSize)
        displayPic = ImageTk.PhotoImage(displayPicNewSize)
        PicHolder= Label(secRegWin, image = displayPic)
        PicHolder.place(relx=0.3, rely=0.63)
        PicHolder.image = displayPic

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
    UploadButton= Button(secRegWin,text="Upload photo", bg="white", width=15, command = uploadPhoto)
    UploadButton.place(relx=0.49,rely=0.67)

    Reg_button= Button(secRegWin, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command = registerSecurity)
    Reg_button.place(relx= 0.46, rely=0.78)

def OpenParkingRegistrationWindow():
    parkRegWin = Toplevel(homeWindow)
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
        database = 'digitalParkingLotSecurityLogDatabase',
    )
    cursor = DB.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS registeredUsers (\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        studentNumber INT(20), \
        department VARCHAR(255), \
        vehicleType VARCHAR(255),\
        userPhoto MEDIUMBLOB)")
    currentFileName = ""
    def registerUser():
        #table
        cursor.execute("CREATE TABLE IF NOT EXISTS registeredUsers (\
        userID INT AUTO_INCREMENT PRIMARY KEY,\
        firstName VARCHAR(255), \
        lastName VARCHAR(255), \
        studentNumber INT(20), \
        department VARCHAR(255), \
        vehicleType VARCHAR(255),\
        userPhoto MEDIUMBLOB)")
        
        with open(currentFileName,"rb") as file:
            photo = file.read()
        
        sqlCommand = "INSERT INTO registeredUsers (firstName, lastName, studentNumber, department, vehicleType,userPhoto) VALUES (%s, %s, %s, %s, %s,%s)"
        values = (fNameField.get(), lNameField.get(), StudentNoField.get(), deptOptionsDrpDwn.get(), vehicleOptionsDrpDwn.get(),photo)
        cursor.execute(sqlCommand, values)
        DB.commit()
        messagebox.showinfo("Parking registration", "Registration Sucessful")
        parkRegWin.destroy()
    
    def uploadPhoto():
        nonlocal currentFileName
        filePath = filedialog.askopenfilename(title = "Select an image")
        currentFileName = filePath

        displayPicCallImage = Image.open(filePath)
        newSize = (140,140)
        displayPicNewSize = displayPicCallImage.resize(newSize)
        displayPic = ImageTk.PhotoImage(displayPicNewSize)
        PicHolder= Label(parkRegWin, image = displayPic, width=140,height=140)
        PicHolder.place(relx=0.2, rely=0.3)
        PicHolder.image = displayPic

    def goToScanWindow():
        parkRegWin.destroy()

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
    StudentNoField.insert(0,"Student No.")
    StudentNoField.bind("<Button-1>",studentNoClearOnClick)

    #Combo Boxes
    deptOptionsDrpDwn = ttk.Combobox(parkRegWin, value = ["Select Department","COE", "COED", "CAS", "CHAS", "CBAA", "CCS"])
    deptOptionsDrpDwn.current(0)
    deptOptionsDrpDwn.place(relx=0.4, rely=0.525, width=305)

    vehicleOptionsDrpDwn = ttk.Combobox(parkRegWin, value = ["Select Type of Vehicle","Bike", "E-Bike", "Motorcycle", "Car",])
    vehicleOptionsDrpDwn.current(0)
    vehicleOptionsDrpDwn.place(relx=0.4,rely=0.672)

    #Buttons

    uploadPhotoButton= Button(parkRegWin, text="Upload Photo", bg="white", width=20, command=uploadPhoto)
    uploadPhotoButton.place(relx=0.6, rely=0.672)

    Reg_button = Button(parkRegWin, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command=registerUser)
    Reg_button.place(relx= 0.4, rely=0.85)

    backButton = Button(parkRegWin, text="Go Back", bg="gray" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command=goToScanWindow)
    backButton.place(relx= 0.7, rely=0.85)

def OpenExportWindow():
    exportWindow = Toplevel(homeWindow)
    exportWindow.title("Export to Excel")
    exportWindow.geometry("961x964")
    exportWindow.iconbitmap("PNCLogo.ico")
    exportWindowCallImage=Image.open("exportExcelWindowBG.png")
    exportWindowBackground=ImageTk.PhotoImage(exportWindowCallImage)
    exportWindowBG=Label(exportWindow,image=exportWindowBackground)
    exportWindowBG.image = exportWindowBackground
    exportWindowBG.grid(row=0, column=0)
    exportWindow.resizable(False,False)

    def exportToExcel(_table):
        DB = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'password123',
            database = 'digitalParkingLotSecurityLogDatabase',
        )
        cursor = DB.cursor()
        #lagay ng if statement
        if _table == "parkedUsers":
            exportFileName = "Daily Parking Log " + dateNow + ".csv"
            
            sqlCommand = f"SELECT * FROM {_table}"
            cursor.execute(sqlCommand)
            columnNames = [col[0] for col in cursor.description]
            result = cursor.fetchall()
            with open(exportFileName, "w", newline="")as file:
                writer = csv.writer(file,dialect='excel')
                writer.writerow(columnNames)
                for record in result:
                    writer.writerow(record)
            messagebox.showinfo("File Export", exportFileName + " has successfully been exported")
            exportWindow.destroy()

        elif _table == "registeredUsers":
            exportFileName = "Registered Parking Users " + dateNow + ".csv"
            sqlCommand = f"SELECT userID,firstName, lastName, studentnumber, department, vehicleType FROM {_table}"
            cursor.execute(sqlCommand)
            columnNames = [col[0] for col in cursor.description]
            result = cursor.fetchall()
            with open(exportFileName, "w", newline="")as file:
                writer = csv.writer(file,dialect='excel')
                writer.writerow(columnNames)
                for record in result:
                    writer.writerow(record)
            messagebox.showinfo("File Export", exportFileName + " has successfully been exported")
            exportWindow.destroy()
        else:
            exportFileName = ""
        

    #label
    ParkingLotScan= Label(exportWindow, text="Export Excel",font=("Segoe",30,"bold"),bg="darkgreen",width=20, height=1,)
    ParkingLotScan.place(relx=0.249, rely=0.3,)

    #button
    ParkUserButton=Button(exportWindow, text="Daily Parking Log", font=("Segoe",20),width=30,height=1, command=lambda: exportToExcel("parkedUsers"))
    ParkUserButton.place(relx=0.249, rely=0.4)

    RegStFtButton=Button(exportWindow, text="Registered Parking Users", font=("Segoe",20),width=30,height=1, command=lambda: exportToExcel("registeredUsers"))
    RegStFtButton.place(relx=0.249, rely=0.5)


def SecurityOnDutySetUp():
    global secOnDutyFullName
    sqlSecFName = "SELECT firstName FROM registeredSecurity WHERE userID = %s"
    sqlSecLName = "SELECT lastName FROM registeredSecurity WHERE userID = %s"
    sqlSecPhoto = "SELECT photo FROM registeredSecurity WHERE userID = %s"

    #name setup
    cursorDbase.execute(sqlSecFName, currSecUID)
    secFName = cursorDbase.fetchone()
    cursorDbase.execute(sqlSecLName, currSecUID)
    secLName = cursorDbase.fetchone()
    secOnDutyFullName = secLName[0].upper() + ", " +  secFName[0]
    FNlabel.config(text = secOnDutyFullName)

    #image setup
    cursorDbase.execute(sqlSecPhoto, currSecUID)
    secPhoto = cursorDbase.fetchone()
    resultPhoto = secPhoto[0]
    callPhoto = Image.open(io.BytesIO(resultPhoto))
    newSize = (200, 200)
    profilePic = callPhoto.resize(newSize)
    displayPic = ImageTk.PhotoImage(profilePic)
    secPicHolder = Label(homeWindow, image = displayPic)
    secPicHolder.image = displayPic
    secPicHolder.place(relx= 0.75, rely = 0.35)

#label
ScanID= Label(homeWindow,text="Security Scanner Home Page", bg="green", font=("Segoe",15), width=24, height=3)
ScanID.place(relx=0.001,rely=0.2)

#ScannedIDButton
scIDButton= Button(homeWindow, text="ID Scanning", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3, command = OpenScanWindow)
scIDButton.place(relx=0.000,rely=0.3)

#STRegButton
STRegButton= Button(homeWindow, text="Student    Registration", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3, command = OpenParkingRegistrationWindow)
STRegButton.place(relx=0.000,rely=0.4)

#ScRegButton
ScRegButton= Button(homeWindow, text="Security    Registration", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3, command = OpenSecurityRegistration)
ScRegButton.place(relx=0.000,rely=0.5)

#ExpExcButton
EXPButton= Button(homeWindow, text="Export    Excel", bg="#f8faf7" ,font=("Segoe",15),width=24, height=3, command = OpenExportWindow)
EXPButton.place(relx=0.000,rely=0.6)

#DateLabel
DayLabel= Label(homeWindow,text=dayNow, bg="#ccd6dd", font=("Segoe",50,"italic","bold"), width=2, height=1)
DayLabel.place(relx=0.76,rely=0.1975)

MonthLabel= Label(homeWindow,text=monthNow, bg="#ccd6dd", font=("Segoe",20,"italic"), width=8, height=1)
MonthLabel.place(relx=0.82,rely=0.18)

YearLabel= Label(homeWindow,text=yearNow, bg="#ccd6dd", font=("Segoe",20,"italic"), width=4, height=1)
YearLabel.place(relx=0.82,rely=0.22)

TimeLabel= Label(homeWindow, fg="darkgreen",bg="#ccd6dd", font=("Segoe",20,"italic"), width=10, height=1)
TimeLabel.place(relx=0.82,rely=0.26)

#fullNameLabel
FNlabel=Label(homeWindow,fg="white", bg="#167237", font=("Segoe",25), width=25, height=1)
FNlabel.place(relx=0.675, rely=0.025)

updateClock()
OpenSecurityLogInWindow()
homeWindow.mainloop()