import sys

input = sys.stdin.readline

grade_sum = 0

for _ in range(5):
    grade = int(input())
    grade_sum += grade

print(grade_sum)