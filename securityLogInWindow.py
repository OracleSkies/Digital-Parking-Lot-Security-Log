import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image


#window
root = tk.Tk()
root.title("PNC Parking")
root.geometry("397x400")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("securityLogInWindowBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#text/labels
loginText= tk.Label(root, text="SECURITY LOG IN",font="berlinsans",bg="darkgreen",width=20, height=1,)
loginText.place(relx=0.27, rely=0.28,)


#entryfields
usernameField= tk.Entry(root, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 10),width=17)
usernameField.place(relx=0.37, rely=0.42)
usernameField.insert(0,"Username")

pwField= tk.Entry(root, fg="gray",border=2, bg="white", font=("Microsoft YaHei UI Light", 10),width=17)
pwField.place(relx=0.37, rely=0.52)
pwField.insert(0,"Password")


#buttons
forgotPwButton= tk.Button(root, text="Forgot Password?",bg="white")
forgotPwButton.place(relx=0.495, rely=0.64)

loginButton= tk.Button(root, text="LOG IN", bg="darkgreen" ,width=20)
loginButton.place(relx= 0.32, rely=0.78)

root.mainloop()