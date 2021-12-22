# ----- HOTDOG.PY -----
# Author: Matthew Chin
# GitHub: https://github.com/matthewjchin
#
# This program features the use of functions aside from a main function that
# also takes in user input as the program begins from the main function.
# Mathematical operations in use for this program include modulus, addition,
# division, and subtraction. The functions also allow for user to be returned
# output as a result of the use of functions, to which a return value is
# required in the Python language.

# Function to find the number of packages of dogs needed for cookout
# Packages of hot dogs come in 10
# Determine how many are needed
def packagesNeeded(numItems, itemsPerPackage):
    if numItems % itemsPerPackage == 0:
        # packsNec will return as a float, in print statement
        # packsNec will return as a string
        packsNec = numItems / itemsPerPackage
        return packsNec
    else:
        # find integer division of packages
        packsNec = numItems // itemsPerPackage
        # add 1 when there are remaining dogs or buns
        packsNec = packsNec + 1
        return packsNec


# From the packages of hot dogs used find how many individual dogs are remainders
# Only if applicable - if otherwise then the value of 0 is returned
def itemsLeftover(numItems, itemsPerPackage):
    remgDogs = numItems % itemsPerPackage
    if remgDogs != 0:
        # subtract the remainder of remgDogs from total number of objects in a package
        remgDogs = itemsPerPackage - remgDogs
        return remgDogs
    else:
        remgDogs = 0
        return remgDogs


# User input taken to find number of hot dogs and number of people attending cookout
# Input all currently string type, converted to int (integer) type after input taken
def main():
    people = int(input("How many people will be at the cookout? "))
    hotDogs = int(input("How many hot dogs will each person be given? "))

    # total number of dogs cooked = people attending * hot dogs given per person
    hotDogs = people * hotDogs

    # number of hot dog packages required
    # hot dog packages in 10 per pack
    # dogsPerPack = 10
    print("There are", str(int(packagesNeeded(hotDogs, 10))), "packages of hot dogs needed.")
    # if no remainder by dividing the function will return and print a float - turn into string

    # number of hot dog buns required
    # hot dog buns in 8 per pack
    # bunsPerPack = 8
    print("There are", str(int(packagesNeeded(hotDogs, 8))), "packages of hot dog buns needed. ")
    # if no remainder by dividing the function will return and print a float - turn into string

    # remaining hot dogs
    # hot dog packages in 10 per pack
    # dogsPerPack = 10
    print("There are", str(itemsLeftover(hotDogs, 10)), "hot dogs remaining.")

    # remaining hot dog buns
    # hot dog buns in 8 per pack
    # bunsPerPack = 8
    print("There are", str(itemsLeftover(hotDogs, 8)), "hot dog buns remaining.")


# Call the main function
main()
