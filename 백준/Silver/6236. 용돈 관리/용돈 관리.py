import sys

input = sys.stdin.readline

# 1. N, M을 입력받는다.
N, M = map(int, input().split())

# 2. 변수를 정의한다.
K = 0               # 정답

# 3. N번 반복하여 매일 인출해야 할 금액을 입력받는다.
daily_money = [int(input().rstrip()) for _ in range(N)]

# 4. start, end를 정의한다.
start = max(daily_money)
end = sum(daily_money)

# 5. 이분 탐색을 진행한다.
while start <= end:
    mid = (start + end) // 2
    total = 0   # 현재까지의 인출 금액
    times = 1   # 인출 횟수

    for money in daily_money:
        # 인출 금액보다 커서 추가적인 인출이 필요한 경우
        if total + money > mid:
            times += 1
            # 인출 한번 더 해서 인출된 금액이 0
            total = 0
        total += money

    if times > M:
        start = mid + 1
    else:
        end = mid - 1
        K = mid

print(K)