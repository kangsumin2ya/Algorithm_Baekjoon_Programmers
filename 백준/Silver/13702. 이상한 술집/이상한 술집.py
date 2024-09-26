import sys

input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 주전자 용량 입력
pots = [int(input()) for _ in range(N)]

# 이분탐색 범위 지정
start = 1
end = max(pots)

# 결과 저장 변수
answer = 0

# 이분탐색 진행
while start <= end:
    # 중앙값 지정
    mid = (start + end) // 2

    # 나눠줄 수 있는 사람 수 계산
    count = 0
    for pot in pots:
        count += pot // mid

    # 나눠줄 수 있는지 여부 확인
    if count >= K:
        # 가능하니까 저장 후 범위 늘리기
        answer = mid
        start = mid + 1
    else:
        # 불가능하니까 범위 좁히기
        end = mid - 1

# 결과 출력
print(answer)