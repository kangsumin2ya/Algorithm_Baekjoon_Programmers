import sys

input = sys.stdin.readline

N = input().rstrip()

A = list(map(int, input().split()))

M = input().rstrip()

target_list = list(map(int, input().split()))

hash = {}

for i in A:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in target_list:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')