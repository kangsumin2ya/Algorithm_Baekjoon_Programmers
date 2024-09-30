import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 회의 정보 입력
meetings = [list(map(int, input().split())) for _ in range(N)]

# 빨리 끝나는 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의 개수 세는 변수 정의
count = 1

# 비교 위해 끝나는 시간 저장
end = meetings[0][1]

# 끝나는 시간, 시작 시간 비교해서 시작 시간이 나중일 때 회의 선택
for i in range(1, N):
    if meetings[i][0] >= end:
        # 끝나는 시간 갱신
        end = meetings[i][1]
        # 회의 수 세기
        count += 1

# 결과 출력
print(count)