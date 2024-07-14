import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int,input().split())

# 바구니 리스트
basket = [i for i in range(1, N+1)]

# 바구니 역순 범위 M번 입력
orders = [list(map(int, input().split())) for _ in range(M)]

# 역순 실행
for order in orders:
    # 리스트 슬라이싱해 역순으로 변경
    basket[order[0]-1:order[1]] = basket[order[0]-1:order[1]][::-1]

# 출력
print(*basket)