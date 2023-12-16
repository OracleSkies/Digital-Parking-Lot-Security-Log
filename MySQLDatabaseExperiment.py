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
submitButton = Button(root, text="Submit")
submitButton.grid(row=8, column=0, columnspan=2,padx=10,pady=10)

root.mainloop()