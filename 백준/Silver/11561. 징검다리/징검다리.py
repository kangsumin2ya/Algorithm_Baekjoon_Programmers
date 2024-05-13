import sys

input = sys.stdin.readline

# 1. 테스트 케이스 수 T를 입력받는다.
T = int(input())

# 2. 테스트 케이스마다 징검다리 총 수 N을 입력받는다.
for _ in range(T):
    N = int(input())

    # 3. 필요한 변수 정의한다.
    start = 1
    end = N
    sum_steps = 0

    # 4. 이분탐색을 진행한다.
    while start <= end:
        k = (start + end) // 2
        
        # 5. 조건을 제시한다.
        if k * (k+1) // 2 <= N:
            start = k + 1
            sum_steps = k
        else:
            end = k - 1

    print(sum_steps)