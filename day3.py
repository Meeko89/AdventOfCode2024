import re

def day3() -> None:
    inputfile = "input/day3.txt"
    # inputfile = "input/day3_example.txt"
    # inputfile = "input/day3_example2.txt"

    result_a = 0
    result_b = 0
    nb_matches = 0
    to_do_or_not_to_do = True
    with open(inputfile, "r") as file:
        for line in file:
            matches = re.findall(r"(do\(\)|don't\(\)|mul\((-?[0-9]{1,3},-?[0-9]{1,3})\))", line)
            for match in matches:
                if match[0] == "do()":
                    to_do_or_not_to_do = True
                elif match[0] == "don't()":
                    to_do_or_not_to_do = False
                else:
                    a, b = match[1].split(",")
                    nb_matches += 1
                    result_a += int(a) * int(b)
                    if to_do_or_not_to_do:
                        result_b += int(a) * int(b)

    # 31635268
    print("Day 3a) result = ", result_a)
    print("Day 3b) result = ", result_b)
