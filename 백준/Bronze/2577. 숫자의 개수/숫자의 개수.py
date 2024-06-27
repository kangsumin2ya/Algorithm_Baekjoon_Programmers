import sys

input = sys.stdin.readline

# 1. A, B, C 입력 받기
A = int(input())
B = int(input())
C = int(input())

# 2. A * B * C 계산 후 문자열로 변환해 리스트 저장
mul = list(str(A * B * C))

# 3. 0부터 9까지 있는 리스트를 돌면서 문자열에 해당 숫자가 있으면 개수 계산
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    cnt = 0
    
    for n in mul:
        if int(n) == num:
            cnt += 1
            
    print(cnt)