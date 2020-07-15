from tkinter import messagebox

#this code will create the website if it doesn't exist
def createSite(self):
    try:
        site = open("summerSale_site.html", "x")
        site.write("<html> \
                    <body> \
                    <p>Stay tuned for our amazing summer sale!</p> \
                    </body> \
                    </html>")
        site.close()
    except:
        messagebox.showinfo("Error: Existing Site","This website already exists. \nPlease add or overwrite the content.")
        return


#this function will overwrite the body contents
def overwriteBody(self):
    overwriteText = self.addBody.get(1.0, 'end')
    site = open("summerSale_site.html", "w")
    site.write("<html> \
                <body> \
                <p>" + overwriteText + "</p> \
                </body> \
                </html>")
    site.close()


#this function will addend info to the website body
def addToBody(self):
    addendText =  self.addBody.get(1.0, 'end')
    site = open("summerSale_site.html", "a")
    site.write("<html> \
                <body> \
                <p>" + addendText + "</p> \
                </body> \
                </html>")
    site.close()

#this closes the program
def endProgram(self):
        self.master.destroy()


if __name__ == "__main__":
    pass
