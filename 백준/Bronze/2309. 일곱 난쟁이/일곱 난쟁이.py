import sys
from itertools import combinations

input = sys.stdin.readline

# 1. for문으로 height 입력받아 heights에 추가
heights = [int(input().rstrip()) for _ in range(9)]

# 2. heights 정렬
heights.sort()

answer = [0] * 9

# 3. 9개 중 7개를 선택하는 조합 계산
for i in combinations(heights, 7):
    if sum(i) == 100:
        answer = i
        break

# 4. 원하는 형식으로 출력
for i in range(len(answer)):
    print(answer[i])