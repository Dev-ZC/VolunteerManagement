import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
    
conn = sqlite3.connect('Volunteers.db')

c = conn.cursor()


#c.execute("""CREATE TABLE VolunteerInfo (
#                    firstname varchar(50) NOT NULL, 
#                    middleinitial varchar(1),
#                    lastname varchar(50) NOT NULL,
#                    phone varchar(20), 
#                    email varchar(50), 
#                    gender varchar(1) NOT NULL CHECK (gender IN ('M', 'F', 'O')), 
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    role varchar(50))""")

# Next have a way display number of total number of vounteers
# general data button that writes, the amount of each person per role, total amount of volunteers, and num people without a role
# Seperate database to assign each volunteer with a role 
# Have a search bar to see each person with a specific role
# Search for people without roles

#Select and return search
def find_vol():
    firstName = search_firstname_entry.get()
    lastName = search_lastname_entry.get()
    role = search_role_entry.get()
    gender = search_gender_combobox.get()
    if gender == "Male" :
        gender = "M"
    elif gender == "Female" :
        gender = "F"
    elif gender == "Other" :
        gender = "O"
        
    if len(firstName) != 0 or len(lastName) != 0 or len(role) != 0  or len(gender) != 0:
    
        sqlInsert = '''SELECT * FROM VolunteerInfo WHERE firstname=? OR lastname=? OR role=? OR gender=?'''
        
        c.execute(sqlInsert, (firstName, lastName, role, gender))
        results = c.fetchall()
        if len(results) == 0:
            print("")
            print("No volunteers found")
        else:
            if len(results) > 1:
                print(len(results), "Volunteers Found")
            else:
                print("One Volunteer Found!")
            for row in results:
                print("-----------")
                print("First Name: ", row[0])
                print("Middle Initial: ", row[1])
                print("Last Name: ", row[2])
                print("Phone Number: ", row[3])
                print("Email: ", row[4])
                print("Gender: ", row[5])
                print("Role: ", row[7])
    else:
        tk.messagebox.showwarning(title= "Error", message= "Please complete at least one field")
        
def display_all():
    sqlInsert = '''SELECT * FROM VolunteerInfo'''
        
    c.execute(sqlInsert)
    results = c.fetchall()
    if len(results) == 0:
        print("")
        print("No volunteers found")
    else:
        num_vol = len(results)
        print("")
        print("Volunteers Found:", num_vol)
        for row in results:
            print("-----------")
            print("First Name: ", row[0])
            print("Middle Initial: ", row[1])
            print("Last Name: ", row[2])
            print("Phone Number: ", row[3])
            print("Email: ", row[4])
            print("Gender: ", row[5])
            print("Role: ", row[7])

# FCN called to add volunteer to
def enter_data():
    #Assigning variables
    firstName = firstname_entry.get()
    lastName = lastname_entry.get()
    middleInitial = middleinitial_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    gender = gender_combobox.get()
    if gender == "Male" :
        gender = "M"
    elif gender == "Female" :
        gender = "F"
    elif gender == "Other" :
        gender = "O"
        
    if len(firstName) != 0 and len(lastName) != 0 and len(email) != 0  and len(gender) != 0:
        print("-----------")
        print("Volunteer Added to Database!")
        print("First Name: ", firstName)
        print("Middle Initial: ", middleInitial)
        print("Last Name: ", lastName)
        print("Phone Number: ", phone)
        print("Email: ", email)
        print("Gender: ", gender)
        sqlInsert = '''SELECT role FROM VolunteerInfo WHERE firstName=?'''
        c.execute(sqlInsert, (firstName,))
        result = c.fetchone()()
        print("Role: ", result)
        
        # Defines the SQL INSERT statement with placeholders for the values
        sqlInsert = '''INSERT INTO VolunteerInfo (firstname, lastname, middleinitial, phone, email, gender)
                    VALUES (?, ?, ?, ?, ?, ?)'''
        
        # Executes the INSERT statement with the variables as parameters
        c.execute(sqlInsert, (firstName, lastName, middleInitial, phone, email, gender))
        
        # Commits changes to the database
        conn.commit()
        
    else:
        tk.messagebox.showwarning(title= "Error", message= "Please complete each required field (with an *)")
        
        
def assign_role():
    firstName = rol_firstname_entry.get()
    lastName = rol_lastname_entry.get()
    role = rol_role_entry.get()
    
    if len(role) != 0 and len(firstName) != 0:
        sqlInsert = '''UPDATE VolunteerInfo SET role=? WHERE firstname=? AND lastname=?'''
        c.execute(sqlInsert, (role, firstName, lastName))
        print("Inserted: ", role, " to the profile of " , firstName, lastName)
    else:
        tk.messagebox.showwarning(title= "Error", message= "Please complete each field")
    
    
# GUI using Tkinter <----------------

root = tk.Tk()
#root.geometry("500x500")
#root.configure(bg='blue')
root.title("Volunteer Data Manager")

frame = tk.Frame(root)
frame.pack()

# Search Volunteer Frame 
search_vol_frame = tk.LabelFrame(frame, text="Search Volunteer's in Database")
search_vol_frame.grid(row = 0, column=0, padx=20, pady=20)

# First section of input, for volunteer entry
search_firstname_label = tk.Label(search_vol_frame, text="First Name", font=('Arial', 18)) # Creates object in add_vol_frames, gives attributes
search_firstname_label.grid(row = 0, column = 0) # Places object within parent, according to grid 
search_lastname_label = tk.Label(search_vol_frame, text="Last Name", font=('Arial', 18))
search_lastname_label.grid(row = 0, column = 1)
search_gender_label = tk.Label(search_vol_frame, text="Gender", font=('Arial', 18))
search_gender_label.grid(row = 2, column = 1)
search_role_label = tk.Label(search_vol_frame, text="Role", font=('Arial', 18))
search_role_label.grid(row = 2, column = 0)

search_firstname_entry = tk.Entry(search_vol_frame)
search_firstname_entry.grid(row = 1, column = 0)
search_lastname_entry = tk.Entry(search_vol_frame)
search_lastname_entry.grid(row = 1, column = 1)
search_gender_combobox = ttk.Combobox(search_vol_frame, values=["Male", "Female", "Other"])
search_gender_combobox.grid(row = 3, column = 1)
search_role_entry = tk.Entry(search_vol_frame)
search_role_entry.grid(row = 3, column = 0)

for widget in search_vol_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
search_button = tk.Button(search_vol_frame, text = "Search", command = find_vol)
search_button.grid(row = 1, column = 2, sticky = "news", padx = 20, pady = 10)

search_all_button = tk.Button(search_vol_frame, text = "Display All Volunteers", command = display_all)
search_all_button.grid(row = 3, column = 2, sticky = "news", padx = 20, pady = 10)


# Container frame for volunteer entry
add_vol_frame = tk.LabelFrame(frame, text="Add Volunteer to Database")
add_vol_frame.grid(row = 1, column=0, padx=20, pady=20)

# First section of input, for volunteer entry
firstname_label = tk.Label(add_vol_frame, text="First Name*", font=('Arial', 18)) # Creates object in add_vol_frames, gives attributes
firstname_label.grid(row = 0, column = 0) # Places object within parent, according to grid 
lastname_label = tk.Label(add_vol_frame, text="Last Name*", font=('Arial', 18))
lastname_label.grid(row = 0, column = 1)
middleinitial_label = tk.Label(add_vol_frame, text="Middle Initial", font=('Arial', 18))
middleinitial_label.grid(row = 0, column = 2)

firstname_entry = tk.Entry(add_vol_frame)
firstname_entry.grid(row = 1, column = 0)
lastname_entry = tk.Entry(add_vol_frame)
lastname_entry.grid(row = 1, column = 1)
middleinitial_entry = tk.Entry(add_vol_frame)
middleinitial_entry.grid(row = 1, column = 2)

# Second section of input
phone_label = tk.Label(add_vol_frame, text="Phone", font=('Arial', 18))
phone_label.grid(row = 2, column = 0)
email_label = tk.Label(add_vol_frame, text="Email*", font=('Arial', 18))
email_label.grid(row = 2, column = 1)

phone_entry = tk.Entry(add_vol_frame)
phone_entry.grid(row = 3, column = 0)
email_entry = tk.Entry(add_vol_frame)
email_entry.grid(row = 3, column = 1)

gender_label = tk.Label(add_vol_frame, text="Gender*", font=('Arial', 18))
gender_combobox = ttk.Combobox(add_vol_frame, values=["Male", "Female", "Other"]) # Combobox for gender, from ttk not tk
gender_label.grid(row = 2, column = 2)
gender_combobox.grid(row = 3, column = 2)

# Adds padding for each object within add_vol_frame
for widget in add_vol_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

add_vol_button = tk.Button(add_vol_frame, text = "Add Volunteer", command = enter_data)
add_vol_button.grid(row = 4, column = 1, sticky = "news", padx = 20, pady = 10)

#Role Section <-----------------
role_frame = tk.LabelFrame(frame, text="Role Assignemnt and Info")
role_frame.grid(row = 2, column=0, padx=20, pady=20)

rol_firstname_label = tk.Label(role_frame, text="First Name*", font=('Arial', 18)) # Creates object in add_vol_frames, gives attributes
rol_firstname_label.grid(row = 0, column = 0) # Places object within parent, according to grid 
rol_lastname_label = tk.Label(role_frame, text="Last Name*", font=('Arial', 18))
rol_lastname_label.grid(row = 0, column = 1)
rol_role_label = tk.Label(role_frame, text="Role Selection*", font=('Arial', 18))
rol_role_label.grid(row = 0, column = 2)

#Role Section Entries
rol_firstname_entry = tk.Entry(role_frame)
rol_firstname_entry.grid(row = 1, column = 0)
rol_lastname_entry = tk.Entry(role_frame)
rol_lastname_entry.grid(row = 1, column = 1)
rol_role_entry = tk.Entry(role_frame)
rol_role_entry.grid(row = 1, column = 2)

# Adds padding for each object within add_vol_frame
for widget in role_frame.winfo_children():
    widget.grid_configure(padx=13, pady=5)
    
role_button = tk.Button(role_frame, text = "Assign Role", command = assign_role)
role_button.grid(row = 4, column = 1, sticky = "news", padx = 20, pady = 10)

root.mainloop()

#Closes database connection
conn.close()