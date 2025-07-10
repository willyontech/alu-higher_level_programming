#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []

    count = 0
    try:
        while count < x:
            print(my_list[count], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
