import math

def mySqrt(n):

    initialGuess = n/2

    for i in range(10):
        newGuess = (1/2)*(initialGuess + (n/initialGuess))
        initialGuess = newGuess
        count = i + 1
        print("Guess #", count,": ", newGuess)


    trueSQRT = math.sqrt(n)
    print("True Square root value = ", trueSQRT)


print("Intilizing the function")

value = int(input("Please enter value you want to find the square root of: "))
mySqrt(value) #Execute the function
print()
print("End of Program!")