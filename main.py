from day3 import *

def day2() -> None:
    reports = []
    safe_reports = []
    safe_reports_with_dampener = []
    with open('input/day2.txt') as file:
        for line in file:
            report_is_unsafe = False
            data = [int(x) for x in line.split(" ")]
            reports.append(data)
            if is_report_safe(data):
                safe_reports.append((-1, data))
            else:
                for i in range(len(data)):
                    reduced_report = data[:i] + data[i+1:]
                    if is_report_safe(reduced_report):
                        safe_reports_with_dampener.append((i, reduced_report))
                        break

    wrong_guesses = [2495, 17, 5]
    print("a) Number of safe reports: " + str(len(safe_reports)))
    # print("a) Answer already guessed: " + str(safe_reports in wrong_guesses))

    print("b) Number of safe reports with problem dampener: " + str(len(safe_reports_with_dampener) + len(safe_reports)))

def is_report_safe(data) -> bool:
    report_is_unsafe = False
    if sorted(data) == data or sorted(data, reverse=True) == data:
        for i in range(1, len(data)):
            diff = abs(data[i] - data[i - 1])
            if diff < 1 or diff > 3:
                report_is_unsafe = True
    else:
        report_is_unsafe = True

    return not report_is_unsafe


if __name__ == '__main__':
    # day2()
    day3()
