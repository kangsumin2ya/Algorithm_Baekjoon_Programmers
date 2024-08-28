import sys

input = sys.stdin.readline

# 주사위 개수 입력
n = int(input())

# 주사위 숫자 입력
dices = [list(map(int, input().split())) for _ in range(n)]

# 주사위 마주 보는 면 정의
pairs = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

# 갱신할 최댓값 저장할 변수 정의
max_sum = 0

# 첫번째 주사위 놓기
for i in range(6):
    up = dices[0][i]
    down = dices[0][pairs[i]]

    # 현재 합 계산
    current_sum = 0

    # 옆면 중 최댓값 구하기
    current_sum += max([num for idx, num in enumerate(dices[0]) if idx != i and idx != pairs[i]])

    for j in range(1, n):
        # 밑 주사위 숫자 = 위 주사위 숫자
        down_idx = dices[j].index(up)

        down = dices[j][down_idx]
        up = dices[j][pairs[down_idx]]

        # 옆면 중 최댓값 구하기
        current_sum += max([num for idx, num in enumerate(dices[j]) if idx != down_idx and idx != pairs[down_idx]])

    # 최대 합 찾기
    max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)

