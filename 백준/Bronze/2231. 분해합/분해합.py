import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 분해합 = 각 자리수 합 + 숫자 / 생성자 = 분해합을 만들어내는 수 / 어떤 자연수는 생성자X or 생성자 많을 수 있음
# N의 가장 작은 생성자 구하기
for i in range(N+1):
    # 숫자 -> 문자열 -> 리스트 -> 각 요소 숫자 변환 ==> 각 요소 합 + 원래 숫자 = 분해합
    num_sum = sum([int(n) for n in list(str(i))]) + i

    # 원하는 생성자 발견
    if num_sum == N:
        print(i)
        break

    # N까지 왔는데 생성자 발견 못한 것은 없는 것
    if i == N:
        print(0)
        break