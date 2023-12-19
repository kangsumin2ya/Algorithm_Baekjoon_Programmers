from sys import stdin
from collections import deque

K = int(stdin.readline())

stack = deque()

for _ in range(K):
    n = int(stdin.readline())

    if n != 0 :
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))