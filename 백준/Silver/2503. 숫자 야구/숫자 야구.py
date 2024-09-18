import sys
from itertools import permutations

input = sys.stdin.readline

# N 입력
N = int(input())

# 민혁의 숫자, 스트라이크 수, 볼 수 입력
questions = [list(map(int, input().split())) for _ in range(N)]

# 답 개수 변수 정의
count = 0

# 1~9 중 서로 다른 3개 골라 세 자리 수
nums = list(permutations(range(1, 10), 3))

# 답 확인
for num in nums:
    # 정답 가능성 있는지 나타내는 플래그 변수
    valid = True

    for question in questions:
        question_num = list(map(int, str(question[0])))
        answer_strikes, answer_balls = question[1], question[2]

        # 스트라이크 수, 볼 수 초기화
        strikes = balls = 0

        # 계산
        for i in range(3):
            # 같은 자리 같은 숫자
            if num[i] == question_num[i]:
                strikes += 1
            # 다른 자리 같은 숫자
            elif num[i] in question_num:
                balls += 1

        # 유효한지 아닌지 확인
        if answer_strikes != strikes or answer_balls != balls:
            valid = False
            break

    # 모든 조건 만족하면 정답 가능성 있는 답 수 증가
    if valid:
        count += 1

# 결과 출력
print(count)
