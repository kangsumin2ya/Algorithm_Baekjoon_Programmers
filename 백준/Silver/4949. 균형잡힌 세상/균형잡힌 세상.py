import sys

input = sys.stdin.readline


# 체크 함수
def check_balance(string):
    stack = []
    for s in string:
        if s in '([':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return not stack


while True:
    # 입력 받기
    sentence = input().rstrip()

    if sentence == ".":
        break

    if check_balance(sentence):
        print("yes")
    else:
        print("no")