# 테스트 케이스 입력
T = int(input())

# 테스트 케이스만큼 반복 수행
for _ in range(T):
    # 문자열 입력
    word = str(input())

    # 원하는 글자 저장
    new = [word[0], word[-1]]
    
    # 원하는 형태로 출력
    print(''.join(new))