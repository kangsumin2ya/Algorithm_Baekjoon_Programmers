import sys

input = sys.stdin.readline

# 정답 저장할 리스트 정의
answer = []

while True:
    # 길이 입력
    lengths = list(map(int, input().split()))
    
    # 모든 변의 길이가 0이면 while 종료
    if all(lengths) == 0:
        break
    
    # 가장 긴 변 찾기 쉽게 하기 위해 정렬
    lengths.sort()
    
    # 각 변의 길이 제곱
    square_lenghts = [x**2 for x in lengths]
    
    # 직각 여부 확인 위해 짧은 변들 더하기
    rest_sum = square_lenghts[0] + square_lenghts[1]
    
    # 직각인 경우
    if square_lenghts[2] == rest_sum:
        answer.append('right')
    # 직각이 아닌 경우
    else:
        answer.append('wrong')

# 원하는 정답 출력
for a in answer:
    print(a)