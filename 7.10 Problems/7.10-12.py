# Use a for statement to print 10 random numbers.
# Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.

import random

count = 1 # This keeps track of how many times the for-loop has looped
print("2")
for i in range(10):

    number = random.randint(25,35)
    print("Loop: ",count," Random Number: ", number)
