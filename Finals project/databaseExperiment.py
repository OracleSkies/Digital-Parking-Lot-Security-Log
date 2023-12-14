import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("database test")
root.geometry("400x400")

#Database
connection = sqlite3.connect("databaseTest.db")
cursor = connection.cursor()
#create table

cursor.execute("""CREATE TABLE addresses (
    firstName text,
    lastName text,
    address text
    )""")

#create submit funtion
def submit():
    connection = sqlite3.connect("databaseTest.db")
    cursor = connection.cursor()
    #Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:fName,:lName,:address)",
        {
            'fName':fNameEntry.get(),
            'lName':lNameEntry.get(),
            'address':addressEntry.get()
        }
    )
    clear()

    #commiting changes
    connection.commit()
    #closing Connection
    connection.close()

def clear():
    fNameEntry.delete(0,'end')
    lNameEntry.delete(0,'end')
    addressEntry.delete(0,'end')

def query():
    connection = sqlite3.connect("databaseTest.db")
    cursor = connection.cursor()

    #query database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print(records)
    printRecords = ""
    for record in records:
        printRecords += str(record[0]) +" "+str(record[1]) + " "+ str(record[2]) + '\n'
    
    queryLabel = tk.Label(root,text = printRecords)
    queryLabel.grid(row=8, column=0,columnspan=2)

    connection.commit()
    connection.close()

#text boxes
fNameEntry = tk.Entry(root, width=30)
fNameEntry.grid(row=0,column=1,padx=20)
lNameEntry = tk.Entry(root, width=30)
lNameEntry.grid(row=1,column=1,padx=20)
addressEntry = tk.Entry(root, width=30)
addressEntry.grid(row=2,column=1,padx=20)

#labels
fNameLabel = tk.Label(root, text="First Name")
fNameLabel.grid(row=0,column=0)
lNameLabel = tk.Label(root, text="Last Name")
lNameLabel.grid(row=1,column=0)
addressLabel = tk.Label(root, text="Address")
addressLabel.grid(row=2,column=0)

#buttons
submitButton = tk.Button(root, text="Submit",command=submit)
submitButton.grid(row=3, column=0,columnspan=2, pady=10,padx=10,ipadx=100)
queryButton = tk.Button(root, text="Show Records", command=query)
queryButton.grid(row=4, column =0, columnspan=2, pady=10, padx=10,ipadx=82)

#commiting changes
connection.commit()
#closing Connection
connection.close()
root.mainloop()
