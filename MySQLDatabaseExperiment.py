from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('MySQLDBExp')
root.iconbitmap('PNCLogo.ico')
root.geometry('400x400')

#connection to MySQL
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'experimentDatabase',
)


#create and initialize cursor
cursor = db.cursor()

#create database
cursor.execute("CREATE DATABASE IF NOT EXISTS experimentDatabase")

#database creation test
'''
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
'''
# Drop (delete) Table
#cursor.execute ("DROP TABLE customers")

#create table
cursor.execute("CREATE TABLE IF NOT EXISTS customers ( firstName VARCHAR(255), \
    lastName VARCHAR(255), \
    addressID INT(10), \
    price DECIMAL(10,2), \
    userID INT AUTO_INCREMENT PRIMARY KEY)")

'''
#alter table
cursor.execute("ALTER TABLE IF customers ADD (\
    email VARCHAR(255),\
    city VARCHAR(255),\
    phoneNumber VARCHAR(255))")
'''
'''
#show table
cursor.execute("SELECT * FROM customers")
for element in cursor.description:
    print(element)
'''
def clearFields():
    firstNameEntry.delete(0,END)
    lastNameEntry.delete(0,END)
    addressIDEntry.delete(0,END)
    priceEntry.delete(0,END)
    emailEntry.delete(0,END)
    cityEntry.delete(0,END)
    phoneEntry.delete(0,END)

def sumbitInfo():
    sqlCommand = "INSERT INTO customers (firstName, lastName, addressID, price, email, city, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s)" #%s = placeholder
    values = (firstNameEntry.get(), lastNameEntry.get(), addressIDEntry.get(), priceEntry.get(), emailEntry.get(), cityEntry.get(), phoneEntry.get())
    cursor.execute(sqlCommand, values)
    #commit changes to database
    db.commit()
    #clears the fields
    clearFields()

def dbquery():
    #query
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    for x in result:
        print(x)

#Title with Label widget
titleLabel = Label(root, text="Experiment Customer Database", font=("Helvatica", 16))
titleLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

#main form for fields
#labels
firstNameLabel = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
lastNameLabel = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
addressIDLabel = Label(root, text="Address").grid(row=3, column=0, sticky=W, padx=10)
priceLabel = Label(root, text="Price").grid(row=4, column=0, sticky=W, padx=10)
emailLabel = Label(root, text="Email").grid(row=5, column=0, sticky=W, padx=10)
cityLabel = Label(root, text="City").grid(row=6, column=0, sticky=W, padx=10)
phoneLabel = Label(root, text="Phone Number").grid(row=7, column=0, sticky=W, padx=10)
#entry boxes
firstNameEntry = Entry(root)
firstNameEntry.grid(row=1, column=1)
lastNameEntry = Entry(root)
lastNameEntry.grid(row=2, column=1,pady=5)
addressIDEntry = Entry(root)
addressIDEntry.grid(row=3, column=1,pady=5)
priceEntry = Entry(root)
priceEntry.grid(row=4, column=1,pady=5)
emailEntry = Entry(root)
emailEntry.grid(row=5, column=1,pady=5)
cityEntry = Entry(root)
cityEntry.grid(row=6, column=1,pady=5)
phoneEntry = Entry(root)
phoneEntry.grid(row=7, column=1,pady=5)
#buttons
submitButton = Button(root, text="Submit", command=sumbitInfo)
submitButton.grid(row=8, column=0,padx=10,pady=10)
clearFieldsButton = Button(root, text="Clear",command=clearFields)
clearFieldsButton.grid(row=8, column=1)

#query button. Trash this
queryButton = Button(root, text="Query", command=dbquery)
queryButton.grid(row=9, column=0)
root.mainloop()