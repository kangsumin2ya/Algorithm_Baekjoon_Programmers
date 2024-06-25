import sys

input = sys.stdin.readline

# 1. 정수 N 입력받기
N = int(input())

# 2. member를 리스트로 입력받기
members = [list(map(str, input().split())) for _ in range(N)]

# 3. 정렬하기
members.sort(key=lambda x: int(x[0]))

# 4. 원하는 형식으로 출력하기
for member in members:
    print(*member)