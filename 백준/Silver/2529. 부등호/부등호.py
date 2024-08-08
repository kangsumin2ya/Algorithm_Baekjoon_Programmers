import sys
from itertools import permutations

input = sys.stdin.readline

# 부등호 조건 만족하는지 확인하는 함수
def check_sign(a, b, op):
    if op == '<' and a < b:
        return True
    if op == '>' and a > b:
        return True
    return False

# k 입력
k = int(input())

# A 입력
A = list(input().rstrip().split())

# 0 ~ 9까지의 정수 리스트 만들기
nums = [i for i in range(10)]

# 새로 만든 정수 저장할 리스트 초기화
new_nums = []

# 0 ~ 9 중 k+1개 선택하는 순열 생성
for per in permutations(nums, k+1):
    check = True
    for i in range(len(A)):
        # 부등호 조건 불만족
        if not check_sign(per[i], per[i + 1], A[i]):
            check = False
            break
    # 부등호 조건 만족 시 최댓값, 최솟값 갱신
    if check == True:
        # 한 문자열로 만들기
        n = ''.join(map(str, per))
        new_nums.append(n)

# 만들어진 정수 정렬
new_nums.sort()

# 결과 출력
print(new_nums[-1])
print(new_nums[0])
