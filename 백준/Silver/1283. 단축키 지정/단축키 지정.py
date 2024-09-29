import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 문자열 입력
strings = [list(input().rstrip().split()) for _ in range(N)]

# 옵션 저장 리스트
options = []

# 단축키 생성
for string in strings:
    for i in range(len(string)):
        if string[i][0].lower() not in options:
            options.append(string[i][0].lower())
            # 문자에 괄호 추가
            string[i] = '[' + string[i][0] + ']' + string[i][1:]
            break

    # 첫글자 모두 존재
    else:
        for i in range(len(string)):
            # 첫 글자 이후의 문자 탐색
            for j in range(1, len(string[i])):
                if string[i][j].lower() not in options:
                    options.append(string[i][j].lower())
                    string[i] = string[i][:j] + '[' + string[i][j] + ']' + string[i][j + 1:]
                    break
            else:
                continue
            break

# 결과 출력
for option in strings:
    print(' '.join(option))
