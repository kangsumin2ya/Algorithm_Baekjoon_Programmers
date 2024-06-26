import sys

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. for문으로 N개의 단어 입력
words = [str(input().rstrip()) for _ in range(N)]

# 3. set 함수로 중복 제거
no_overlap_words = list(set(words))

# 4. sort() 함수로 2가지 기준에 따라 정렬
sort_words = sorted(no_overlap_words, key=lambda x: (len(x), x))

# 5. 원하는 형식으로 출력
for word in sort_words:
    print(word)