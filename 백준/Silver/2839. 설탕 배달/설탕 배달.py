import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 최소 봉지 수 초기화
count = 0

# N을 줄여가며 반복
while N >= 0:
    # N이 5의 배수이면 몫 더해주기
    if N % 5 == 0:
        count += N // 5
        # 정답 출력
        print(count)
        break
    # 나누어 떨어지지 않으므로 총 무게에서 3을 뺀 후 위의 조건문으로 돌아가기
    N -= 3
    count += 1

# N이 0으로 종료되지 않은 경우 실행
else:
    print(-1)