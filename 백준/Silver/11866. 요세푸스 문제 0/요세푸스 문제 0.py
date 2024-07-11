import sys
from collections import deque

input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 사람 번호 저장
people = deque(i for i in range(1, N+1))

# 정답 저장
result = []

while True:
    # 종료 조건
    if len(people) < 1:
        break

    # K번째 사람 빼기
    else:
        for i in range(1, K):
            # K 전까지 사람을 뒤로 옮기기
            people.append(people.popleft())
        # K번째 사람 빼서 정답에 넣기
        result.append(people.popleft())

# 원하는 형식으로 출력
print(str(result).replace('[', '<').replace(']', '>'))