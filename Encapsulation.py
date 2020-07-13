class Warrior:
    # protected variables with default values
    _style = ""
    _weapon = ""

    # private variable with default value
    __health = 0

    def __init__(self, style, weapon, health):
        self._style = style
        self._weapon = weapon
        self.__health = health

    # protected method
    def _displayStats(self):
        print("Basic Style: ", self._style)
        print("Starting Weapon: ", self._weapon)
        print("Starting Health: ", self.__health)


# instantiate a class object, make sure the function works
newPlayer = Warrior("Fighter", "Nunchaku", 100)
newPlayer._displayStats()

              
              
