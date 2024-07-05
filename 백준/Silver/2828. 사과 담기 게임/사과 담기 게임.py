import sys

input = sys.stdin.readline

# 1. N M 입력
N, M = map(int, input().split())

# 2. J 입력
J = int(input())

# 3. 사과 떨어지는 위치 J번 입력
locations = [int(input()) for _ in range(J)]

# 4. 바구니의 왼쪽 끝, 오른쪽 끝 위치 정의
left, right = 1, M

# 5. 이동 거리 누적할 변수 정의
move = 0

# 6. for 루프로 사과 떨어지는 위치 반복하며 3가지 경우 고려
for location in locations:
    # 7-1. 바구니 왼쪽 끝보다 작을 때
    if location < left:
        move += left - location
        # 위치 갱신
        left = location
        right = location + M - 1

    # 7-2. 바구니 오른쪽 끝보다 클 때
    elif location > right:
        move += location - right
        # 위치 갱신
        left = location - M + 1
        right = location

    # 7-3. 그 사이일 때
    else:
        move += 0

# 8. 원하는 형태로 값 출력
print(move)