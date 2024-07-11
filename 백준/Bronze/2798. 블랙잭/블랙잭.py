import sys
from itertools import combinations

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# N장의 카드 입력
cards = list(map(int,input().split()))

# 정답 저장 변수 선언
ans = 0
differ = 300000

# N개 중 3개 고르는 조합 계산
for com in combinations(cards, 3):
    card_sum = sum(com)
    # M을 넘지 않으면서 M에 가장 가까운 카드의 합 구하기
    if card_sum <= M and abs(card_sum - M) <= differ:
        ans = card_sum
        differ = abs(card_sum - M)

# 원하는 형태로 출력
print(ans)