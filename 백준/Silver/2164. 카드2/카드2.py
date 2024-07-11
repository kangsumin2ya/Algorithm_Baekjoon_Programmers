import sys
from collections import deque

input = sys.stdin.readline

# N 입력
N = int(input())

# 카드 번호 큐로 생성
cards = deque(i for i in range(1, N+1))

# 한장 남을 때까지 반복
while len(cards) != 1:
    # 제일 위의 카드 버리기
    cards.popleft()
    # 제일 위의 카드 맨 밑으로 옮기기
    card = cards.popleft()
    cards.append(card)

print(cards[0])