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
    DBcommit()

def varTrace(var, index, mode):
    fieldContentLogic(pwVar,pwField)
    fieldContentLogic(cPwVar,confirmPwField)
    

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



#text/labels
loginText= Label(root, text="Security Registration",font="berlinsans",bg="darkgreen",width=30, height=1,)
loginText.place(relx=0.31, rely=0.25,)


#entry/fields
fNameField= Entry(root, width=20,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
fNameField.place(relx=0.3, rely=0.35)
fNameField.insert(0,"First Name")

lNameField= Entry(root, width=20, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light",9))
lNameField.place(relx=0.485, rely=0.35)
lNameField.insert(0,"Last Name")

usernameField= Entry(root, width=40,fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
usernameField.place(relx=0.3, rely=0.42)
usernameField.insert(0,"                            Username")

#put some logic for the show="*" para makita ung text
pwVar = StringVar()
pwVar.trace_add('write', varTrace)
pwField= Entry(root, textvariable = pwVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
pwField.place(relx=0.3, rely=0.49)
pwField.insert(0,"                             Password")

cPwVar = StringVar()
cPwVar.trace_add('write', varTrace)
confirmPwField= Entry(root, textvariable = cPwVar, width=40, fg="black",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
confirmPwField.place(relx=0.3, rely=0.56)
confirmPwField.insert(0,"                        Confirm Password")



#buttons
PicHolder=Button(root, text="PHOTO HERE", bg="white", width=15,height=6)
PicHolder.place(relx=0.3, rely=0.63)

UploadButton= Button(root,text="Upload photo", bg="white", width=15)
UploadButton.place(relx=0.49,rely=0.67)

Reg_button= Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18)
Reg_button.place(relx= 0.46, rely=0.78)

root.mainloop()
