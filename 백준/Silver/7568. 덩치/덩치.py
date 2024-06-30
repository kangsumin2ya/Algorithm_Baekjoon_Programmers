import sys

input = sys.stdin.readline

# 0. 필요한 변수 정의
rank = []

# 1. `N` 입력
N = int(input())

# 2. N 반복해서 (x, y) 입력
sizes = [list(map(int, input().split())) for _ in range(N)]

# 3. for문으로 N개의 (x, y) 반복
for size in sizes:
    count = 0

    # 4. for문으로 첫번째 for문의 (x, y)와 나머지를 비교
    for rest in sizes:
        # 5. 몸무게, 키가 모두 더 큰 경우를 count
        if size[0] < rest[0] and size[1] < rest[1]:
            count += 1

        else:
            continue

    # 6. count+1한 수를 리스트에 append
    rank.append(count+1)

# 7. 원하는 결과 출력
print(*rank)