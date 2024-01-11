import sys

input = sys.stdin.readline

T = int(input())

A = []

for _ in range(T):
    A.append(list(map(int, input().split())))

for a in A:
    sorted_a = sorted(a, reverse=True)
    print(sorted_a[2])