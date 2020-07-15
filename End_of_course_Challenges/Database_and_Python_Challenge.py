import sqlite3
from sqlite3 import *

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))

with sqlite3.connect(':memory:') as connection:
    conn = connection.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ TEXT)")
    conn.executemany("INSERT INTO Roster VALUES (?,?,?)", rosterValues)

    connection.commit()

##    conn.execute("SELECT * FROM Roster")
##    for row in conn.fetchall():
##        print(row)

    conn.execute("UPDATE Roster SET Species=? WHERE Name=?", ('Human', 'Korben Dallas'))

##    conn.execute("SELECT * FROM Roster")
##    for row in conn.fetchall():
##        print(row)

    conn.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    while True:
        row = conn.fetchone()
        if row is None:
            break
        print(row)

              
