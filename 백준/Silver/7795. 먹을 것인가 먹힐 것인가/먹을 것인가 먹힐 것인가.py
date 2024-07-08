import sys

input = sys.stdin.readline


# 1. T 입력
T = int(input())

for _ in range(T):
    # 2. N, M 입력
    N, M = map(int, input().split())

    # 3. N개의 A 크기 입력
    A = list(map(int, input().split()))

    # 4. M개의 B 크기 입력
    B = list(map(int, input().split()))

    # 5. 크기 리스트 오름차순 정렬
    A.sort()
    B.sort()

    # 6. 투 포인터
    count = 0
    p2 = 0
    for p1 in range(N):
        while p2 < M and A[p1] > B[p2]:
            p2 += 1
        count += p2

    print(count)