import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image


#window
root = tk.Tk()
root.title("PNC Parking")
root.geometry("800x450")
root.iconbitmap(r"C:\Users\Admin\Downloads\334524180_902897874326778_6090952642815903161_n.ico")
image_0=Image.open(r"C:\Users\Admin\Downloads\Security_regwin_bg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#text/labels
loginText= tk.Label(root, text="Security Registration",font="berlinsans",bg="darkgreen",width=30, height=1,)
loginText.place(relx=0.31, rely=0.25,)


#entry/fields
fNameField= tk.Entry(root, width=20,fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
fNameField.place(relx=0.3, rely=0.35)
fNameField.insert(0,"First Name")

lNameField= tk.Entry(root, width=20, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light",9))
lNameField.place(relx=0.485, rely=0.35)
lNameField.insert(0,"Last Name")

usernameField= tk.Entry(root, width=40,fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
usernameField.place(relx=0.3, rely=0.42)
usernameField.insert(0,"                            Username")

pwField= tk.Entry(root, width=40, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
pwField.place(relx=0.3, rely=0.49)
pwField.insert(0,"                             Password")

confirmPwField= tk.Entry(root, width=40, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 9))
confirmPwField.place(relx=0.3, rely=0.56)
confirmPwField.insert(0,"                        Confirm Password")


#buttons
PicHolder=tk.Button(root, text="PHOTO HERE", bg="white", width=15,height=6)
PicHolder.place(relx=0.3, rely=0.63)

UploadButton=tk.Button(root,text="Upload photo", bg="white", width=15)
UploadButton.place(relx=0.49,rely=0.67)

Reg_button= tk.Button(root, text="Register", bg="darkgreen" ,font=("Microsoft YaHei UI Light",10,"bold"),width=18)
Reg_button.place(relx= 0.46, rely=0.78)


root.mainloop()