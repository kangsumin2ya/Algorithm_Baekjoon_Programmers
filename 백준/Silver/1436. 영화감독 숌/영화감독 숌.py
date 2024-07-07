import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 순서 세기
count = 0

# 666이 있는 숫자만 세기
i = 666

while True:
    str_i = str(i)

    if '666' in str_i:
        count += 1

    if count == N:
        print(i)
        break

    i += 1