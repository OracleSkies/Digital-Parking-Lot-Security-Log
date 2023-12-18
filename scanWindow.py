import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image


#window
root = tk.Tk()
root.title("PNC Parking")
root.geometry("400x315")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("scanWindowBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)


#label
ParkingLotScan= tk.Label(root, text="Parking Lot Scanner",font="berlinsans",bg="darkgreen",width=20, height=1,)
ParkingLotScan.place(relx=0.27, rely=0.32,)


#text
ScanID= tk.Label(root,text="Scan ID", font="berlinsans", width=12, height=1)
ScanID.place(relx=0.258,rely=0.47)


#entry/field
scanIDfield= tk.Entry(root, width=20,border=2, bg="white")
scanIDfield.place(relx=0.33,rely=0.54)


#Button
confirmButton=tk.Button(root, text="Confirm", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10)
confirmButton.place(relx=0.4,rely=0.7)

root.mainloop()