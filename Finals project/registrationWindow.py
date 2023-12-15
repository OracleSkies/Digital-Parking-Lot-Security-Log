import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image

root= tk.Tk()
root.title("PNC Parking Registration")
root.geometry("800x450")
root.iconbitmap(r"C:\Users\Admin\Downloads\334524180_902897874326778_6090952642815903161_n.ico")
image_0=Image.open(r"C:\Users\Admin\Downloads\410416337_675750344428577_6935728864826318124_n.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)


#var
DEPTOPT=["College of Engineering","College of Education","College of Arts and Sciences","College of Allied Health and Sciences","College of Business Administration and Accountancy","College of Computing Studies"] 
selected_DEPT= tk.StringVar()
selected_DEPT.set("Department")

TOVOPT=["Bike", "E-Bike", "Motorcycle"," Car "]
selected_TOVOPT= tk.StringVar()
selected_TOVOPT.set("Type of Vehicle")


#text/labels
heading= tk.Label(root, text="Registration Form",bg="darkgreen", font=("Microsoft YaHei UI Light", 15,"bold"),width=40)
heading.place(relx=0.2, rely=0.2)

LineLang=  tk.Label(root, text="   ",bg="black", font=("Microsoft YaHei UI Light", 1,"bold"),width=240)
LineLang.place(relx=0.2,rely=0.625)

Vehicle= tk.Label(root, text="  VEHICLE  ",font=("Microsoft YaHei UI Light", 12,"bold"),width=14)
Vehicle.place(relx=0.2,rely=0.675)

#input/entry
fNameField= tk.Entry(root, width=20,fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 10))
fNameField.place(relx=0.4, rely=0.3)
fNameField.insert(0,"First Name")

lNameField= tk.Entry(root, width=20, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light",10))
lNameField.place(relx=0.6, rely=0.3)
lNameField.insert(0,"Last Name")

StudentNoField= tk.Entry(root, width=43, fg="gray", border=2, bg="white",font=("Microsoft YaHei UI Light",10))
StudentNoField.place(relx=0.4,rely=0.425)
StudentNoField.insert(0,"Faculty / Student No.")


#Optionmenus
DEPTOPTIONS= tk.OptionMenu(root, selected_DEPT, *DEPTOPT)
DEPTOPTIONS.place(relx=0.4, rely=0.525)

TOVOPTIONS=tk.OptionMenu(root,selected_TOVOPT,*TOVOPT)
TOVOPTIONS.place(relx=0.4,rely=0.672)


#Buttons
PicHolder=tk.Button(root, text="PHOTO HERE", bg="white", width=20,height=8)
PicHolder.place(relx=0.2, rely=0.3)

VehiclePDF=tk.Button(root, text="Upload Vehicle PDF", bg="white", width=20)
VehiclePDF.place(relx=0.6, rely=0.672)

Reg_button= tk.Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18)
Reg_button.place(relx= 0.4, rely=0.85)


#SHEEESSHHHHHHSHHHSHSHSHSHSH
root.mainloop()