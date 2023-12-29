from tkinter import*
from PIL import ImageTk, Image
import mysql.connector

'''
===SCRIPT Tasks===
GOODS na to >>> try iconnect sa registeredParkingUsersDatabase and script na to 
Implement Database Lookup for registered parking users
need maglagay nung time aspect para sa time in and out
'''

#window
root = Tk()
root.title("PNC Parking")
root.geometry("400x314")
root.iconbitmap("PNCLogo.ico")
image_0=Image.open("scanWindowBGupdated.png")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.grid(row=0, column=0)
root.resizable(False,False)

DB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    
)
#print(DB) #check if connected to MySQL

cursor = DB.cursor()

def dbquery(): #temporary function. Trash this later
    dataQuery = Tk()
    dataQuery.title("Data Query")
    dataQuery.geometry('800x600')
    cursor.execute("SELECT * FROM registeredUsers")
    result = cursor.fetchall()
    for index, tableRow in enumerate(result):
        num = 0
        for tableColumn in tableRow:
            dataQueryLabel = Label(dataQuery,text=tableColumn) 
            dataQueryLabel.grid(row=index, column=num, padx=5)
            num += 1

def checkUserToDatabase():
    sqlCommand = "SELECT * FROM registeredUsers WHERE studentNumber = %s" 
    scannedStdnNo = scanIDfield.get()
    stdnNumber = (scannedStdnNo, )
    cursor.execute(sqlCommand, stdnNumber)
    result = cursor.fetchone()

    #checker lang to. Trash this
    if result:
        print("data exist")
    else:
        print("data doesnt exist")

#timeholder
DTholder= Label(root,text="January 1, 2023 | 10:30 AM", font=("Segoe",10),bg="#f8faf7", width=25, height=1)
DTholder.place(relx=0.53, rely=0.02)

#label
ParkingLotScan= Label(root, text="Parking Lot Scanner",font="berlinsans",bg="darkgreen",width=21, height=1,)
ParkingLotScan.place(relx=0.249, rely=0.35,)


#text
ScanID= Label(root,text="Scan ID", font="berlinsans", width=12, height=1)
ScanID.place(relx=0.258,rely=0.49)


#entry/field
scanIDfield= Entry(root, width=20,border=2, bg="white")
scanIDfield.place(relx=0.33,rely=0.56)


#Button
confirmButton= Button(root, text="Confirm", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10, command=checkUserToDatabase)
confirmButton.place(relx=0.4,rely=0.72)

#temporary button. trash this later
queryButton= Button(root, text="query", bg="darkgreen" ,font=("Microsoft YaHei UI Light",8,"bold"),width=10, command=dbquery)
queryButton.place(relx=0.4,rely=0.85)

root.mainloop()