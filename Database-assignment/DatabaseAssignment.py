

import sqlite3 #Import the sqlite3 module


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# iterate through fileList and find the files that end with .txt
# and add them to the new list txtFiles
txtFiles = []
for file in fileList:
    if file.endswith(".txt"):
        txtFiles.append(file)


        
conn = sqlite3.connect('DBassignment.db') #create a new database and connect to it


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files VARCHAR(50) \
        )")
    conn.commit()
    def addItemsFromList():
        for item in txtFiles:
            cur.execute("INSERT INTO tbl_fileList (col_files) VALUES (?)", [item])
        conn.commit()
        
    addItemsFromList()
    
    cur.execute('SELECT col_files from tbl_fileList')
    varFiles = cur.fetchall()
    for i in varFiles:
        msg = "Here are the requested files: {}".format(i)
        print(msg)
        
conn.close()




##if __name__ = "__main__":
##    connectDB()
