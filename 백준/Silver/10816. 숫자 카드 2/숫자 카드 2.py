from collections import Counter
import sys

input = sys.stdin.readline

N = input().rstrip()

A = list(map(int, input().split()))

M = input().rstrip()

target_list = list(map(int, input().split()))

count = Counter(A)

for i in range(len(target_list)):
    if target_list[i] in count:
        print(count[target_list[i]], end=' ')
    else:
        print(0, end=' ')