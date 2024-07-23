import sys

input = sys.stdin.readline

# 테스트케이스 수
T = int(input())

for _ in range(T):
    # 거스름돈 입력
    C = int(input())

    # 정답 저장
    answer = []

    temp = C

    # 쿼터 개산
    q = temp // 25
    answer.append(q)
    temp %= 25

    # 다임 계산
    d = temp // 10
    answer.append(d)
    temp %= 10

    # 니켈 계산
    n = temp // 5
    answer.append(n)
    temp %= 5

    # 페니 계산
    answer.append(temp)

    print(*answer)