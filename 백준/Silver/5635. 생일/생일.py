import sys
from datetime import datetime

input = sys.stdin.readline

# 2. 오늘 날짜를 변수에 저장한다.
today = datetime.today().date()

# 3. n을 입력받는다.
n = int(input())

# 4. n만큼 반복해서 이름과 생일을 입력받는다.
students = [input().strip().split(' ', 1) for _ in range(n)]

# 5. 입력받은 생일을 날짜 객체로 변경한다.
for student in students:
    student[1] = datetime.strptime(student[1], '%d %m %Y').date()

# 6. 나이를 계산한다.
for student in students:
    age = (today - student[1]).days
    student.append(age)

# 7. 나이순으로 정렬한다.
students.sort(key=lambda x: x[2])

# 8. 원하는 형태로 출력한다.
print(students[0][0])
print(students[-1][0])