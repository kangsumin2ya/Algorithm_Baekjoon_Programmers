import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# N번 반복해 T 입력
T = [int(input()) for _ in range(N)]

# 이분 탐색 초기값 정의
start = 1
end = max(T) * M

# 정답을 최댓값으로 초기화
answer = end

# 이분 탐색 구현
while start <= end:
    mid = (start + end) // 2
    # 심사한 사람 누적합 저장 변수
    count = 0

    # 각 시간에 대한 사람 수 누적합 계산
    for t in T:
        count += mid // t

    # 처리 가능한 사람 수가 M보다 작으면 시간을 늘려야 한다
    if count < M:
        start = mid + 1

    # 처리 가능한 사람 수가 M보다 크면 정답을 갱신하고 시간을 줄여본다
    else:
        answer = mid
        end = mid - 1

# 정답 출력
print(answer)
