import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image

root= tk.Tk()
root.title("PNC Parking Registration")
root.geometry("800x450")
root.iconbitmap(r"C:\Users\Admin\Downloads\334524180_902897874326778_6090952642815903161_n.ico")
image_0=Image.open(r"C:\Users\Admin\Downloads\398404165_204899129363982_1310191754435457287_n.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)

#var
DEPTOPT=["College of Engineering","College of Education","College of Arts and Sciences","College of Allied Health and Sciences","College of Business Administration and Accountancy","College of Computing Studies"] 
selected_DEPT= tk.StringVar()
selected_DEPT.set(DEPTOPT[0])

#display
Registration_text= tk.Label(root, text="Registration",font="berlinsans",bg="darkgreen",width=20, height=1,)
Registration_text.place(relx=0.39, rely=0.3)
F_NAME= tk.Message(root, text="FIRST NAME", width=80)
F_NAME.place(relx=0.32, rely=0.4)
F_NAME_FIELD= tk.Entry(root, width=20)
F_NAME_FIELD.place(relx=0.29, rely=0.47)
L_NAME= tk.Message(root, text="LAST NAME", width=80)
L_NAME.place(relx= 0.58, rely=0.4)
LN_FIELD= tk.Entry(root, width=20)
LN_FIELD.place(relx=0.55, rely=0.47)
ST_NO= tk.Message(root, text="FACULTY / STUDENT NO.", width=150)
ST_NO.place(relx=0.28,rely=0.55)
ST_NO_FIELD=tk.Entry(root, width=20) 
ST_NO_FIELD.place(relx=0.29,rely=0.62)
DEPT=tk.Message(root, text="DEPARTMENT",width=80)
DEPT.place(relx=0.58,rely=0.55)
DEPTOPTIONS= tk.OptionMenu(root, selected_DEPT, *DEPTOPT)
DEPTOPTIONS.place(relx=0.53, rely=0.6)
SIGNUP_button= tk.Button(root, text="SIGN UP", bg="white" ,width=20)
SIGNUP_button.place(relx= 0.41, rely=0.77)



root.mainloop()