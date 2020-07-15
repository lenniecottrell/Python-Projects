import datetime
from datetime import datetime
import pytz
from pytz import timezone

##def getBranchTime():
##    #this code will find the time for a given branch
##        PDXtz = timezone('America/Los_Angeles')
##        PDXlocaltime = datetime.now(PDXtz)
##        return PDXlocaltime
##        
##        NYCtz = timezone('America/New_York')
##        NYClocaltime = datetime.now(NYCtz)
##        return NYClocaltime
##        
##        Londontz = timezone('Europe/London')
##        Londonlocaltime = datetime.now(Londontz)
##        return Londonlocaltime

def openOrClosed():
    # this code will compare each local time to
    # open and closing times, and print the status of all three branches
    PDXtz = timezone('America/Los_Angeles')
    PDXlocaltime = datetime.now(PDXtz)
    PDXhour = PDXlocaltime.strftime('%H')
    int_PDX = int(PDXhour)
    print(int_PDX)
    
    if int_PDX > 9 and int_PDX < 17:
        print("The PDX branch is open.")
    else:
        print("The PDX branch is closed.")



    NYCtz = timezone('America/New_York')
    NYClocaltime = datetime.now(NYCtz)
    NYChour = NYClocaltime.strftime('%H')
    int_NYC = int(NYChour)
    print(int_NYC)

    if int_NYC > 9 and int_NYC < 17:
        print("The NYC branch is open.")
    else:
        print("The NYC branch is closed.")



    Londontz = timezone('Europe/London')
    Londonlocaltime = datetime.now(Londontz)
    LondonHour = Londonlocaltime.strftime('%H')
    int_London = int(LondonHour)
    print(int_London)

    if int_London > 9 and int_London < 17:
        print("The London branch is open.")
    else:
        print("The London branch is closed.")


if __name__ == "__main__":
    openOrClosed()
