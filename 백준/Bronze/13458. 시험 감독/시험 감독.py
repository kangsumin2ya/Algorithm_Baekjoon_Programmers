import sys

input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 감독관 최소 수 초기화
min_ob = 0

# 시험장마다 필요 감독관 수 계산
for a in A:
    # 총감독관만으로도 감시 가능
    if a <= B:
        min_ob += 1
    # 부감독관 필요
    else:
        # 총감독관 감시 인원 제외
        a -= B
        min_ob += 1
        
        # 부감독관 수로 나누어 떨어지면 몫 더하기
        if a % C == 0:
            min_ob += a // C
        # 부감독관 수로 나누어 떨어지지 않으면 몫 + 1 더하기
        else:
            min_ob += a // C + 1

# 결과
print(min_ob)
