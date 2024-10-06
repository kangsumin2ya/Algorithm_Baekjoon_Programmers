import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 포켓몬 사전 정의
pokemon_dict = {}
pokemon_reverse_dict = {}

# 포켓몬 입력
for i in range(N):
    # 이름 입력
    name = input().rstrip()

    # 번호, 이름을 사전에 추가
    pokemon_dict[i+1] = name
    pokemon_reverse_dict[name] = i + 1

# 문제 맞추기
for _ in range(M):
    question = input().rstrip()

    # 숫자인지 아닌지 확인
    if question.isdigit():
        print(pokemon_dict[int(question)])
    else:
        print(pokemon_reverse_dict[question])
