import sys
from collections import deque

input = sys.stdin.readline

# N 입력
N = int(input())

# 명령 입력
orders = [list(map(int, input().split())) for _ in range(N)]

# 큐 정의
queue = deque()

# 명령 실행
for order in orders:
    # 덱의 앞에 넣는다
    if order[0] == 1:
        queue.appendleft(order[1])

    # 덱의 뒤에 넣는다
    elif order[0] == 2:
        queue.append(order[1])

    # 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력, 없다면 -1을 대신 출력
    elif order[0] == 3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    # 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력, 없다면 -1을 대신 출력
    elif order[0] == 4:
        if queue:
            print(queue.pop())
        else:
            print(-1)

    # 덱에 들어있는 정수의 개수를 출력
    elif order[0] == 5:
        print(len(queue))

    # 덱이 비어있으면 1, 아니면 0을 출력
    elif order[0] == 6:
        if queue:
            print(0)
        else:
            print(1)

    # 덱에 정수가 있다면 맨 앞의 정수를 출력, 없다면 -1을 대신 출력
    elif order[0] == 7:
        if queue:
            print(queue[0])
        else:
            print(-1)

    # 덱에 정수가 있다면 맨 뒤의 정수를 출력, 없다면 -1을 대신 출력
    elif order[0] == 8:
        if queue:
            print(queue[-1])
        else:
            print(-1)
