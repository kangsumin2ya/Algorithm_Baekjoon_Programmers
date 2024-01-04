import sys

input = sys.stdin.readline

values = []

N, K = map(int, input().split())

for _ in range(N):
    values.append(int(input()))

values.sort(reverse=True)

total_count = 0

while K != 0:
    for value in values:
        coin_count = K // value
        total_count += coin_count
        K -= value * coin_count

print(total_count)