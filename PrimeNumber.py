def is_prime(num):
    """ Function is_prime
    Parameters: positive integer
    Returns: boolean, True if prime, and
    False otherwise (it has a factor > 1)
    """
    factor = 2
    while factor <= num / 2:
        if num % factor == 0:
            return False
        factor += 1
    return True


def are_coprime(a, b):
    """ Function are_coprime
    Parameters: two positive integers, a and b
    Returns: boolean, True if a and b are coprime, and
    False otherwise (they have a factor in common)
    """
    factor = 2
    while factor <= a:
        if a % factor == 0 and b % factor == 0:
            return False
        factor += 1
    return True


def main():
    num1 = int(input("Enter an integer\n"))
    num2 = int(input("Enter another integer\n"))
    if is_prime(num1):
        print(num1, "is PRIME TIME!")
    else:
        print(num1, "is just a composite")
    if is_prime(num2):
        print(num2, "is PRIME TIME!")
    else:
        print(num2, "is just a composite")
    if are_coprime(num1, num2):
        print(num1, "and", num2, "are CO PRIME!")
    else:
        print(num1, "and", num2, "are not coprime, they have a factor in common")


main()
