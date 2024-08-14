import sys

input = sys.stdin.readline

# X(게임 횟수), Y(이긴 게임)
X, Y = map(int, input().split())

# 현재 승률
Z = (Y * 100) // X

# 이분 탐색 위한 초기값 설정
start = 0
end = 1000000000
answer = 0

# 승률이 충분히 크면 바뀌지 않을 것
if Z >= 99:
    answer = -1

else:
    # 이분 탐색 진행
    while start <= end:
        mid = (start + end) // 2
        # 승률 계산
        new_Z = ((Y + mid) * 100) // (X + mid)

        # 승률이 더 커졌다면 정답 갱신 후 더 좁은 범위 탐색
        if new_Z > Z:
            answer = mid
            end = mid - 1

        # 승률이 더 작아졌다면 더 큰 범위 탐색
        else:
            start = mid + 1

# 정답 출력
print(answer)