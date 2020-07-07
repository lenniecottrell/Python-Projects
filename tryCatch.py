try:
    age = input("How old are you?: ")
    ageInt = int(age)
    ageMinus5 = str(ageInt - 5)
    print("Five years ago you were " + ageMinus5 + " years old")
except:
    print("Please enter your age as a number")
finally:
    print("let's play again")
    
