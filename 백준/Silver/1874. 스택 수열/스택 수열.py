import sys

input = sys.stdin.readline

# n 입력
n = int(input())

# 원하는 수열 입력
num_array = [int(input()) for _ in range(n)]

# 스택과 연산 기록
stack = []
result = []

# 현재 스택에 push할 숫자
current_num = 1

# 수열을 순서대로 확인
for num in num_array:
    # num에 도달할 때까지 push
    while current_num <= num:
        stack.append(current_num)
        result.append('+')
        current_num += 1

    # 스택의 top이 num과 같으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        # num을 만들 수 없는 경우
        print("NO")
        exit()

# 결과 출력
print('\n'.join(result))