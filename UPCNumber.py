def is_valid_upc(upc_list):
    """Function is_valid_upc
    :param upc_list: List of integers, a possible UPC number
    :return: Boolean, indicating whether the given input is valid or not
    """
    # Initialize odd_sum
    odd_sum = 0
    # Initialize even_sum
    even_sum = 0
    # If the input is less than 2 digits long, or if all the digits have value 0,
    # the code is ​not valid
    if len(upc_list) < 2:
        return False
    if upc_list.count(0) == len(upc_list):
        return False
    # the number above is written from left to right,
    # but the algorithm goes right to left,
    # so we say 9 is at position 0, 8 is at position 1, etc
    upc_list.reverse()
    # Use a loop to find the UPC number sum result
    upc_list_index = 0
    for i in upc_list:
        # Digits in even positions, including zero: no change
        if upc_list_index % 2 == 0:
            even_sum = even_sum + i
        else:
            # Digits in odd positions: *3
            odd_sum = odd_sum + i * 3

        upc_list_index += 1

    # # Use a loop to find the UPC number sum result
    # for upc_list_index in range(0, len(upc_list)):
    #     if upc_list_index % 2 == 0:
    #         even_sum += upc_list[upc_list_index]
    #     else:
    #         odd_sum += upc_list[upc_list_index] * 3

    # Sum the results
    total_sum = even_sum + odd_sum
    # If it’s a valid UPC number, this result is a multiple of 10
    return total_sum % 10 == 0


def main():
    # The UPC number above is 0 7 3 8 5 4 0 0 8 0 8 9
    upc_list = [0, 7, 3, 8, 5, 4, 0, 0, 8, 0, 8, 9]

    # # User would enter the upc number separated by space
    # str = input("Enter upc number ")
    # # Store the string in the list
    # upc_list = list(str.split(" "))
    # # List of string to list of integer
    # for i in range(0, len(upc_list)):
    #     upc_list[i] = int(upc_list[i])

    # # User would enter the consecutive upc number
    # upc_number = input("Enter upc number ")
    # # Consecutive string to list of integer
    # upc_list = []
    # for i in str(upc_number):
    #     upc_list.append(int(i))
    # # # We would use list comprehension
    # # upc_list = [int(i) for i in str(upc_number)]
    # # # We would use map()
    # # upc_list = list(map(int, str(upc_number)))

    # the number above is written from left to right,
    # but the algorithm goes right to left,
    # so we say 9 is at position 0, 8 is at position 1, etc
    # upc_list.reverse()
    test_input = is_valid_upc(upc_list)
    print(test_input)


main()
