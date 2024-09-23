import sys

input = sys.stdin.readline

# 0, 0 입력 될 때까지 반복
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    else:
        # 약수인지 확인
        if b % a == 0:
            print('factor')
        # 배수인지 확인
        elif a % b == 0:
            print('multiple')
        else:
            print('neither')