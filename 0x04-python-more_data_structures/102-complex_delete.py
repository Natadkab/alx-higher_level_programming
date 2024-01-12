#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for value_d in key_list:
        if value == a_dictionary.get(value_d):
            del a_dictionary[value_d]

    return a_dictionary
