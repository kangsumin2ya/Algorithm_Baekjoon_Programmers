import sys

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. dp 테이블 초기화
D = [0] * 1000001

# 3. dp 테이블 초기값 고려
D[1] = 0

# 4. dp 테이블 채우기
for i in range(2, N+1):
    # 4-1. 1 빼주는 연산
    D[i] = D[i-1] + 1

    # 4-2. 2로 나누어 떨어지는지 고려
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)

    # 4-3. 3으로 나누어 떨어지는지 고려
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)

# 5. 원하는 형식으로 출력
print(D[N])