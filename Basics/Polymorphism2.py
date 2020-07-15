#Parent class
class USA():
    hemisphere = "North"
    govt = "Constitutional Republic"
    
    def capital(self):
        cap = "Washington D.C."
        print("{} is the capital of the United States".format(cap))

    def motto(self):
        motto = "'In God We Trust'"
        print("The official motto of the USA is {}".format(motto))

#child class
class Oregon(USA):
    pop = 4,300,000
    totalArea = 98,466

    def capital(self):
        cap = "Salem"
        print("{} is the capital of Oregon".format(cap))

    def motto(self):
        motto = "Alis Volat Propriis ('She Flies With Her Own Wings')"
        print("The official motto of Oregon is {}".format(motto))

#child class
class California(USA):
    pop = 41,000,000
    totalArea = 163,696

    def capital(self):
        cap = "Sacramento"
        print("{} is the capital of California".format(cap))

    def motto(self):
        motto = "Eureka"
        print("The official motto of California is {}".format(motto))

if __name__ == "__main__":
    country = USA()
    stateOR = Oregon()
    stateCA = California()
    
    country.capital()
    country.motto()
    stateOR.capital()
    stateOR.motto()
    stateCA.capital()
    stateCA.motto()



    
