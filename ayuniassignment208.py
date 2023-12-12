import sqlite3
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ALY LIBRARY MEMBERSHIP SYSTEM")
root.geometry("3000x3000")
my_tree = ttk.Treeview(root)
storeName = "ALY LIBRARY MEMBERSHIP SYSTEM"


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( id, name, gender, no_phone, email):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemId TEXT, itemName TEXT, itemGender TEXT, itemNo_phone TEXT, itemEmail TEXT)""")
    
    cursor.execute("INSERT INTO inventory VALUES ('" + str(id) + "','" + str(name) + "','" + str(gender) + "','" + str(no_phone) + "','" + str(email) + "')")
    conn.commit()
    

def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemGender TEXT, itemNo_phone TEXT, itemEmail TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()


def update(id, name, gender, no_phone, email,  idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemGender TEXT, itemNo_phone TEXT, itemEmail TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = '" + str(id) + "', itemName = '" + str(name) + "', itemGender = '" + str(gender) + "', itemNo_phone = '" + str(no_phone) +  "', itemEmail = '" + str(email) + "' WHERE itemId='"+str(idName)+"'")
    conn.commit()


def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemGender TEXT, itemNo_phone TEXT, itemEmail TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results


def insert_data():
    itemId = str(entryId.get())
    itemName = str(entryName.get())
    itemGender = str(entryGender.get())
    itemNo_phone = str(entryNo_phone.get())
    itemEmail = str(entryEmail.get())
    if itemId == "" or itemName == " ":
        print("Error Inserting Id")
    elif itemName == "" or itemName == " ":
        print("Error Inserting Name")
    elif itemGender == "" or itemGender == " ":
        print("Error Inserting Gender")
    elif itemNo_phone == "" or itemNo_phone == " ":
        print("Error Inserting No_phone")
    elif itemEmail == "" or itemEmail == " ":
        print("Error Inserting Email")    
    else:
        insert(str(itemId), str(itemName), str(itemGender), str(itemNo_phone), str(itemEmail))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0]) 
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryId.get(), entryName.get(), entryGender.get(), entryNo_phone.get(), entryEmail.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

#grid and label

titleLabel = Label(root, text=storeName, font=('Cooper Black', 30), bd=2, bg= "#00BFFF" )
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Cooper Black', 15))
nameLabel = Label(root, text="Name", font=('Cooper Black', 15))
genderLabel = Label(root, text="Gender", font=('Cooper Black', 15))
no_phoneLabel = Label(root, text="No_phone", font=('Cooper Black', 15))
emailLabel = Label(root, text="Email", font=('Cooper Black', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
genderLabel.grid(row=3, column=0, padx=10, pady=10)
no_phoneLabel.grid(row=4, column=0, padx=10, pady=10)
emailLabel.grid(row=5, column=0, padx=10, pady=10)

entryId = Entry(root, width=25, bd=5, font=('Cooper Black', 15))
entryName = Entry(root, width=25, bd=5, font=('Cooper Black', 15))
entryGender = Entry(root, width=25, bd=5, font=('Cooper Black', 15))
entryNo_phone = Entry(root, width=25, bd=5, font=('Cooper Black', 15))
entryEmail = Entry(root, width=25, bd=5, font=('Cooper Black', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryGender.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryNo_phone.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
entryEmail.grid(row=5, column=1, columnspan=3, padx=5, pady=5)


# button 

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Cooper Black', 15), bg="#00C957", command=insert_data)
buttonEnter.grid(row=6, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Cooper Black', 15), bg="#97FFFF", command=update_data)
buttonUpdate.grid(row=6, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Cooper Black', 15), bg="#B22222", command=delete_data)
buttonDelete.grid(row=6, column=3, columnspan=1)

#style table

style = ttk.Style()
style.configure("Treeview.Heading", font=('Cooper Black', 15))

my_tree['columns'] = ("ID", "Name", "Gender", "No_phone", "Email")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=200)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Gender", anchor=W, width=120)
my_tree.column("No_phone", anchor=W, width=120)
my_tree.column("Email", anchor=W, width=120)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Gender", text="Gender", anchor=W)
my_tree.heading("No_phone", text="No_phone", anchor=W)
my_tree.heading("Email", text="Email", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Cooper Black', 15))
my_tree.grid(row=1, column=6, columnspan=5, rowspan=6, padx=12, pady=12)

root.mainloop()
