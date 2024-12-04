def read_input(filename):
    column1 = []
    column2 = []
    with open(f'../inputs/{filename}', 'r') as file:
        for line in file:
            # Split the line into two numbers based on whitespace
            num1, num2 = map(int, line.split())
            column1.append(num1)
            column2.append(num2)
    return column1, column2

def read_string(filename):
    with open(f'../inputs/{filename}', 'r') as file:
        data = file.read()
    return data