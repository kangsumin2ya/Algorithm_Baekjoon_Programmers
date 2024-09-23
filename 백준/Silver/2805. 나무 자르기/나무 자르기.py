import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 나무 길이 입력
heights = list(map(int, input().split()))

# 이분탐색 범위 지정
start = 0
end = max(heights)

# 이분탐색 수행
while start <= end:
    # 중앙값 정의
    mid = (start + end) // 2
    # 잘린 나무 길이 합 저장 변수 정의
    cut_trees = 0

    # 잘린 나무 길이 계산
    for height in heights:
        # 절단기 높이보다 높은 나무만 자름
        if height > mid:
            cut_trees += height - mid

    # 합이 적어도 M보다 큰지 확인
    if cut_trees >= M:
        # 크면 최댓값 구하기 위해 절단기 높이를 더 높여본다
        start = mid + 1
    # 합이 M보다 작으면 절단기 높이 더 줄인다
    else:
        end = mid - 1

# 결과 출력
print(end)
