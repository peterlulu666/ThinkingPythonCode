def main():
    number = int(input("Enter a number "))
    print("The number contains " + str((len(str(number)))) + " digits. ")
    for i in range(1, (len(str(number))) + 1):
        zeros = (len(str(number)) - i) * "0"
        divisor = int("1" + (len(str(number)) - i) * "0")
        digit = (number // divisor) % 10
        if number < 10:
            digit = number % 10
        print("The 1" + str(zeros) + "th " + "digit is " + str(digit))


main()
