import sys

input = sys.stdin.readline

# 1. 문자열을 공백 기준으로 구분해 리스트에 입력받기
str_lst = list(map(str, input().split()))

# 2. 리스트 길이 계산해 출력
print(len(str_lst))