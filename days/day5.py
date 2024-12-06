import copy
from math import floor


def fix_page_ordering(rules: dict[str, str], update_order: list[str]) -> list[str]:
    incorrect_order = True
    new_order = copy.deepcopy(update_order)
    while incorrect_order:
        incorrect_order = False
        update_order = copy.deepcopy(new_order)
        for page_idx in range(len(update_order)):
            if update_order[page_idx] in rules.keys():
                for rule in rules[update_order[page_idx]]:
                    if rule in update_order:
                        rule_idx = update_order.index(rule)
                        if page_idx > rule_idx:
                            incorrect_order = True
                            new_order.remove(update_order[page_idx])
                            new_order.insert(rule_idx,update_order[page_idx])
                            if False:
                                break

    return new_order

def day5() -> None:
    print("Day 5")

    inputfile = "input/day5.txt"
    # inputfile = "input/day5_example.txt"

    rules = {}
    sum_correct_middle_numbers = 0
    sum_fixed_middle_numbers = 0
    with open(inputfile, "r") as file:
        for line in file:
            if line == '\n':
                continue
            if '|' in line:
                first, second = line.strip().split("|")
                if first not in rules.keys():
                    rules[first] = [second]
                else:
                    rules[first].append(second)
            else:
                update_order = line.strip().split(',')

                update_correct = True
                for page in update_order:
                    if page in rules.keys():
                        for page_rule in rules[page]:
                            if (page_rule in update_order
                                    and update_order.index(page) > update_order.index(page_rule)):
                                update_correct = False
                                

                if update_correct:
                    middle_number = update_order[floor(len(update_order) / 2)]
                    sum_correct_middle_numbers += int(middle_number)
                else:
                    new_order = fix_page_ordering(rules, update_order)

                    middle_number = new_order[floor(len(update_order) / 2)]
                    sum_fixed_middle_numbers += int(middle_number)



    print(f"Day 5a) Number of correct updates: {sum_correct_middle_numbers}")
    print(f"Day 5b) Number of fixed updates: {sum_fixed_middle_numbers}")

