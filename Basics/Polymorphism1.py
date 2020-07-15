#Parent class
class USA():
    
    cap = "Washington D.C."
    motto = "'In God We Trust'"
    
    def capital(self):
        print("{} is the capital of the United States".format(self.cap))

    def motto(self):
        print("The official motto of the USA is {}".format(self.motto))

#child class
class Oregon(USA):
    
    cap = "Salem"
    motto = "Alis Volat Propriis ('She Flies With Her Own Wings')"
    
    def capital(self):
        print("{} is the capital of Oregon".format(self.cap))

    def motto(self):
        print("The official motto of Oregon is {}".format(self.motto))



if __name__ == "__main__":
    country = USA()
    state = Oregon()
    
    country.capital()
    country.motto()
    state.capital()
    state.motto()



    
