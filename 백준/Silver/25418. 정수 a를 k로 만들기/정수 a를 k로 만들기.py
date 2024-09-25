import sys

input = sys.stdin.readline

# A, K 입력
A, K = map(int, input().split())

# 연산 횟수 변수 정의
count = 0

while True:
    # K가 A가 될 때까지 연산 반복
    if K == A:
        break

    else:
        # 짝수면 2 나누기 (반드시 K를 A로 만들 수 있도록 조건 추가) 
        if K % 2 == 0 and K // 2 >= A:
            K //= 2
            # 연산 횟수 세기
            count += 1

        # 홀수이면 1 빼기
        else:
            K -= 1
            # 연산 횟수 세기
            count += 1

# 결과 출력
print(count)
