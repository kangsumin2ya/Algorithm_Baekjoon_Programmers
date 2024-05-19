import sys

input = sys.stdin.readline

# 1. N, C를 입력받는다.
N, C = map(int, input().split())

# 2. N번 반복하여 집의 좌표를 입력받아 리스트에 저장한다.
locations = [int(input().rstrip()) for _ in range(N)]

# 2-1. 순서대로 위치하도록 정렬
locations.sort()

# 3. 이분탐색을 정의한다.
start = 1
end = locations[-1] - locations[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    now = locations[0]

    # 3-1. 공유기 개수 세기
    for i in range(1, N):
        if locations[i] >= now + mid:
            count += 1
            now = locations[i]

    if count < C:
        end = mid - 1

    else:
        start = mid + 1
        answer = mid

print(answer)