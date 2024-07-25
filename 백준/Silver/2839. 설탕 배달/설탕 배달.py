import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 최소 봉지 수 초기화
count = -1

# 5kg 봉지 최대 개수부터 하나씩 줄여가며 검사
for i in range(N // 5, -1, -1):
    # 5kg 봉지 사용해 남은 무게 계산
    remain = N - (i * 5)
    # 남은 무게가 3으로 나누어 떨어지는지 확인
    if remain % 3 == 0:
        # 나누어 떨어지면 그 몫을 더해줌
        count = i + (remain // 3)
        # 원하는 값 찾았으니 종료
        break

# 정답 출력
print(count)