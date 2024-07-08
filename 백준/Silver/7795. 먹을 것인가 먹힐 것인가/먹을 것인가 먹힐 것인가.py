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

    # 6. 이분 탐색
    count = 0
    for a in A:
        start, end = 0, M-1
        # 6-1. 이분 탐색 종료 조건
        while start <= end:
            mid = (start + end) // 2
            # B[mid]가 a보다 작은 요소를 더 찾기 위해 배열의 오른쪽 검사
            if B[mid] < a:
                start = mid + 1
            # B[mid]가 a보다 작은 요소를 더 찾기 위해 배열의 왼쪽 검사
            else:
                end = mid - 1
        # 최종 start : B에서 a보다 작은 요소의 개수 의미
        count += start

    # 7. 원하는 형식의 결과 출력
    print(count)