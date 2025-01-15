import sys

input = sys.stdin.readline


# 지나갈 수 있는 길인지 확인하는 함수 구현
def check_road(road):
    # 경사로 설치 여부 저장한 리스트 정의
    slope = [False] * N  # 길이 N만큼 초기화

    # 해당 줄 확인
    for i in range(N - 1):
        # 다음 칸과 높이 같은지 확인
        if road[i] == road[i + 1]:
            continue

        # 높이 차이 확인
        if abs(road[i] - road[i + 1]) > 1:
            return False

        # 낮은 곳 -> 높은 곳 경사로
        if road[i] < road[i + 1]:
            for j in range(L):
                # 범위 내인지 확인
                if i - j < 0 or slope[i - j] or road[i - j] != road[i]:
                    return False
                slope[i - j] = True  # 경사로 설치

        # 높은 곳 -> 낮은 곳 경사로
        elif road[i] > road[i + 1]:
            for j in range(L):
                # 범위 내인지 확인
                if i + 1 + j >= N or slope[i + 1 + j] or road[i + 1 + j] != road[i + 1]:
                    return False
                slope[i + 1 + j] = True  # 경사로 설치

    return True


# N, L 입력
N, L = map(int, input().split())

# 지도 입력
map_info = [list(map(int, input().split())) for _ in range(N)]

# 지나갈 수 있는 길의 개수
answer = 0

# 가로 방향 확인
for row in map_info:
    if check_road(row):
        answer += 1

# 세로 방향 확인
for col in zip(*map_info):
    if check_road(col):
        answer += 1

# 결과 출력
print(answer)
