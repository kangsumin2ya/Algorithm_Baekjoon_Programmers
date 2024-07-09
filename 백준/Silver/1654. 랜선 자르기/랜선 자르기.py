import sys

input = sys.stdin.readline

# 1. K, N 입력
K, N = map(int, input().split())

# 2. K번 반복해 길이 입력
lengths = [int(input()) for _ in range(K)]

# 3. 랜선 길이 오름차순 정렬
lengths.sort()

# 4. 이분 탐색 구현
# 4-1. start, end 정의
start = 1
end = lengths[-1]

while start <= end:
    # 4-2. mid 정의
    mid = (start + end) // 2

    # 4-3. 각 길이에 나누어 얻은 몫의 합 계산
    count = 0
    for length in lengths:
        count += length // mid

    # 4-4. 조건문에 따라 start, end 조절
    if count >= N :
        start = mid + 1
    else:
        end = mid - 1

# 5. 원하는 형식으로 출력
print(end)
