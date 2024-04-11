import sys

input = sys.stdin.readline

h, m = map(int, input().split())

cook = int(input())

m += cook
# print(h, m)
if m > 59:
    h += m // 60
    m %= 60
    # print(h, m)

if h > 23:
    h = h % 24

print(h, m)