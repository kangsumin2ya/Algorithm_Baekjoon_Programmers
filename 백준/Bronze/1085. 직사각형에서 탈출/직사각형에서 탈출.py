import sys

input = sys.stdin.readline

# 입력
x, y, w, h = map(int, input().split())

# 계산
distance = min(x, y, w-x, h-y)

print(distance)