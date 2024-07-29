import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 학생 점수 저장 리스트
students = []

# N명 점수 입력
for _ in range(N):
    students.append(input().split())

# 정렬하기
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(students)):
    print(students[i][0])