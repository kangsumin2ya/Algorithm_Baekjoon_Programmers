import sys
input = sys.stdin.readline

numN, sumN = map(int, input().split())

nums = list(map(int, input().split()))

interval_sum = [0]
temp = 0

for i in nums:
    temp += i
    interval_sum.append(temp)

for i in range(sumN):
    start, end = map(int, input().split())
    print(interval_sum[end] - interval_sum[start-1])