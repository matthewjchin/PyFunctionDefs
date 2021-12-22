# ----- LEAPYEAR.PY -----
# Author: Matthew Chin
# GitHub: https://github.com/matthewjchin
#
# This program features the use of functions aside from a main function that
# also takes in user input as the program begins from the main function.
# Mathematical operations in use for this program include modulus, addition,
# division, and subtraction. The functions also allow for user to be returned
# output as a result of the use of functions, to which a return value is
# required in the Python language.
#
# This program checks if a year that the user inputs is a leap year or not.
# A leap year is 366 days, different from the 365 days in a calendar year.
# This is determined if the year inputted is divisible by 4, 100, and 400,
# which is a leap year that starts from the year 0 and on. Therefore, the
# years 2000, 2004, 2008, 2012, and 2016 are leap years, but 1900, 1904,
# and 1908 are not leap years even though the former years listed are even.
# Just because a year is even does not mean that the year is a leap year.
# If an inputted year is NOT divisible by 4, 100, and 400, the year that
# is inputted by the user is NOT a leap year and will return a statement
# of boolean type: True if it is, False if otherwise.
# The modulus operand was used for this program to check divisibility as if
# whether or not there are remainders in each of the statements that the
# argument is checked. If all three statements are met such that each modulus
# equation has a value of 0, it is a leap year

# Function used to determine if a year is a leap year
# Modulus checked to see if there are any remainders
# If remainder exists then it is
# Year must have modulus or remainder value of 0 when
# checked to be divisible by 4, 100, and 400 to return True
# False returned otherwise
def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            if(year%400==0):
                return True
            return False
	return True
    else:
        return False


# Main function created for taking user input
# Calls the isLeapYear function with the year that was user input converted into int type
def main():
	print("You will input a year and will find if it is a leap year. ")
	userYear = int(input("Enter a year with at least one digit: "))
	yearDetd = isLeapYear(userYear)
	print(yearDetd)

	
# Call the main function
main()

