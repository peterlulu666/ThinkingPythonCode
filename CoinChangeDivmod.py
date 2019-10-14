def main():
    # The input from the user is a float number
    # Store the user input in userInput variable
    userInput = float(input("Enter the change amount "))
    # If they enter more than two digits after the decimal place,
    # round to the closest 100th
    # convert dollars to cents
    cents = round(userInput * 100.0)
    dollars, centsLeftOver = divmod(cents, 100)
    quarters, centsLeftOver = divmod(centsLeftOver, 25)
    dimes, centsLeftOver = divmod(centsLeftOver, 10)
    nickels, pennies = divmod(centsLeftOver, 5)
    print(str(dollars) + " dollars ")
    print(str(quarters) + " quarters ")
    print(str(dimes) + " dimes ")
    print(str(nickels) + " nickels ")
    print(str(pennies) + " pennies ")


main()
