import sys

input = sys.stdin.readline

# 정수의 개수 N 입력
N = int(input())

# N개 정수 입력
nums = list(map(int, input().split()))

# 찾으려는 v 입력
v = int(input())

# 리스트에서 v가 있으면 개수 세기
count = 0

for num in nums:
    if num == v:
        count += 1

# 원하는 형식으로 출력
print(count)