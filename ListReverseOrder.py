def rev(number_list):
    reverse_list = []
    for index in range(0, len(number_list)):
        reverse_list.append(number_list[(len(number_list) - index - 1)])
    # for index in range((len(number_list) - 1), -1, -1):
    #     reverse_list.append(number_list[index])
    return reverse_list


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    revlist = rev(lst)
    print(lst, 'in reverse is', revlist)        


main()
