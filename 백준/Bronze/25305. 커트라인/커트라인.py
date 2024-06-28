import sys

input = sys.stdin.readline

# 1. N, k 입력
N, k = map(int, input().split())

# 2. N만큼 반복해서 x 입력
x_list = list(map(int, input().split()))

# 4. x 저장한 리스트를 내림차순 정렬
x_list.sort(reverse=True)

# 5. 커트라인 점수 출력
print(x_list[k-1])