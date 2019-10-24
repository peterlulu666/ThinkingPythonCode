# def main():
#     number = int(input("Enter a integer \n"))
#     thousands, LeftOver = divmod(number, 1000)
#     hundreds, LeftOver = divmod(LeftOver, 100)
#     tens, LeftOver = divmod(LeftOver, 10)
#     ones, LeftOver = divmod(LeftOver, 1)
#     print(str(thousands) + " thousands ")
#     print(str(hundreds) + " hundreds ")
#     print(str(tens) + " tens ")
#     print(str(ones) + " ones ")
#
#
# main()


def main():
    number = int(input("Enter a integer \n"))
    print("The number contains " + str((len(str(number)))) + " digits. ")
    LeftOver = 0
    for i in range(1, (len(str(number)) + 1)):
        zero = (len(str(number)) - i) * "0"
        divisor = int("1" + zero)
        if i == 1:
            digit, LeftOver = divmod(number, divisor)
        else:
            digit, LeftOver = divmod(LeftOver, divisor)
        print("The 1" + zero + "th " + "digit is " + str(digit))


main()
