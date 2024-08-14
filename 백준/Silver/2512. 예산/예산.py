import sys

input = sys.stdin.readline

# 1. 지방의 수 N을 입력받는다.
N = int(input())

# 2. 각 지방의 예산들을 리스트로 입력받는다.
budgets = list(map(int, input().split()))

# 3. 총 예산 M을 입력받는다.
M = int(input())

# 4. while문을 통해 이분탐색을 진행한다.
start = 0
end = max(budgets)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total_budgets = 0

    for budget in budgets:
        total_budgets += min(budget, mid)

    if total_budgets > M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1


# 5. 예산 총액을 출력한다.
print(answer)
