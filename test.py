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

#cursor.execute("""ALTER TABLE VolunteerInfo ADD role varchar(50)""")


# Close the cursor and database connection
cursor.close()
