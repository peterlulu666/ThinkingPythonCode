import math


def main():
    # The input from the user is a float
    # Store the user input in userInput variable
    userInput = float(input("Enter the change amount\n "))
    # If they enter more than two digits after the decimal place,
    # round to the closest 100th
    amount = round(userInput, 2)
    print("That breaks down to ... ")
    dollars = math.floor(amount)
    print(str(dollars) + " dollars ")
    quarters = int(((amount - dollars) * 100) / 25)
    print(str(quarters) + " quarters ")
    dims = int((((amount - dollars) - quarters * 0.25) * 100) / 10)
    print(str(dims) + " dims ")
    nickels = int((((amount - dollars) - quarters * 0.25 - dims * 0.1) * 100) / 5)
    print(str(nickels) + " nickels ")
    pennies = round(((amount - dollars) - quarters * 0.25 - dims * 0.1 - nickels * 0.05) * 100 / 1)
    print(str(pennies) + " pennies ")


main()
