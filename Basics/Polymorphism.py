#Parent class
class USA():
    def capital(self):
        cap = "Washington D.C."
        print("{} is the capital of the United States".format(cap))

    def motto(self):
        motto = "'In God We Trust'"
        print("The official motto of the USA is {}".format(motto))

#child class
class Oregon(USA):
    def capital(self):
        cap = "Salem"
        print("{} is the capital of Oregon".format(cap))

    def motto(self):
        motto = "Alis Volat Propriis ('She Flies With Her Own Wings')"
        print("The official motto of Oregon is {}".format(motto))



if __name__ == "__main__":
    country = USA()
    state = Oregon()
    country.capital()
    country.motto()
    state.capital()
    state.motto()



    
