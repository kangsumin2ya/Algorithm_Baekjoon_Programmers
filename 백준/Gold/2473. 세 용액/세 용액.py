import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# N개 용액 특성값 입력
values = list(map(int, input().split()))

# 오름차순 정렬
values.sort()

# 결과 저장 리스트 정의
answer = []

# 합 큰 수로 정의
sum = 5000000000

# 투 포인터 구현
for i in range(N - 2):
    # 2개의 용액 지정
    left, right = i + 1, N - 1

    # 투 포인터 구현
    while left < right:
        # 현재 합 계산
        temp = values[i] + values[left] + values[right]

        # 합의 절댓값 비교해 더 작으면 저장
        if abs(temp) < sum:
            # 합 갱신
            sum = abs(temp)
            # 정답 갱신
            answer = [values[i], values[left], values[right]]

        # 탐색 범위 좁히기
        if temp < 0:    # 더 큰 수로 이동
            left += 1
        elif temp > 0:  # 더 작은 수로 이동
            right -= 1
        else:   # 가장 0에 가까운 경우로 바로 종료
            break

# 결과 출력
print(*answer)