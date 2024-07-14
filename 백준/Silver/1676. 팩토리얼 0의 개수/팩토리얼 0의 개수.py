import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 팩토리얼 구현
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


# 구한 결과를 문자열로 변환해 0이 아닌 숫자까지 0의 개수 세기
result = list(str(factorial(N)))

count = 0

for i in range(len(result)-1, -1, -1):
    if result[i] == '0':
        count += 1
    else:
        break

# 출력
print(count)