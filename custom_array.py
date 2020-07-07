streets = ["Hawthorne", "Columbia", "Main", "Division", "Mississippi"]

x = streets.count("Main")
print(x)

#This will print out each value in it's current index 
for i in streets:
    print(i)

#This will print out the entire array, but in alphabetical order (re-ordering the index numbers)
streets.sort()
print(streets)
