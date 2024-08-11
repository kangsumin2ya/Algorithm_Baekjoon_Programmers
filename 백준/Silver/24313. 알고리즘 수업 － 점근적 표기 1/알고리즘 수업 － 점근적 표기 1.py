import sys

input = sys.stdin.readline

# 입력1
a1, a0 = map(int, input().split())  # -> f(n) = a_1 * n + a_0

# 입력2
c = int(input())

# 입력3
n0 = int(input())

# O(n) 정의를 만족하는지 검사
if a1 <= c and a1 * n0 + a0 <= c * n0:
    print(1)
else:
    print(0)