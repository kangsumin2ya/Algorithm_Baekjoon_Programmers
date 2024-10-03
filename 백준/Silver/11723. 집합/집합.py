import sys

input = sys.stdin.readline

# M 입력
M = int(input())

# S 정의
S = set()

for _ in range(M):
    order = list(input().split())

    if order[0] == 'add':
        S.add(int(order[1]))

    elif order[0] == 'remove':
        S.discard(int(order[1]))

    elif order[0] == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)

    elif order[0] == 'toggle':
        if int(order[1]) in S:
            S.discard(int(order[1]))
        else:
            S.add(int(order[1]))

    elif order[0] == 'all':
        S = set(range(1, 21))

    elif order[0] == 'empty':
        S.clear()