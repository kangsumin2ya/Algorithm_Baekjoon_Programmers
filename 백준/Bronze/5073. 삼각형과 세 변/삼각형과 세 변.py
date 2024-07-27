import sys

input = sys.stdin.readline

while True:
    # a, b, c 입력
    lines = list(map(int, input().split()))

    if lines[0] == lines[1] == lines[2] == 0:
        break

    long_line = max(lines)
    other_lines = sum(lines) - long_line

    if long_line >= other_lines:
        print('Invalid')

    else:
        if lines[0] == lines[1] == lines[2]:
            print('Equilateral')

        elif lines[0] == lines[1] or lines[1] == lines[2] or lines[2] == lines[0]:
            print('Isosceles')

        else:
            print('Scalene')