import sys

input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 팩토리얼 정의
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

# 이항 계수 계산
answer = factorial(N) // (factorial(N-K) * factorial(K))

# 원하는 형식으로 출력
print(answer)