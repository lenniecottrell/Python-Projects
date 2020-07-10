

class Boss:
    def __init__(self, name, health, stamina, weapon):
        self.name = name
        self.health = int(health)
        self.stamina = int(stamina)
        self.weapon = weapon

    def encounterMsg(self):
        msg = "You have encountered {}!".format(self.name)
        return msg

    def catchPhrase(self):
        msg = "The boss says:\n\t 'I will slay you with my {}!'".format(self.weapon)
        return msg

    def bossStats(self):
        stats = "Boss stats:\n\tHealth: {}\n\tStamina: {}".format(self.health, self.stamina)
        return stats

#child class
class MiniBoss(Boss):
    def __init__(self, name, health, stamina, weapon, weakness):
        Boss.__init__(self, name, health, stamina, weapon)
        self.weakness = weakness

    def miniBossSays(self):
        msg = "NYAHHH I WILL END YOU! BUT DON'T YOU DARE HIT ME IN MY " + self.weakness + "!"
        return msg


if __name__ == "__main__":
    miniGanon = MiniBoss("miniGanon", 250, 175, "Baby Sword", "soft tummy")
    print(miniGanon.encounterMsg())
    print(miniGanon.bossStats())
    print(miniGanon.catchPhrase())
    print(miniGanon.miniBossSays())
    
    ganon = Boss("Ganon", 500, 400, "Giant Sword")
    print(ganon.encounterMsg())
    print(ganon.catchPhrase())
    print(ganon.bossStats())
    
    
