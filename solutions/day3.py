import re

from utils.utils import read_string


def part_one():
    calculation = read_string("day3.txt")
    print(calculation)
    multiplications = re.findall("mul[(]\d+,\d+[)]", calculation)
    mul_sum = 0
    for entry in multiplications:
        first, second = entry.split(",")
        first = first[4:]
        second = second[:-1]
        mul_sum += int(first) * int(second)
    print(mul_sum)







def part_two():
    print("implement me pls")






if __name__ == '__main__':
    part_one()
    part_two()
