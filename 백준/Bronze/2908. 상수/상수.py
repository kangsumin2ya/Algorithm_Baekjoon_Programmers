import sys

input = sys.stdin.readline

# a, b 입력
a, b = map(str, input().split())

# 역순 뒤집기
reverse_a = a[::-1]
reverse_b = b[::-1]

# 큰 수 출력
print(max(reverse_a, reverse_b))