import sys

input = sys.stdin.readline

# N, A, B 입력
N, A, B = map(int, input().split())

# A개 이쁨 저장
A_beauty = list(map(int, input().split()))

# B개 이쁨 저장
B_beauty = list(map(int, input().split()))

# 오름차순 정렬
A_beauty.sort()
B_beauty.sort()

# 총 예쁨 합 저장할 변수 정의
beauty_sum = 0

# 채워야할 공간 정의
space = N

if space % 2 == 1:
    if A_beauty:  
        beauty_sum += A_beauty.pop()
        space -= 1

# 남은 공간 없을 때까지 채우기
while space > 0:
    if len(A_beauty) < 2 and len(B_beauty) == 0:
        break  
    
    if len(B_beauty) > 0 and (len(A_beauty) < 2 or B_beauty[-1] > A_beauty[-1] + (A_beauty[-2] if len(A_beauty) > 1 else 0)):
        beauty_sum += B_beauty.pop()
    else:
        if len(A_beauty) >= 2:
            beauty_sum += A_beauty.pop() + A_beauty.pop()
        elif len(A_beauty) == 1:
            beauty_sum += A_beauty.pop()

    space -= 2

# 결과 출력
print(beauty_sum)
