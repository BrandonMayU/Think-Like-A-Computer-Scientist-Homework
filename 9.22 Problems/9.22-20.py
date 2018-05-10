# Write a function called remove_dups that takes a string and creates
# a new string by only adding those characters that are not already present.
# In other words, there will never be a duplicate letter added to the new string.

def remove_dups(l):
    newString = ""
    for i in list(set(l)):

        newString+=i
    return newString

print(remove_dups("brandon mayhew"))
print("^^ The text above contains all the letters you need to spell Brandon Mayhew with no duplicates! ^^")