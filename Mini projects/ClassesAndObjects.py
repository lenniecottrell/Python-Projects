

# Parent class
class Organism:
    name = 'unknown'
    species = 'unknown'
    legs = None #none is a special data type, which is nothing
    arms = None
    dna = "Sequence A"
    origin = 'unknown'
    carbon_based = True
    
    #give this class a method - must be indented properly
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

# Child class of Organism
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg


# another class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = 'Sequence B'
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

class Bacterium(Organism):
    name = 'x'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms"
        return msg
    
#instantiate each class object




if __name__ == "__main__":
    human = Human()
    print(human.information()) #we can call the information method on human because it's in the parent class
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())





    
