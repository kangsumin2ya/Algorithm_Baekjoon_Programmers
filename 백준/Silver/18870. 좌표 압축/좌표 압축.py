import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 좌표 입력
X = list(map(int, input().split()))

# 중복 제거 후 정렬
sorted_X = sorted(set(X))

# 좌표 압축을 위한 딕셔너리 생성
dict_X = {X: idx for idx, X in enumerate(sorted_X)}

# 좌표 압축
compressed_X = [dict_X[x] for x in X]

# 결과 출력
print(' '.join(map(str, compressed_X)))
