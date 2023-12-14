import tkinter as tk
import sqlite3
from datetime import datetime
from datetime import date
from datetime import time
from pytz import timezone
import datetime


def timezoneAttempt1():
    phtz = timezone('Asia/Singapore')
    timeUTC = datetime.datetime.now(datetime.timezone.utc)
    phST = timeUTC.astimezone(phtz) 
    today = date.today()
    print(phST)
def timezoneAttempt2():
    return

def clockUpdate():
    
    return




root = tk.Tk()
root.title("PN Parking")
root.geometry("400x220")

connection = sqlite3.connect("School_Parking_Database.db")
cursor = connection.cursor()

#create table
'''
cursor.execute("""CREATE TABLE parkingLog(
    studentNumber text,
    typeOfVehicle text,
    timeIn text,
    timeOut text
    )""")
'''

def confirm():
    connection = sqlite3.connect("School_Parking_Database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO parkingLog VALUES (:studentNumber, :typeOfVehicle, :timeIn, :timeOut)",
        {
            'studentNumber':scan_id_text.get(),
            'typeOfVehicle':TOV_option_menu.get()
        }
    )
    clearField()

def query ():
    connection = sqlite3.connect("School_Parking_Database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM parkingLog")

def clearField():
    scan_id_text.delete(0,'end')
    selected_TOV.set(TOV_options[0])

#option var
TOV_options=[
    "     Bicycle      ",
    "    Motorcycle    ",
    "      E-Bike      ",
    "       Car        "
] 

selected_TOV= tk.StringVar()
selected_TOV.set(TOV_options[0])


#display entry
scan_id_display= tk.Label(root, text="SCAN ID QR CODE", width=100)
scan_id_display.grid(row=1,column=0,pady=(20,0))

#kung single line entry lang, goods na ang Entry widget (tk.Entry)
scan_id_text= tk.Entry(root, width=18)
scan_id_text.grid(row=2,column=0,padx=(20,0))

TOV_display= tk.Message(root, text="Type of Vehicle", width=100)
TOV_display.grid(row=4,column=0,pady=(20,0))

TOV_option_menu= tk.OptionMenu(root, selected_TOV, *TOV_options)
TOV_option_menu.grid(row=5, column=0,padx=(0,0))

Confirm_button= tk.Button(root, text="Confirm", command = clearField)
Confirm_button.grid(row=6, column=0, pady=(30,0))

Clear_button= tk.Button(root, text="Clear")
Clear_button.grid(row=6, column=1, pady=(30,0))

root.mainloop()