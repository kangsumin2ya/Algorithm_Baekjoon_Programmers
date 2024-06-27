import sys

input = sys.stdin.readline

# 1. A, B, C 입력받기
A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

# 2. 숫자로 생각하고 A+B-C 연산
answer1 = int(A) + int(B) - int(C)

# 3. 문자로 생각하고 A+B-C 연산
temp = str(A) + str(B)
answer2 = int(temp) - int(C)

# 4. 출력
print(answer1)
print(answer2)