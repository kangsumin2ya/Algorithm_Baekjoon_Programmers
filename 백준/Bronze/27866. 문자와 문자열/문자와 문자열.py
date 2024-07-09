import sys

input = sys.stdin.readline

# 1. S, i(인덱스 말고 순서) 입력받기
S = str(input())

i = int(input()) - 1

# 2. S의 i번째 글자 출력
print(S[i])