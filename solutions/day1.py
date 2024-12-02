from utils.utils import read_input
from collections import Counter


def part_one():
    left_list, right_list = read_input('day1.txt')
    left_list.sort()  # Sort both lists
    right_list.sort()

    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)  # Calculate absolute difference
    print(f"Total Distance: {total_distance}")

def part_two():
    left_list, right_list = read_input('day1.txt')
    right_list_counts = Counter(right_list)  # Count frequencies in the right list
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_list_counts.get(num, 0)  # Multiply by frequency
    print(f"Similarity Score: {similarity_score}")

if __name__ == '__main__':
    part_one()
    part_two()