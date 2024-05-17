import sys

input =  sys.stdin.readline

# 1. N, M 입력받는다.
N, M = map(int, input().split())

# 2. 보석 개수를 입력받는다.
gems = [int(input().rstrip()) for _ in range(M)]

# 3. 이분탐색을 정의한다.
start = 1
end = max(gems)

# 4. 이분탐색을 수행한다.
while start <= end:
    mid = (start + end) // 2
    students = 0

    for gem in gems:
        if gem % mid == 0:
            students += gem // mid
        else:
            students += gem // mid + 1

    if students > N:
        start = mid + 1

    else:
        end = mid - 1

print(start)