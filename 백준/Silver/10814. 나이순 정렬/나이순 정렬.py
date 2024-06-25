import sys

input = sys.stdin.readline

# 1. 정수 N 입력받기
N = int(input())

# 2. N만큼 반복하여 회원 이름, 나이를 인덱스와 함께 딕셔너리로 입력받기
member_dict = {}

for idx in range(N):
    member_dict[idx] = list(input().split())

# 3. 2가지 기준으로 sort()로 정렬
sorted_member_dict = dict(sorted(member_dict.items(), key=lambda x: (int(x[1][0]), x[0])))

# 4. 원하는 형식으로 출력
for value in sorted_member_dict.values():
    print(f'{value[0]} {value[1]}')