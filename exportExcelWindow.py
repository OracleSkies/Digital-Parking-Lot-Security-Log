from tkinter import*
from PIL import ImageTk, Image

#window
root = Tk()
root.title("PNC Parking")
root.geometry("961x964")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("exportExcelWindowBG.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

#label
ParkingLotScan= Label(root, text="Export Excel",font=("Segoe",30,"bold"),bg="darkgreen",width=20, height=1,)
ParkingLotScan.place(relx=0.249, rely=0.3,)

#button
ParkUserButton=Button(root, text="Park User", font=("Segoe",20),width=30,height=1)
ParkUserButton.place(relx=0.249, rely=0.4)

RegStFtButton=Button(root, text="Registered Student and Faculty", font=("Segoe",20),width=30,height=1)
RegStFtButton.place(relx=0.249, rely=0.5)

RegScButton=Button(root, text="Registered Security", font=("Segoe",20),width=30,height=1)
RegScButton.place(relx=0.249, rely=0.6)


root.mainloop()
