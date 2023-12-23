import sys

input = sys.stdin.readline

answer = []

N = int(input())

n_list = set(map(int, input().split()))

M = int(input())

target_list = list(map(int, input().split()))

for target in target_list:
    answer.append(1) if target in n_list else answer.append(0)

print(((str(answer).replace('[', '')).replace(']', '')).replace(',',''))