import numpy
from numpy import character


def day6() -> None:
    input_file = "input/day6.txt"
    input_file = "input/day6_example.txt"

    with open(input_file, 'r') as file:
        lines = [[ch for ch in line.strip()] for line in file.readlines()]
        grid = numpy.array(lines)
        grid.reshape(len(lines), len(lines[0]))


