def is_valid_upc(upc_list):
    """Function is_valid_upc
    Input: List of integers, a possible UPC number
    Returns: Boolean, indicating whether the given input is valid or not
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
    # Reverse the upc_list
    # upc_list = upc_list[::-1]
    upc_list.reverse()
    # Use a loop to find the UPC number sum result
    upc_list_index = 0
    for element in upc_list:
        # Digits in even positions, including zero: no change
        if upc_list_index % 2 == 0:
            even_sum = even_sum + element
        else:
            # Digits in odd positions: *3
            odd_sum = odd_sum + element * 3
        upc_list_index += 1
    # Sum the results
    total_sum = even_sum + odd_sum

    # # Use a loop to find the UPC number sum result
    # for upc_list_index in range(0, len(upc_list)):
    #     if upc_list_index % 2 == 0:
    #         even_sum += upc_list[upc_list_index]
    #     else:
    #         odd_sum += upc_list[upc_list_index] * 3
    # # Sum the results
    # total_sum = even_sum + odd_sum

    # # Use a loop to find the UPC number sum result
    # even_number_list = []
    # odd_number_list = []
    # # The for loop start at index 0 and the step size is 2. The list slicing syntax is [start:stop:step].
    # for element in upc_list[::2]:
    #     even_number_list.append(element)
    # # The for loop start at index 1 and the step size is 2. The list slicing syntax is [start:stop:step].
    # for element in upc_list[1::2]:
    #     odd_number_list.append(element * 3)
    # # Sum the results
    # total_sum = sum(even_number_list + odd_number_list)

    # # Use a loop to find the UPC number sum result
    # even_number_list = []
    # odd_number_list = []
    # # The for loop start at index 0 and the step size is 2. The list slicing syntax is (start:stop:step).
    # for upc_list_index in range(0, len(upc_list), 2):
    #     even_number_list.append(upc_list[upc_list_index])
    # # The for loop start at index 0 and the step size is 2. The list slicing syntax is (start:stop:step).
    # for upc_list_index in range(1, len(upc_list), 2):
    #     odd_number_list.append((upc_list[upc_list_index]) * 3)
    # # Sum the results
    # total_sum = sum(even_number_list + odd_number_list)

    # If it’s a valid UPC number, this result is a multiple of 10
    return total_sum % 10 == 0


def main():
    # The UPC number above is 0 7 3 8 5 4 0 0 8 0 8 9
    upc_list = [0, 7, 3, 8, 5, 4, 0, 0, 8, 0, 8, 9]

    # # User would enter the upc number separated by space
    # upc_number = input("Enter upc number ")
    # # Store the string in the list
    # upc_list = list(upc_number.split(" "))
    # # # We would store the string in the list like this
    # # # The user would enter pure digit upc number
    # # # Initialize the ipc_list
    # # upc_list = []
    # # # Store string to list of string. The characters in string would be the elements in list of string.
    # # upc_list[:0] = upc_number
    # # List of string to list of integer
    # for i in range(0, len(upc_list)):
    #     upc_list[i] = int(upc_list[i])

    # # User would enter the pure digit upc number
    # upc_number = input("Enter upc number ")
    # # Consecutive list of string to list of integer
    # upc_list = []
    # for i in str(upc_number):
    #     upc_list.append(int(i))
    # # # We would use list comprehension for list of string to list of integer
    # # upc_list = [int(i) for i in str(upc_number)]
    # # # We would use map() for list of string to list of integer
    # # upc_list = list(map(int, str(upc_number)))
    # # # We would use lambda for list of string to list of integer
    # # upc_list = list(map(lambda i: int(i), str(upc_number)))

    test_input = is_valid_upc(upc_list)
    print(test_input)
    # # List of integer to list of string
    # number_list = [3, 6, 9]
    # str_List = list(map(str, number_list))
    # print(str_List)
    # for i in str_List:
    #     str_list_index = str_List.index(i)
    #     print(str_list_index)


main()
