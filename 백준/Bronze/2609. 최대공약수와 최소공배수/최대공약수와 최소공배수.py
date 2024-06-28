import sys

input = sys.stdin.readline

# 1. a, b 입력받기
a, b = map(int, input().split())

#### 직접 구현 시
# # 2. 최대공약수 구하기
# def gcd(a, b):
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
#
# # 3. 최소공배수 구하기
# def lcm(a, b):
#     for i in range(max(a, b), (a*b)+1):
#         if i % a == 0 and i % b == 0:
#             return i
#
# print(gcd(a, b))
# print(lcm(a, b))

#### math 이용
import math

print(math.gcd(a,b))
print(math.lcm(a,b))