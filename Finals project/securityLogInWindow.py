import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image


#window
root = tk.Tk()
root.title("PNC Parking")
root.geometry("800x450")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("main_securitywindow_bg.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)


#text/labels
loginText= tk.Label(root, text="SECURITY LOG IN",font="berlinsans",bg="darkgreen",width=20, height=1,)
loginText.place(relx=0.39, rely=0.35,)

#entryfields
usernameField= tk.Entry(root, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 8),width=17)
usernameField.place(relx=0.44, rely=0.47)
usernameField.insert(0,"Username")

pwField= tk.Entry(root, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 8),width=17)
pwField.place(relx=0.44, rely=0.59)
pwField.insert(0,"Password")
#buttons
forgotPwButton= tk.Button(root, text="Forgot Password?",bg="white")
forgotPwButton.place(relx=0.495, rely=0.68)

loginButton= tk.Button(root, text="LOG IN", bg="darkgreen" ,width=20)
loginButton.place(relx= 0.41, rely=0.8)

root.mainloop()