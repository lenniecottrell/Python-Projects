# abc stands for abstract base classes
from abc import ABC, abstractmethod

#this is an abstract class
class Game(ABC):

    #this is NOT an abstract method
    def message(self):
        print("Let's play a game!")
        
    #this is an abstract method - its body is undefined       
    @abstractmethod
    def gameTitle(self):
        pass

#this is a child class
class Poker(Game):
    
    #here is the abstract method from above, but defined in the child class
    def gameTitle(self):
        print("We're going to play Poker")

cardGame = Poker() #instantiate an object from class Poker
cardGame.message() #call the message method from the parent class
cardGame.gameTitle() #call the gameTitle method from the child class



