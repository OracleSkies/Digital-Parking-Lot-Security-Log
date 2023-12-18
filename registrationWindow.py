from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import csv

'''
===SCRIPT Tasks===
gumawa ng interaction from here to scanWindow.py using button
maglagay ng messagebox na nagsasabing registered na ang user
icoclose ang window kapag registered na ang user
'''


root = Tk()
root.title("PNC Parking Registration")
root.geometry("800x450")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("registrationWindowBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#connection to MySQL
DB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'registeredParkingUsersDatabase',
)
#print(DB) #check if connected to MySQL

#create and Init cursor
cursor = DB.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS registeredParkingUsersDatabase")

#database creation test
'''
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
'''

#create table
cursor.execute("CREATE TABLE IF NOT EXISTS registeredUsers (\
    userID INT AUTO_INCREMENT PRIMARY KEY,\
    firstName VARCHAR(255), \
    lastName VARCHAR(255), \
    studentNumber INT(20), \
    department VARCHAR(255), \
    vehicleType VARCHAR(255))")

'''
    idagdag to kapag na-code na ung file handling for pictures
    userPhoto VARCHAR(255), \
    vechiclePhoto VARCHAR(255)\
    '''

def registerUser():
    sqlCommand = "INSERT INTO registeredUsers (firstName, lastName, studentNumber, department, vehicleType) VALUES (%s, %s, %s, %s, %s)"
    values = (fNameField.get(), lNameField.get(), StudentNoField.get(), deptOptionsDrpDwn.get(), vehicleOptionsDrpDwn.get())
    cursor.execute(sqlCommand, values)
    DB.commit()

def dbquery(): #this function is temporary. This just shows all data in the table
    dataQuery = Tk()
    dataQuery.title("Data Query")
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
    cursor.execute('DROP TABLE registeredUsers')

def fNameClearOnClick(event):
    fNameField.delete(0,END)
def lNameClearOnClick(event):
    lNameField.delete(0,END)
def studentNoClearOnClick(event):
    StudentNoField.delete(0,END)

#text/labels
heading = Label(root, text="Registration Form",bg="darkgreen", font=("Microsoft YaHei UI Light", 15,"bold"),width=40)
heading.place(relx=0.2, rely=0.2)

LineLang=  Label(root, text="   ",bg="black", font=("Microsoft YaHei UI Light", 1,"bold"),width=240)
LineLang.place(relx=0.2,rely=0.625)

Vehicle= Label(root, text="  VEHICLE  ",font=("Microsoft YaHei UI Light", 12,"bold"),width=14)
Vehicle.place(relx=0.2,rely=0.675)

#input/entry
fNameField= Entry(root, width=20,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 10))
fNameField.place(relx=0.4, rely=0.3)
fNameField.insert(0,"First Name")
fNameField.bind("<Button-1>",fNameClearOnClick)

lNameField= Entry(root, width=20, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light",10))
lNameField.place(relx=0.6, rely=0.3)
lNameField.insert(0,"Last Name")
lNameField.bind("<Button-1>",lNameClearOnClick)

StudentNoField= Entry(root, width=43, fg="black", border=2, bg="white",font=("Microsoft YaHei UI Light",10))
StudentNoField.place(relx=0.4,rely=0.425)
StudentNoField.insert(0,"Faculty / Student No.")
StudentNoField.bind("<Button-1>",studentNoClearOnClick)

#Combo Boxes
deptOptionsDrpDwn = ttk.Combobox(root, value = ["Select Department","College of Engineering", "College of Education", "College of Arts and Sciences", "College of Allied Health and Sciences", "College of Business Administration and Accountancy", "College of Computing Studies"])
deptOptionsDrpDwn.current(0)
deptOptionsDrpDwn.place(relx=0.4, rely=0.525, width=305)

vehicleOptionsDrpDwn = ttk.Combobox(root, value = ["Select Type of Vehicle","Bike", "E-Bike", "Motorcycle"," Car"])
vehicleOptionsDrpDwn.current(0)
vehicleOptionsDrpDwn.place(relx=0.4,rely=0.672)

#Buttons
PicHolder= Button(root, text="PHOTO HERE", bg="white", width=20,height=8)
PicHolder.place(relx=0.2, rely=0.3)

VehiclePDF= Button(root, text="Upload Vehicle PDF", bg="white", width=20)
VehiclePDF.place(relx=0.6, rely=0.672)

Reg_button = Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command=registerUser)
Reg_button.place(relx= 0.4, rely=0.85)


#temporary buttons
test_button = Button(root, text="Query", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command=dbquery)
test_button.place(relx= 0.4, rely=0.75)

cleardb_button = Button(root, text="Clear database", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=12, command=clearDB)
cleardb_button.place(relx= 0.65, rely=0.75)

root.mainloop()