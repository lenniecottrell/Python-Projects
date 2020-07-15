import sqlite3

#this is a tuple of tuples, each small tuple being
# a list of information about a user
peopleValues = (('Ron', 'Obvious',42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))


#with the connection we open, we create a table and insert the above tuples as data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)

    #we select the first and last names of people older than 30, and print them.
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)

    #this does the same as above, but fetches the data one at a time vs all at once.
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break #break out of the loop if the row has no data
        print(row)
