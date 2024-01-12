#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    nw_list = list(a_dictionary.keys())

    nw_list.sort()

    for i in nw_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
