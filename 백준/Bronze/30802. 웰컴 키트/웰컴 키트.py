import sys

input = sys.stdin.readline

# 참가자의 수 입력
N = int(input())

# 티셔츠 사이즈별 신청자의 수 입력
people = list(map(int, input().split()))

# 티셔츠와 펜의 묶음 수 입력
T, P = map(int, input().split())

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 계산 후 출력
shirt = 0
for person in people:
    if person % T == 0:
        shirt += person // T
    else:
        shirt += person // T + 1
print(shirt)

# 펜을 P자루씩 최대 몇묶음 주문할 수 있는지, 펜 한 자루씩 몇 개 주문하는지 출력
pens = N // P
pen = N % P
print(pens, pen)