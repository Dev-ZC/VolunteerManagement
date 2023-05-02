import sqlite3
from datetime import datetime
    
conn = sqlite3.connect('Volunteers.db')

c = conn.cursor()


#c.execute("""CREATE TABLE VolunteerInfo (
#                    name varchar(50) NOT NULL, 
#                    created datetime NOT NULL, 
#                    phone varchar(20), 
#                    email varchar(50), 
#                    gender varchar(1) NOT NULL CHECK (gender IN ('M', 'F', 'O')), 
#                    id INTEGER PRIMARY KEY AUTOINCREMENT)""")

print(c.fetchall())

#Make another table for availability