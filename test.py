import sqlite3
from datetime import datetime

conn = sqlite3.connect('Volunteers.db')

cursor = conn.cursor()

def printVolunteerInfo():
    # Define the SQL SELECT statement
    sql = 'SELECT * FROM VolunteerInfo'

    # Execute the SELECT statement
    cursor.execute(sql)

    # Fetch all rows from the cursor
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)
        
printVolunteerInfo()

# Close the cursor and database connection
cursor.close()
