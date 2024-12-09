import re
import time

import numpy
from numpy import character
from selenium.webdriver.common.devtools.v121.debugger import pause


def day6() -> None:
    input_file = "input/day6.txt"
    start_position_row = 80
    start_position_col = 79

    # input_file = "input/day6_example.txt"
    # start_position_col = 4
    # start_position_row = 6


    current_direction = 0
    directions = ['N', 'E', 'S', 'W']

    with open(input_file, 'r') as file:
        lines = [[ch for ch in line.strip()] for line in file.readlines()]
        grid = numpy.matrix(lines)
        grid.reshape(len(lines), len(lines[0]))

    visited_positions_count = 0
    position_row = start_position_row
    position_col = start_position_col
    while True:
        if directions[current_direction] == 'N':
            next_row = position_row - 1
            next_col = position_col - 0
        elif directions[current_direction] == 'S':
            next_row = position_row + 1
            next_col = position_col - 0
        elif directions[current_direction] == 'E':
            next_row = position_row - 0
            next_col = position_col + 1
        elif directions[current_direction] == 'W':
            next_row = position_row - 0
            next_col = position_col - 1

        if position_row > grid.shape[0]-1 or position_row < 0 or position_col > grid.shape[1]-1 or position_col < 0:
            break

        if (-1 < next_row < grid.shape[0]
                and -1 < next_col < grid.shape[1]
                and grid[next_row, next_col] == '#'):
            current_direction = current_direction + 1 if current_direction < 3 else 0
        else:
            if grid[position_row, position_col] != 'X':
                visited_positions_count += 1
                grid[position_row, position_col] = 'X'
            position_row = next_row
            position_col = next_col

    print("Day 6a) Total number of visited positions: {}".format(visited_positions_count))







