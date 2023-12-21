import sys

input = sys.stdin.readline

N, M = map(int, input().split())

heights = list(map(int, input().split()))

start = 0
end = sum(heights)

while start <= end:
    mid_value = (start + end) // 2
    count = 0

    for h in heights:
        if h > mid_value:
            count += h - mid_value

    if count >= M:
        start = mid_value + 1

    else:
        end = mid_value - 1

print(end)