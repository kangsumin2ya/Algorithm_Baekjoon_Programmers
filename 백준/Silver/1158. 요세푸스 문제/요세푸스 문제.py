from collections import deque

import sys

input = sys.stdin.readline

stack = deque()
answer = []

n, k = map(int, input().split())

for i in range(n):
    stack.append(i+1)

while stack:

	for _ in range(k-1):
		stack.append(stack.popleft())

	answer.append(stack.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))