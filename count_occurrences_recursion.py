def count_occurrences(integer_list, number):
    """
    Name: count_occurrences
    Input: a list of integers, an item to look for
    Returns: an integer, the number of times the item appears in the list
    """

    count = 0
    for index in range(0, len(integer_list)):
        if integer_list[index] == number:
            count += 1
    return count


def count_occurrences_recursion(lst, item):
    """Function count_occurrences
    Params: list of ints, plus an int to look for
    Returns: the number of items item appears in the list
    Does: recursively counts the occurrences of item
    """

    if len(lst) == 1:
        if lst[0] == item:
            return 1
        return 0
    else:
        if lst[0] == item:
            return 1 + count_occurrences(lst[1:], item)
        else:
            return count_occurrences(lst[1:], item)


def main():
    print(count_occurrences([0], 1))
    print(count_occurrences([0], 0))
    print(count_occurrences([2, 2, 3, 5, -1], 5))
    print(count_occurrences([1, 1, 2], 1))
    print("\n")
    print(count_occurrences_recursion([0], 1))
    print(count_occurrences_recursion([0], 0))
    print(count_occurrences_recursion([2, 2, 3, 5, -1], 5))
    print(count_occurrences_recursion([1, 1, 2], 1))


main()
