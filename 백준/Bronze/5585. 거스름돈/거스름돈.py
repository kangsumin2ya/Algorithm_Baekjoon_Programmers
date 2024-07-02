import sys

input = sys.stdin.readline

# 1. 동전 리스트 선언
coins = [500, 100, 50, 10, 5, 1]

# 2. price 입력
price = int(input())

# 3. 받아야 할 잔돈 계산
left = 1000 - price

# 4. for문으로 동전 가격을 나누기 반복
count = 0

for coin in coins:
    if left == 0:
        break

    count += left // coin
    left = left % coin

print(count)