import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# x, y 입력
locations = []

for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x,y))

# 정렬 (y 오름차순 후 x 오름차순)
locations.sort(key=lambda x: (x[1], x[0]))

# 출력
for loc in locations:
    print(*loc)