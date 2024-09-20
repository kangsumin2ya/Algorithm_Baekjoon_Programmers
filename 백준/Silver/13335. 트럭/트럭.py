import sys

input = sys.stdin.readline

# n, w, L 입력
n, w, L = map(int, input().split())

# 트럭 무게 입력
trucks = list(map(int, input().split()))

# 다리 리스트 초기화
bridge = [0] * w

# 시간 계산 변수 정의
time = 0

# 트럭 올리는 과정 진행
while bridge:
    # 시간 증가
    time += 1
    # 빈자리 만들기
    bridge.pop(0)

    # 트럭 다 옮길 때까지 진행
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            # 더해서 최대하중 안넘으면 트럭 추가
            bridge.append(trucks.pop(0))
        else:
            # 최대하중 넘으면 다리 위 제거
            bridge.append(0)

# 결과 출력
print(time)