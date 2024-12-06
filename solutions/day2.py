from utils.utils import read_string

def part_one():
    #Read reports as one string and replace newline with X to distinguish reports
    data = read_string('day2.txt')
    report_data = data.split('\n')
    safe_reports = 0
    reports = [
        [int(x) for x in subset.split() if x.isdigit()]
        for subset in report_data
    ]
    print(reports)
    for report in reports:
        #Check if reported numbers are increasing, decreasing or unsafe
        change = report[1] - report[0]
        if 0 < change < 4:
            increasing = True
        elif -4 < change < 0:
            increasing = False
        else:
            continue
        for i in range(2,len(report)):
            change = report[i] - report[i-1]
            if change < -3 or change > 3 or change == 0:
                break
            if increasing and change < 0:
                break
            if not increasing and change > 0:
                break
            if i == len(report)-1:
                safe_reports += 1
    print(safe_reports)


def part_two():
    data = read_string('day2.txt')
    report_data = data.split('\n')
    safe_reports = 0
    reports = [
        [int(x) for x in subset.split() if x.isdigit()]
        for subset in report_data
    ]

    for report in reports:
        checked = False
        for idx, entry in enumerate(report):
            if checked:
                break
            report_subset = report.copy()
            # Entferne das Element anhand des Index
            del report_subset[idx]
            # Fortfahren mit den restlichen Überprüfungen
            if len(report_subset) < 2:
                continue  # Vermeide Indexfehler bei zu kurzen Listen
            change = report_subset[1] - report_subset[0]
            if 0 < change < 4:
                increasing = True
            elif -4 < change < 0:
                increasing = False
            else:
                continue
            for i in range(2, len(report_subset)):
                change = report_subset[i] - report_subset[i - 1]
                if change < -3 or change > 3 or change == 0:
                    break
                if increasing and change < 0:
                    break
                if not increasing and change > 0:
                    break
                if i == len(report_subset) - 1:
                    safe_reports += 1
                    checked = True
                    break
    print(safe_reports)
         


if __name__ == '__main__':
    part_one()
    part_two()

