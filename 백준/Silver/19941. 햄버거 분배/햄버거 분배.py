import sys

input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 위치 입력
locations = list(input().rstrip())

# 먹은 사람 수 저장
people = 0

# 사람 위치 찾기
for i in range(N):
    if locations[i] == 'P':
        # 햄버거 있는지 탐색
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if locations[j] == 'H':
                locations[j] = 0
                people += 1
                break

# 결과 출력
print(people)