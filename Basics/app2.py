

import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    # The following is calling code from within this script
    # the return of the print_app2() function will be put in the curly braces
    # the return should be "__main__"
    print("I am running code from {}".format(print_app2()))

    # The folloing is calling code from the imported app.py
    print("I am running code from {}".format(app.print_app()))    
