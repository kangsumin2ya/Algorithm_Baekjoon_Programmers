import sys

input = sys.stdin.readline

students = []

n = int(input())

for _ in range(n):
    name, day, month, year = input().rstrip().split()
    day, month, year = map(int, (day, month, year))
    students.append((year, month, day, name))

students.sort()

print(students[-1][3])
print(students[0][3])