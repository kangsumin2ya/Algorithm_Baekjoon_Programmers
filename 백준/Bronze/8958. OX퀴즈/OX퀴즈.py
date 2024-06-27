import sys

input = sys.stdin.readline

# 1. 테스트케이스 수 입력받기
T = int(input())

# 2. 테스트케이스만큼 문자열 입력받기
results = [list(input().rstrip()) for _ in range(T)]

# 3. 인덱스로 for문 돌면서 문제를 맞았는지 확인
for result in results:
    scores = []
    score = 0
    
    for i in range(len(result)):
        if result[i] == 'O':
            score += 1
            if i > 0:
                if result[i-1] == '0':
                    score += 1
        else:
            score = 0
            
        scores.append(score)

    # 4. 점수 출력
    print(sum(scores))