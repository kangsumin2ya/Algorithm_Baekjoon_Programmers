import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# N개의 x, y 입력
locations = [list(map(int, input().split())) for _ in range(N)]

# 기준1:x, 기준2:y로 정렬
locations.sort(key=lambda x: [x[0], x[1]])

# 원하는 형태로 출력
for location in locations:
    print(location[0], location[1])