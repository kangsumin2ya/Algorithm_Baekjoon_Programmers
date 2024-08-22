import sys

input = sys.stdin.readline

# n 입력
n = int(input())

# H 입력
H = list(map(int, input().split()))

# A 입력
A = list(map(int, input().split()))

# 나무 첫날 길이, 자라는 양 튜플로 묶기
tree = []
for i in range(n):
    tree.append((H[i], A[i]))

# 자라는 양 기준 정렬
tree.sort(key=lambda x: x[1])

# 자른 나무 길이 저장할 변수 정의
cut_tree = 0

# 적게 자라는 나무 길이부터 누적합 계산
for day in range(n):
    h, a = tree[day]
    cut_tree += h + a * day

# 정답 출력
print(cut_tree)
