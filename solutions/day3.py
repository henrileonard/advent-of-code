import re


from utils.utils import read_string


def part_one():
    calculation = read_string("day3.txt")
    multiplications = re.findall("mul[(]\d+,\d+[)]", calculation)
    mul_sum = 0
    for entry in multiplications:
        first, second = entry.split(",")
        first = first[4:]
        second = second[:-1]
        mul_sum += int(first) * int(second)
    print(mul_sum)







def part_two():
    calculation = read_string("day3.txt")
    multiplications = re.findall("mul[(]\d+,\d+[)]|do(?:n't)?[(][)]", calculation)
    print(multiplications)
    mul_sum = 0
    enable = True
    for entry in multiplications:
        if entry == "don't()":
            enable = False
        elif entry == "do()":
            enable = True
        elif enable:
            first, second = entry.split(",")
            first = first[4:]
            second = second[:-1]
            mul_sum += int(first) * int(second)
    print(mul_sum)







if __name__ == '__main__':
    part_one()
    part_two()
