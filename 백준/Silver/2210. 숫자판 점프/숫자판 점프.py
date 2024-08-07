import sys
from collections import deque

input = sys.stdin.readline


# bfs 구현
def bfs(start_x, start_y):
    # 큐 초기화
    queue = deque([(start_x, start_y, digits[start_x][start_y])])
    # 큐가 빌 때까지
    while queue:
        x, y, num = queue.popleft()

        if len(num) == 6:
            new_nums.add(num)
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                queue.append((nx, ny, num + digits[nx][ny]))


# 숫자 입력 리스트 초기화
digits = []

# 5번 반복해 digit 입력
for _ in range(5):
    digits.append(list(input().rstrip().split()))

# 이동 방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 만든 숫자 저장할 리스트 초기화
new_nums = set()

# 숫자판 전체 돌면서 BFS 수행
for i in range(5):
    for j in range(5):
        bfs(i, j)

# 결과 출력
print(len(new_nums))
