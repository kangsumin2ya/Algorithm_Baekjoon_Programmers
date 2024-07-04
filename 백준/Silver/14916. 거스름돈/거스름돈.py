import sys

input = sys.stdin.readline

# 1. n을 입력
n = int(input())

# 2. while 루프 작성
count = 0

while True:
    # 3. n이 5의 배수인지 확인
    if n % 5 == 0:
        count += n//5
        break

    # 4. 아닌 경우 2 빼고 count를 1씩 증가
    else:
        n -= 2
        count += 1

    if n < 0:
        break

# 5. 만약 n이 0보다 작으면 종료 후 -1 출력
if n < 0:
    print(-1)
else:
    print(count)