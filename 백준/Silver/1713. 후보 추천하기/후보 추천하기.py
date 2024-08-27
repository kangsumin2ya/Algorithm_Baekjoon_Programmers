import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 전체 추천 횟수 입력
recommendations = int(input())

# 추천 받은 학생 번호 입력
selected_students = list(map(int, input().split()))

# 사진틀 딕셔너리 정의
frames = dict()

# 추가된 시간 변수
time = 0

for i in range(recommendations):
    # 사진틀에 학생 있는지 확인
    if selected_students[i] in frames:
        # 있는 학생이면 추천 횟수 증가
        frames[selected_students[i]][0] += 1
    else:
        # 자리가 있다면 추가
        if len(frames) < N:
            frames[selected_students[i]] = [1, i]
        # 자리가 없다면 추천 횟수 적은 사람 찾기
        else:
            # 추천 횟수, 추가된 시간 기준 정렬 (리스트로 변환)
            out_list = sorted(frames.items(), key=lambda x: (x[1][0], x[1][1]))
            # 학생 제거
            out_student = out_list[0][0]
            del(frames[out_student])
            # 새로운 학생 추가
            frames[selected_students[i]] = [1, i]

# 번호 오름차순으로 정렬
nums = list(sorted(frames.keys()))

# 결과 출력
print(" ".join(map(str, nums)))