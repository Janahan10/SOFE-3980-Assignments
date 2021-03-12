#!/usr/bin/python

import sys


def parse(statement, cur_line):
    if statement in cur_line:
        return True

    return False


file = open("Source.txt", "r")
line_number = 1

for line in file:
    if parse(sys.argv[1], line):
        print('line ', line_number, ':', line.strip())

    line_number += 1

file.close()

