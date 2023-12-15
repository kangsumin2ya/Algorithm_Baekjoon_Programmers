from collections import deque
import sys

input = sys.stdin.readline

bracket_list = []
n = int(input())

for i in range(n):
    bracket_list.append(input().strip())  # 줄바꿈 문자 제거해 괄호열을 리스트에 추가

for brackets in bracket_list:
    stack = deque()
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if stack and stack[-1] == "(":
                stack.pop()  # 올바른 쌍의 괄호를 찾으면 스택에서 제거
            else:
                print("NO")
                break  # 올바른 쌍의 괄호가 아닌 경우 "NO"를 출력하고 반복 중단
    else:
        if not stack:  # 스택이 비어있다면 모든 괄호가 올바른 쌍을 이루었음 의미
            print("YES")
        else:
            print("NO")  # 올바르지 않은 쌍의 괄호가 스택에 남아있는 경우 "NO" 출력