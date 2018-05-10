# Write a function that reverses its string argument.


def reverseString(string):

    reversedString = ""

    for letter in reversed(string):
        print(letter)
        reversedString+=str(letter) #Add the letter print out to form a backwards string

    print(reversedString)

    return reversedString



stringToAlter = "BCIT"
print("Welcome")
print("Today we will reverse ", stringToAlter )
print("reversing now...")
reverseString(stringToAlter)

