#!/usr/bin/python3
for i in range(122, 97 - 1, -1):
    if i % 2 != 0:
        print("{:c}".format(i).upper(), end="")
    else:
        print("{:c}".format(i), end="")
