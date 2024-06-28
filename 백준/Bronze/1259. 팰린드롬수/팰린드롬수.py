import sys

input = sys.stdin.readline

# 1. 0 나올 때까지 반복
while True:
    num = int(input())

    if num == 0:
        break
    # 2. str로 캐스팅 후 리스트 만들기
    num_origin = list(str(num))
    # 3. 역순 구하기
    num_reverse = list(reversed(num_origin))
    # 4. 같은지 다른지 확인
    if num_origin == num_reverse:
        print('yes')
    else:
        print('no')