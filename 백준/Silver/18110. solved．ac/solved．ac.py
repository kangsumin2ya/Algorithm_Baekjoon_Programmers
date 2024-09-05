import sys

input = sys.stdin.readline

# 반올림 함수 정의
def round_func(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

# N 입력
N = int(input())

# 난이도 리스트 입력
grades = [int(input()) for _ in range(N)]

# 의견 없다면 0 출력
if len(grades) == 0:
    print(0)

# 의견 있다면
else:
    # 15%가 몇명인지 계산
    except_people = round_func(N * 15 / 100)
    # 오름차순 정렬
    grades.sort()
    # 계산할 사람 저장
    people = []
    # 사람 제외 후 평균 계산
    for i in range(except_people, N - except_people):
        people.append(grades[i])
    # 결과 출력
    print(round_func(sum(people) / len(people)))
