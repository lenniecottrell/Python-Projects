class Platform:
    def __init__(self, operatingsys, server, database, language):
        self.operatingsys = operatingsys
        self.server = server
        self.database = database
        self.language = language

    def describeClass(self):
        msg = "\nThis is our stack...\n\tOS: {}\n\tServer: {}\n\tDatabase: {}\n\tLanguage: {}.".format(self.operatingsys, self.server, self.database, self.language)
        return msg

#child class
class Battlestation(Platform):
    def __init__(keyboard):
        keyboard = keyboard
        operatingsys = "Windows"
        server = "Apache"
        database = "MySQL"
        language = "Python"
        super().__init__(operatingsys, server, database, language)

    def addStuff(self):
        msg = "My battlestation also has a {} keyboard".format(self.keyboard)
        return msg


if __name__ == "__main__":
    LampStack = Platform("Linux", "Apache", "MySQL", "PHP")
    print(LampStack.describeClass())
    myBattle = Battlestation()
    print(myBattle.describeClass())
    print(myBattle.addStuff())

