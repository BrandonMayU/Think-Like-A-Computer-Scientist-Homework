# Now write the function is_odd(n) that returns True when n is odd and False otherwise.


def is_odd(n):
    algo = n%2

    if(algo != 0): # '!=' means does not equal
        print("Number is Odd")
    else:
        print("Number is Even")


print("Find out if your number is odd?")

number = int(input("Please enter a number to find out if it is odd: "))

is_odd(number)



