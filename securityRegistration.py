from tkinter import*
from PIL import ImageTk, Image
import mysql.connector

'''
=== SCRIPT TASK===
create database for accounts of security
gagawa ng clears when clicked
gumawa ng if statement logic na dapat parehas ung password na ininput
'''
#window
root = Tk()
root.title("PNC Parking Security Account Registration")
root.geometry("800x450")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("securityRegistrationBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#connect to database
DB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'sercurityAccountDatabase',
)
#print(DB) #checks if connected sa database

cursor = DB.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS sercurityAccountDatabase")

'''
cursor.execute('SHOW DATABASES')
for db in cursor:
    print(db)
'''
#create table

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
    sqlCommand = "INSERT INTO registeredSecurity (firstName, lastName, username, password) VALUES (%s, %s, %s, %s)"
    values = (fNameField.get(), lNameField.get(), usernameField.get(), pwField.get())
    cursor.execute(sqlCommand, values)
    DB.commit()

def dbquery(): #this function is temporary. This just shows all data in the table
    dataQuery = Tk()
    dataQuery.title("Data Query")
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

def varTrace(var, index, mode):
    fieldContentLogic(pwVar,pwField)
    fieldContentLogic(confirmVar,confirmPwField)


def fieldContentLogic(_var,_field):
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

def clearDB(): #temporary function
    cursor.execute('DROP TABLE registeredSecurity')

#text/labels
loginText= Label(root, text="Security Registration",font="berlinsans",bg="darkgreen",width=30, height=1,)
loginText.place(relx=0.31, rely=0.25,)


#entry/fields
fNameField= Entry(root, width=20,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
fNameField.place(relx=0.3, rely=0.35)
fNameField.insert(0,"First Name")
fNameField.bind("<Button-1>",fNameClearOnClick)


lNameField= Entry(root, width=20, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light",9))
lNameField.place(relx=0.485, rely=0.35)
lNameField.insert(0,"Last Name")
lNameField.bind("<Button-1>",lNameClearOnClick)

usernameField= Entry(root, width=40,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
usernameField.place(relx=0.3, rely=0.42)
usernameField.insert(0,"                            Username")
usernameField.bind("<Button-1>",usernameClearOnClick)

#put some logic for the show="*" para makita ung text
pwVar = StringVar()
pwVar.trace_add('write', varTrace)
pwField= Entry(root, textvariable = pwVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
pwField.place(relx=0.3, rely=0.49)
pwField.insert(0,"                             Password")
pwField.bind("<Button-1>",pwClearOnClick)

confirmVar = StringVar()
confirmVar.trace_add('write', varTrace)
confirmPwField= Entry(root, textvariable = confirmVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
confirmPwField.place(relx=0.3, rely=0.56)
confirmPwField.insert(0,"                        Confirm Password")
confirmPwField.bind("<Button-1>",confirmClearOnClick)

#buttons
PicHolder=Button(root, text="PHOTO HERE", bg="white", width=15,height=6)
PicHolder.place(relx=0.3, rely=0.63)

UploadButton= Button(root,text="Upload photo", bg="white", width=15)
UploadButton.place(relx=0.49,rely=0.67)

Reg_button= Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18, command = registerSecurity)
Reg_button.place(relx= 0.46, rely=0.78)

querybutton= Button(root, text="Query", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command = dbquery)
querybutton.place(relx= 0.7, rely=0.78)

clearDBbutton= Button(root, text="clear DB", bg="yellow" ,font=("Microsoft YaHei UI Light",10,"bold"),width=10, command = clearDB)
clearDBbutton.place(relx= 0.85, rely=0.78)

root.mainloop()
