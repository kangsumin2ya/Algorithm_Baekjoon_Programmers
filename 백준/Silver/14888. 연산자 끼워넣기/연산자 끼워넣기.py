import sys

input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))
op_num = list(map(int, input().split()))    # +, -, *, / 순서

# 최댓값, 최솟값 초기화
max_result = -1000000000
min_result = 1000000000


# 완전탐색
def dfs(idx, current, plus, minus, mul, div):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, current)
        min_result = min(min_result, current)
        return

    if plus:
        dfs(idx + 1, current + A[idx], plus - 1, minus, mul, div)
    if minus:
        dfs(idx + 1, current - A[idx], plus, minus - 1, mul, div)
    if mul:
        dfs(idx + 1, current * A[idx], plus, minus, mul - 1, div)
    if div:
        # 음수 나눗셈 처리 (C++14 스타일)
        if current < 0:
            dfs(idx + 1, -(-current // A[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // A[idx], plus, minus, mul, div - 1)


# 초기값부터 시작
dfs(1, A[0], op_num[0], op_num[1], op_num[2], op_num[3])

# 출력
print(max_result)
print(min_result)