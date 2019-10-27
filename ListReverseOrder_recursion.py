def rev(number_list):
    reverse_list = []
    for index in range(0, len(number_list)):
        reverse_list += [(number_list[(len(number_list) - index - 1)])]
        # reverse_list.append(number_list[(len(number_list) - index - 1)])
    # for index in range((len(number_list) - 1), -1, -1):
    #     reverse_list += [(number_list[index])]
    #     # reverse_list.append(number_list[index])
    return reverse_list


def rev_recursion(number_list):
    if len(number_list) == 0:
        return []
    else:
        return [number_list[-1]] + rev(number_list[:-1])


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    revlist = rev(lst)
    print(lst, 'in reverse is', revlist)
    print(" \n")
    rev_list_recursion = rev_recursion(lst)
    print(lst, 'in reverse is', rev_list_recursion)


main()
