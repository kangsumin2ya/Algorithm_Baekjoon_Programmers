import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lengths = [int(input()) for _ in range(K)]

start = 1
end = max(lengths)

while start <= end:
    mid_value = (start + end) // 2
    count = 0

    for len in lengths:
        count += len // mid_value

    if count >= N:
        start = mid_value + 1
    else:
        end = mid_value - 1

print(end)