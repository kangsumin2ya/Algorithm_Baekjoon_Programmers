import sys

input = sys.stdin.readline

# 입력
inputs = [str(input().rstrip()) for _ in range(3)]

# 3가지 입력 중 숫자 찾기
num = [i for i in inputs if i.isnumeric()][0]

# 세 문자열 다음의 문자열 구하기 위해 4에서 숫자의 인덱스를 뺀 나머지를 숫자에 더해준다
next_num = int(num) + (3 - inputs.index(num))

# FizzBuzz 문제에 따라 출력
if next_num % 3 == 0 and next_num % 5 == 0:
    print('FizzBuzz')
elif next_num % 3 == 0 and next_num % 5 != 0:
    print('Fizz')
elif next_num % 3 != 0 and next_num % 5 == 0:
    print('Buzz')
else:
    print(next_num)