import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 바퀴 수
count = 1

# 해당 위치의 숫자
num = 1

while N > num:
    num += 6 * count
    count += 1

# 결과 출력
print(count)
