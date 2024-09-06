import sys

input = sys.stdin.readline

# L 입력
L = int(input())

# 문자열 입력
strings = list(map(str, input().rstrip()))

# r, M 정의
r, M = 31, 1234567891

# 정답 변수 정의
answer = 0

for i in range(L):
    # 숫자 변환 후 계산 (아스키코드 이용)
    answer += (ord(strings[i]) - 96) * (r ** i)

# 모두 합해서 M으로 나누기
print(answer % M)
