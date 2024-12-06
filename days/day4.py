import re
import numpy as np


def count_xmas(word_search) -> int:
    xmas_pattern = r'(?=(XMAS|SAMX))'
    nb_xmas = 0
    for i in range(2):
        for i in range(len(word_search)):
            line = "".join(word_search[i])
            match = re.findall(xmas_pattern, line)
            nb_xmas += len(match)

        line = "".join(word_search.diagonal(0))
        match = re.findall(xmas_pattern, line)
        nb_xmas += len(match)

        for i in range(1, len(word_search)):
            line = "".join(word_search.diagonal(i))
            match = re.findall(xmas_pattern, line)
            nb_xmas += len(match)

            line = "".join(word_search.diagonal(-i))
            match = re.findall(xmas_pattern, line)
            nb_xmas += len(match)

        word_search = np.rot90(word_search)

    return nb_xmas


def count_cross_mas(word_search) -> int:
    nb_cross_mas = 0
    for row in range(1,len(word_search)-1):
        for col in range(1,len(word_search[row])-1):
            if word_search[row][col] == 'A':
                diag1 = {word_search[row - 1][col - 1], word_search[row + 1][col + 1]}
                diag2 = {word_search[row - 1][col + 1], word_search[row + 1][col - 1]}
                if ({'M', 'S'} == {word_search[row - 1][col - 1], word_search[row + 1][col + 1]} and
                        {'M', 'S'} == {word_search[row - 1][col + 1], word_search[row + 1][col - 1]}):
                        nb_cross_mas += 1
    return nb_cross_mas


def day4() -> None:
    print("Day 4")

    inputfile = "input/day4.txt"
    # inputfile = "input/day4_example.txt"

    with open(inputfile, "r") as file:
        lines =  [[ch for ch in line.strip()] for line in file.readlines()]
        word_search = np.array(lines).reshape(len(lines), len(lines[0]))

    nb_xmas = count_xmas(word_search)
    nb_cross_mas = count_cross_mas(word_search)

    print(f"Day 4a) XMAS is spelled {nb_xmas} times")
    print(f"Day 4b) X-MAS is spelled {nb_cross_mas} times")
