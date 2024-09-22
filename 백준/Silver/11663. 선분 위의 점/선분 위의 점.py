# import sys
#
# input = sys.stdin.readline
#
# # 시작점과 가까운 점 찾기
# def find_start(locations, target):
#     # 이분탐색 시작, 끝 초기화
#     start, end = 0, N
#     while start <= end:
#         mid = (start + end) // 2
#         if locations[mid] < target:
#             start = mid + 1
#         else:
#             end = mid
#
#     return start
#
#
#
#
#
# # N, M 입력
# N, M = map(int, input().split())
#
# # N개 좌표 입력
# locations = list(map(int, input().split()))
#
# # M개 선분의 시작점 끝점 입력
# lines = [list(map(int, input().split())) for _ in range(M)]
#
# # 좌표 정렬
# locations.sort()

import sys

input = sys.stdin.readline


# 시작점과 가까운 점을 찾기
def find_start(locations, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if locations[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


# 끝점과 가까운 점을 찾기
def find_end(locations, target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if locations[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start


# N, M 입력
N, M = map(int, input().split())

# N개의 좌표 입력
locations = list(map(int, input().split()))

# M개의 선분의 시작점 끝점 입력
lines = [list(map(int, input().split())) for _ in range(M)]

# 좌표 정렬
locations.sort()

# 각 선분에 대해 계산
for line in lines:
    start, end = line
    start_idx = find_start(locations, start)
    end_idx = find_end(locations, end)

    # 결과 출력
    print(end_idx - start_idx)

