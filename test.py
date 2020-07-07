
def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1, var2

#try/catch block to check for errors and prevent crashing

def compute():
    go = True
    while go: #these two lines make it a loop until it gets the right input
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False #this turns off the loop
        except ValueError as e: #using an alias for the value error
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except:
            print("\n\nOops, you provided an invalid input. Program will close now")
    print("{} + {} = {}".format(var1, var2, var3))
     

if __name__ == "__main__":
    compute()
