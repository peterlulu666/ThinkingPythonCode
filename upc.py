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

