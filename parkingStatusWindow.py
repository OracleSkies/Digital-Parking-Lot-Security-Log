import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image


#window
root = tk.Tk()
root.title("PNC Parking")
root.geometry("800x450")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("parkingStatusWindowBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)


#label
StudentInfo=tk.Label(root, text="Student Information",font=("berlinsans",20,"bold"),bg="darkgreen",width=47, height=2,)
StudentInfo.place(relx=0.001, rely=0.001,)

StudentName=tk.Label(root,text="Name:", font=("berlinsans",15),bg="lightgreen" ,width=8, height=1)
StudentName.place(relx=0.258,rely=0.25)

StudentNameFill=tk.Label(root,text="                               ", font=("berlinsans",15),bg="lightgreen" ,width=30, height=1)
StudentNameFill.place(relx=0.35,rely=0.25)

StudentDepartment=tk.Label(root,text="Department:", font=("berlinsans",15),bg="lightgreen" ,width=12, height=1)
StudentDepartment.place(relx=0.258,rely=0.35)

StudentDepartmentFill=tk.Label(root,text="                               ", font=("berlinsans",15),bg="lightgreen" ,width=30, height=1)
StudentDepartmentFill.place(relx=0.43,rely=0.35)

StudentNo=tk.Label(root, text="Student No.",font=("berlinsans",15),bg="lightgreen" ,width=10, height=1)
StudentNo.place(relx=0.03, rely=0.52)

StudentNoFill=tk.Label(root, text="               ",font=("berlinsans",15),bg="lightgreen" ,width=20, height=1)
StudentNoFill.place(relx=0.17, rely=0.52)

RegisteredVehicle= tk.Label(root, text="Type of Vehicle:",font=("berlinsans",15),bg="lightgreen" ,width=13, height=1)
RegisteredVehicle.place(relx=0.03, rely=0.62)


RegisteredVehicleFill= tk.Label(root, text="        ",font=("berlinsans",15),bg="lightgreen" ,width=18, height=1)
RegisteredVehicleFill.place(relx=0.21, rely=0.62)

TimeIn=tk.Label(root, text="Time in:",font=("berlinsans",15),bg="gray" ,width=7, height=1)
TimeIn.place(relx=0.03,rely=0.75)

TimeOut=tk.Label(root, text="Time out:",font=("berlinsans",15),bg="gray" ,width=8, height=1)
TimeOut.place(relx=0.3,rely=0.75)

TimeInFill=tk.Label(root, text="              ",font=("berlinsans",15),bg="lightgreen" ,width=9, height=1)
TimeInFill.place(relx=0.03,rely=0.85)

TimeOutFill=tk.Label(root, text="              ",font=("berlinsans",15),bg="lightgreen" ,width=10, height=1)
TimeOutFill.place(relx=0.3,rely=0.85)


#button
PicHolder=tk.Button(root, text="PHOTO HERE", bg="white", width=20,height=8)
PicHolder.place(relx=0.03, rely=0.2)

DoneButton=tk.Button(root, text="Done", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=12)
DoneButton.place(relx=0.48,rely=0.9)

root.mainloop()