def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def read_columns(filepath):
    column1 = []
    column2 = []
    with open(filepath, 'r') as file:
        for line in file:
            # Split the line into two numbers based on whitespace
            num1, num2 = map(int, line.split())
            column1.append(num1)
            column2.append(num2)
    return column1, column2