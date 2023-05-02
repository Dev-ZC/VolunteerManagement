import mysql.connector
from datetime import datetime

db = mysql.connecter.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "volunteerdatabase"
    )

mycursor = db.cursor()

mycursor.execute("CREATE TABLE VolunteerInfo (name varchar(50) NOT NULL, created datetime NOT NULL, phone varchar(20), email varchar(50), gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTOINCREMENT)")

#Make another table for availability