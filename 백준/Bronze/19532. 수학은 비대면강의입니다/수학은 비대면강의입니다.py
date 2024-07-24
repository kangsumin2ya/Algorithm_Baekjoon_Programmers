import sys

input = sys.stdin.readline

# a, b, c, d, e, f 입력
a, b, c, d, e, f = map(int, input().split())

# 연립방정식을 풀기 위해 크래머 규칙을 사용
D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - c * d

if D != 0:
    x = Dx // D
    y = Dy // D
    print(x, y)
