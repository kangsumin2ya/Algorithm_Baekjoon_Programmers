import sys

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. N번 반복해서 1부터 1씩 증가하는 숫자 출력
for i in range(N):
    print(i+1)