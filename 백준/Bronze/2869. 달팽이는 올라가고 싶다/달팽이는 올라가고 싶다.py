import sys
import math

input = sys.stdin.readline

# A : 낮에 올라갈 수 있는 높이
# B : 밤에 미끄러지는 높이
# V : 막대의 높이

# 입력받기
A, B, V = map(int, input().split())

# 방법1) while문은 시간 초과 발생
# day = 0

# while 1:
#     day += 1
#     V -= A
# 
#     if V <= 0:
#         break
#     else:
#         V += B

day = math.ceil((V-B)/(A-B))

print(day)