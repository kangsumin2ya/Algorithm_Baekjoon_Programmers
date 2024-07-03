import sys
from collections import deque

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. 좌석 정보 입력
info = list(str(input().rstrip()))

# 3. 컵홀더 포함한 좌석 정보 입력할 큐 선언
seats = deque()

# 4. 맨 첫번째 컵홀더 추가
seats.append('*')

# 5. 입력받은 좌석 정보를 돌면서 컵홀더 추가
while info:
    seat = info.pop()

    if seat == 'S':
        seats.append(seat)
        seats.append('*')
    elif seat == 'L':
        info.pop()
        seats.append('LL')
        seats.append('*')

# 6. 컵홀더 개수 세기
count = 0

for s in seats:
    if s == '*':
        count += 1

# 7. L이 없는 경우
if count > N:
    print(count - 1)
# 8. L이 있는 경우
else:
    print(count)