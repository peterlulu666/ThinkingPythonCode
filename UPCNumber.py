def is_valid_upc(upc_list):
    odd_sum = 0
    even_sum = 0
    for i in upc_list:
        # Digits in even positions, including zero: no change
        if i % 2 == 0:
            even_sum = even_sum + i
        else:
            # Digits in odd positions: *3
            odd_sum = odd_sum + i * 3

    # Sum the results
    return (even_sum + odd_sum) % 10 == 0


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
    upc_list.reverse()
    upc_number = is_valid_upc(upc_list)
    print(upc_number)


main()
