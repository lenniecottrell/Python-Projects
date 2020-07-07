#Python 3.8.3
#
#
#
#
#


def start(nice=0, mean=0, name=""):
    #get user's name
    name = describe_game(name) #the argument passed in will be the return of the describe_game function
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        This function checks if this is a new game or not
        if it is new, get the user's name
        if it is not new, thank the player for
        playing again and continue with the game
    """
    if name !="": #their name will not be blank if they play again, so we acknowledge them and jump to the return
        print("\nThank  you for playing again, {}!".format(name))
    else: #if name is blank, run the below code
        stop = True #check for their name while this is true
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "": #as long as they enter their name, the below will print
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False #now we don't need to check for their name anymore
    return name #after all the printing, the describe_game function returns the entered name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name) #print the current score
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you  \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass in the three variable to the score() below


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    if nice > 2: # if condition is true, call win() function below with the three variables
        win(nice,mean,name)
    if mean > 2: # if condition is true, call lose() function below with the three variables
        lose(nice,mean,name)
    else: # else, call nice_mean() again passing in the current value of the three variables.
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name) #call the again() function below


def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call the again function and pass in our variables to play again
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
            choice = input("\nDo you want to play again? (y/n): \n>>> ").lower()
            if choice == "y":
                stop = False
                reset(nice,mean,name)
            if choice == "n":
                print("\nOh, so sad, sorry to see you go!")
                stop = False
                quit() #built in function that closes the program
            else:
                print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")
            # since stop didn't get turned off, it loops back to the top


def reset(nice,mean,name):
    #reset scores
    nice = 0
    mean = 0
    #The name variable is not reset since this only runs if the same user wants to play again
    start(nice,mean,name)








if __name__ == "__main__":                                                                         
    start()
