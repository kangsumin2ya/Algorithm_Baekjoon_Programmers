import sys

N = int(input())

info = input().rstrip()

count = info.count('LL')

if count <= 1 :
	print(N)
else:
	print(N - count + 1)