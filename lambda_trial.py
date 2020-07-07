lambdaFunc = lambda a : a * 2
print(lambdaFunc(2))



def minusFive(n):
    return lambda b : b - n

results = minusFive(5)

print(results(10))
