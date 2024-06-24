import sys

input = sys.stdin.readline

# 1. for문으로 height 입력받아 heights에 추가
heights = [int(input().rstrip()) for _ in range(9)]

# 2. heights 정렬
heights.sort()

# 3. 2가지 키를 제거하여 합이 100이 되는지 확인
total_sum = sum(heights)
found = False

for i in range(8):
    for j in range(i + 1, 9):
        if total_sum - heights[i] - heights[j] == 100:
            answer = [heights[k] for k in range(9) if k != i and k != j]
            found = True
            break
    if found:
        break

# 4. 원하는 형식으로 출력
for height in answer:
    print(height)