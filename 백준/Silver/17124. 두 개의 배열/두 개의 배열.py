import sys

input = sys.stdin.readline


def binary_search(target, B):
    # 해당 요소와 가까운 B의 요소 찾기 위해 이분 탐색 수행
    start, end = 0, m - 1

    while start <= end:
        mid = (start + end) // 2
        # 같으면 바로 반환
        if target == B[mid]:
            return B[mid]
        elif target > B[mid]:
            start = mid + 1
        else:
            end = mid - 1

    # start가 B의 크기보다 클 때
    if start >= m:
        return B[end]

    # end가 0보다 작을 때
    elif end < 0:
        return B[start]

    else:
        if abs(B[start] - target) < abs(B[end] - target):
            return B[start]
        else:
            return B[end]


# 1. 테스트 케이스 T 입력
T = int(input())

for _ in range(T):
    # 2. n, m 입력
    n, m = map(int, input().split())

    # 3. 배열 A 입력
    A = list(map(int, input().split()))

    # 4. 배열 B 입력
    B = list(map(int, input().split()))

    # 4-1. 배열 B 오름차순 정렬
    B.sort()

    # 5. 배열 C 리스트 초기화
    C = []

    # 6. for문으로 A의 각 요소 접근해 이분 탐색
    for i in range(n):
        closest = binary_search(A[i], B)
        # 6-1. 배열 C에 추가
        C.append(closest)

    # 7. C 리스트 합 출력
    print(sum(C))
