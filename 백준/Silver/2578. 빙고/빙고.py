import sys

input = sys.stdin.readline

# 1. 빙고 함수 구현
# 1-1. 가로
def check_horizontal():
    line = 0
    for i in range(5):
        count = 0
        for j in range(5):
            if bingo[i][j] == 0:
                count += 1
        if count == 5:
            line += 1
    return line

# 1-2. 세로
def check_vertical():
    line = 0
    for i in range(5):
        count = 0
        for j in range(5):
            if bingo[j][i] == 0:
                count += 1
        if count == 5:
            line += 1
    return line

# 1-3. 왼-오 대각선
def check_diagonal1():
    count = 0
    for i in range(5):
        if bingo[i][i] == 0:
            count += 1
    if count == 5:
        return 1
    return 0

# 1-4. 오-왼 대각선
def check_diagonal2():
    count = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            count += 1
    if count == 5:
        return 1
    return 0

# 2. 철수 : 5번 반복해 한 줄에 5개 숫자 입력
bingo = [list(map(int, input().split())) for _ in range(5)]

# 3. 사회자 : 5번 반복해 한 줄에 5개 숫자를 리스트에 추가
numbers = []
for k in range(5):
    numbers.extend(list(map(int, input().split())))

# 4. 철수, 사회자의 숫자 비교
for k in range(25):
    check_num = numbers[k]

    # 4-1. 부른 숫자 0으로 변경
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == check_num:
                bingo[i][j] = 0

    # 4-2. 빙고 체크
    if k >= 11:
        line = 0
        line += check_horizontal()
        line += check_vertical()
        line += check_diagonal1()
        line += check_diagonal2()

        # 5. 빙고이면 해당 숫자의 순서 출력
        if line >= 3:
            print(k + 1)
            break
