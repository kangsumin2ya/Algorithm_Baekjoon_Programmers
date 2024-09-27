import sys

input = sys.stdin.readline


# 거리 계산
def calculate_distance(direction, distance):
    if direction == 1:
        return distance
    elif direction == 2:
        return 2 * n + m - distance
    elif direction == 3:
        return 2 * (n + m) - distance
    elif direction == 4:
        return n + distance


# 블록 가로, 세로 길이 입력
n, m = map(int, input().split())

# 상점 개수 입력
nums = int(input())

# 상점 위치 입력
locations = [list(map(int, input().split())) for _ in range(nums)]

# 동근 위치 입력
start = list(map(int, input().split()))

# 전체 둘레 계산
total_distance = 2 * (n + m)

# 동근 위치 거리 변환
start_distance = calculate_distance(start[0], start[1])

# 최단 거리 합 저장할 변수 정의
answer = 0

# 각 상점에 대해 거리 계산 후 최솟값 찾기
for location in locations:
    store_distance = calculate_distance(location[0], location[1])

    # 시계방향 거리 계산
    distance1 = abs(start_distance - store_distance)
    # 반시계방향 거리 계산
    distance2 = total_distance - distance1

    # 최단 거리 합 선택
    answer += min(distance1, distance2)

# 결과 출력
print(answer)
