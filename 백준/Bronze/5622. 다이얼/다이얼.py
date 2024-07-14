import sys

input = sys.stdin.readline

# 단어 입력
word = list(input().rstrip())

# 전화기 정보 딕셔너리
phone = {
    1: [],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
    0: []
}

# 시간 더하기
count = 0

for w in word:
    for key, value in phone.items():
        # if value == w:
        if w in value:
            count += key + 1

# 출력
print(count)