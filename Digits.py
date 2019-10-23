def main():
    number = int(input("Enter a integer \n"))
    # number // 1000 is the 1000-units
    # if the number was greater than 10000,
    # we would use % 10 to find leftover
    thousands = (number // 1000) % 10
    print("hundreds = ", thousands)

    # number // 100 is the 100-units
    # if the number was greater than 1000,
    # we would use % 10 to find leftover
    hundreds = (number // 100) % 10
    print("hundreds = ", hundreds)

    # number // 10 is the 10-units
    # if the number was greater than 100,
    # we would use % 10 to find leftover
    tens = (number // 10) % 10
    print("tens = ", tens)

    # we use % 10 to find the ones digits
    ones = number % 10
    print("ones = ", ones)


main()
