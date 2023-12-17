from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
import csv

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

#submits information to database
def sumbitInfo():
    sqlCommand = "INSERT INTO customers (firstName, lastName, addressID, price, email, city, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s)" #%s = placeholder
    values = (firstNameEntry.get(), lastNameEntry.get(), addressIDEntry.get(), priceEntry.get(), emailEntry.get(), cityEntry.get(), phoneEntry.get())
    cursor.execute(sqlCommand, values)
    #commit changes to database
    db.commit()
    #clears the fields
    clearFields()

#show all info in database to another window
def dbquery():
    #sets up new window
    customerDataQuery = Tk()
    customerDataQuery.title("Show All Data")
    customerDataQuery.iconbitmap('PNCLogo.ico')
    customerDataQuery.geometry('800x600')

    #query/shows all data to new window
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    #medyo complicated na loop left to right, up to down
    for index, tableRow in enumerate(result):
        num = 0
        for tableColumn in tableRow:
            dataQueryLabel = Label(customerDataQuery,text=tableColumn) 
            # add index to x to get the specific field u want (eg x[0] would give you the 0th column of the database which is the first name) 
            dataQueryLabel.grid(row=index, column=num, padx=5)
            num += 1
    csvButton = Button(customerDataQuery, text="Save as Spreadsheet", command=lambda:exportToExcel(result))
    csvButton.grid(row=index+1,column=0)

#export to csv excel https://www.youtube.com/watch?v=2MMwfNKN1_s&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=32
def exportToExcel(_result):
    with open("customer.csv", "a", newline="") as file:
        writer = csv.writer(file, dialect='excel')
        for record in _result:
            writer.writerow(record)

#search for customers using their names
def searchCustomer():
    searchCustomerWindow = Tk()
    searchCustomerWindow.title("Search for Customer")
    searchCustomerWindow.iconbitmap('PNCLogo.ico')
    searchCustomerWindow.geometry('800x600')
    def searchNow():
        selected = dropDown.get()
        sql=""
        if selected == "Search by...":
            test = Label(searchCustomerWindow, text="Please select from the drop box")
            test.grid(row=1, column=1)

        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE lastName = %s"
            
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"
            
        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE userID = %s"
    
        
        searched = searchCustomerEntry.get()
        name = (searched, )
        result = cursor.execute(sql, name)
        result = cursor.fetchall()
        if not result:
            result = "Record Not Found"
        searchedLabel = Label(searchCustomerWindow, text=result)
        searchedLabel.grid(row=2, column=0, padx=10, sticky=W, columnspan=2)
        

    #entry box to search for customer
    searchCustomerEntry = Entry(searchCustomerWindow)
    searchCustomerEntry.grid(row=0, column=1, padx=10, pady=10)
    searchCustomerLabel = Label(searchCustomerWindow, text="Search Customer: ")
    searchCustomerLabel.grid(row=0, column=0, padx=10, pady=10)
    searchButton = Button(searchCustomerWindow, text="Search", command=searchNow)
    searchButton.grid(row=1, column=0, padx=10)
    dropDown = ttk.Combobox(searchCustomerWindow, value = ["Search by...","Last Name", "Email Address","Customer ID"])
    dropDown.current(0)
    dropDown.grid(row=0, column=2)

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
submitButton.grid(row=8, column=0,padx=10, pady=10)
clearFieldsButton = Button(root, text="Clear",command=clearFields)
clearFieldsButton.grid(row=8, column=1)
queryButton = Button(root, text="Show All Data", command=dbquery)
queryButton.grid(row=9, column=0, sticky=W, padx=10)
searchCustomersButton = Button(root,text="Search for Customers", command=searchCustomer)
searchCustomersButton.grid(row=9, column=1, sticky=W, padx=10)

root.mainloop()