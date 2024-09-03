import sys

input = sys.stdin.readline

# 글자 입력
strings = [list(str(input().rstrip())) for _ in range(5)]

# 원래 글자 저장 리스트
origin_words = []

# 세로로 읽기
for j in range(15):  # 최대 15개의 글자
    for i in range(5):  # 5개의 단어
        # 인덱스가 단어 길이보다 작은 경우에만
        if j < len(strings[i]):
            origin_words.append(strings[i][j])

# 결과 출력
print(''.join(origin_words))