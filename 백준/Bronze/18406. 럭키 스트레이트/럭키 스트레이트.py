import sys

input = sys.stdin.readline

N = str(input().rstrip())

num = int(len(N) / 2)

left_str = list(map(int, N[:num]))

right_str = list(map(int, N[num:]))


left_sum = sum(left_str)

right_sum = sum(right_str)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')