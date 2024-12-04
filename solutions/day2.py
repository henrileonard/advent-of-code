from utils.utils import read_string

def part_one():
    #Read reports as one string and replace newline with X to distinguish reports
    data = read_string('day2.txt')
    report_data = data.split('\n')
    current_report = []
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

if __name__ == '__main__':
    part_one()

