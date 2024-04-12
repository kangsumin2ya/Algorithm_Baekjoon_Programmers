import sys

input = sys.stdin.readline

X = int(input())

Y = int(input())

list_price = []

for _ in range(Y):

    info = list(map(int, input().split()))

    list_price.append(info)

sum = 0

for i in range(len(list_price)):
    sum += list_price[i][0] * list_price[i][1]

if sum == X:
    print('Yes')
else:
    print('No')