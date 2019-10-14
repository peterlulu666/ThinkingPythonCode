def main():
    # number of cents in dollar
    DOLLARS = 100
    # number of cents in quarter
    QUARTERS = 25
    # number of cent in dim
    DIMES = 10
    # number of cent is nickel
    NICKELS = 5
    # The input from the user is a float number
    # store the user input in userInput variable
    userInput = float(input("Enter the change amount "))
    # If they enter more than two digits after the decimal place,
    # round to the closest 100th
    cents = round(userInput * 100.0)
    # We pull out the dollar-sized chunks of cents from the total number of cent
    dollars = cents // DOLLARS
    # We use the modulo to get the number of cents left over after pulling out the dollar-sized chunks
    centsLeftOver = cents % DOLLARS
    # We pull out the quarter-sized chunks
    quarters = centsLeftOver // QUARTERS
    # We use the modulo to get the number of seconds left over after pulling out the quarter-sized chunks
    centsLeftOver = centsLeftOver % QUARTERS
    # We pull out the dim-sized chunks
    dims = centsLeftOver // DIMES
    # We use the modulo to get the number of seconds left over after pulling out the dim-sized chunks
    centsLeftOver = centsLeftOver % DIMES
    # We pull out the nickel-sized chunks
    nickels = centsLeftOver // NICKELS
    # We use the modulo to get the number of seconds left over after pulling out the nickel-sized chunks
    centsLeftOver = centsLeftOver % NICKELS
    print(str(dollars) + " dollars ")
    print(str(quarters) + " quarters ")
    print(str(dims) + " dims ")
    print(str(nickels) + " nickels ")
    print(str(centsLeftOver) + " cents ")


main()
