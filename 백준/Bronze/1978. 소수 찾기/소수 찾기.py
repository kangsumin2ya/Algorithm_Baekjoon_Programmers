import sys

input =  sys.stdin.readline

# N 입력
N = int(input())

# N개 숫자 입력
nums = list(map(int, input().split()))

# 소수 개수 셀 변수 선언
count = 0

# 소수 찾기
for num in nums:
    c = 0
    for i in range(1, num+1):
        # 나누어 떨어지는 수의 개수 세기
        if num % i == 0:
            c += 1
    # 1과 자기 자신만 있는 수라면 소수
    if c == 2:
        count += 1
        
# 원하는 형식으로 출력
print(count)