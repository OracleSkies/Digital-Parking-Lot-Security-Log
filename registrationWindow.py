
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import csv

root = Tk()
root.title("PNC Parking Registration")
root.geometry("800x450")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("main_regwindow_bg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#database = 

#var
#change to combobox
deptOptionsDrpDwn = ttk.Combobox(root, value = ["Select Department","College of Engineering", "College of Education", "College of Arts and Sciences", "College of Allied Health and Sciences", "College of Business Administration and Accountancy", "College of Computing Studies"])
deptOptionsDrpDwn.current(0)
deptOptionsDrpDwn.place(relx=0.4, rely=0.525, width=305)

vehicleOptionsDrpDwn = ttk.Combobox(root, value = ["Select Type of Vehicle","Bike", "E-Bike", "Motorcycle"," Car"])
vehicleOptionsDrpDwn.current(0)
vehicleOptionsDrpDwn.place(relx=0.4,rely=0.672)
'''
DEPTOPT=["College of Engineering",
    "College of Education",
    "College of Arts and Sciences",
    "College of Allied Health and Sciences",
    "College of Business Administration and Accountancy",
    "College of Computing Studies"
    ] 

selected_DEPT = StringVar()
selected_DEPT.set("Department")

#change to combobox
TOVOPT=["Bike", "E-Bike", "Motorcycle"," Car "]
selected_TOVOPT= StringVar()
selected_TOVOPT.set("Type of Vehicle")
'''


#text/labels
heading = Label(root, text="Registration Form",bg="darkgreen", font=("Microsoft YaHei UI Light", 15,"bold"),width=40)
heading.place(relx=0.2, rely=0.2)

LineLang=  Label(root, text="   ",bg="black", font=("Microsoft YaHei UI Light", 1,"bold"),width=240)
LineLang.place(relx=0.2,rely=0.625)

Vehicle= Label(root, text="  VEHICLE  ",font=("Microsoft YaHei UI Light", 12,"bold"),width=14)
Vehicle.place(relx=0.2,rely=0.675)

#input/entry
fNameField= Entry(root, width=20,fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 10))
fNameField.place(relx=0.4, rely=0.3)
fNameField.insert(0,"First Name")

lNameField= Entry(root, width=20, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light",10))
lNameField.place(relx=0.6, rely=0.3)
lNameField.insert(0,"Last Name")

StudentNoField= Entry(root, width=43, fg="gray", border=2, bg="white",font=("Microsoft YaHei UI Light",10))
StudentNoField.place(relx=0.4,rely=0.425)
StudentNoField.insert(0,"Faculty / Student No.")


#Optionmenus
'''
DEPTOPTIONS= OptionMenu(root, selected_DEPT, *DEPTOPT)
DEPTOPTIONS.place(relx=0.4, rely=0.525)

TOVOPTIONS= OptionMenu(root,selected_TOVOPT,*TOVOPT)
TOVOPTIONS.place(relx=0.4,rely=0.672)
'''

#Buttons
PicHolder= Button(root, text="PHOTO HERE", bg="white", width=20,height=8)
PicHolder.place(relx=0.2, rely=0.3)

VehiclePDF= Button(root, text="Upload Vehicle PDF", bg="white", width=20)
VehiclePDF.place(relx=0.6, rely=0.672)

Reg_button = Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18)
Reg_button.place(relx= 0.4, rely=0.85)

root.mainloop()