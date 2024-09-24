import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 특성값 입력
values = list(map(int, input().split()))

# 시작, 종료 인덱스 지정
start, end = 0, N - 1

# 0과 가까운 값의 합을 저장할 변수 초기화
answer_sum = 2000000000
answer_pair = [0, 0]

# 포인터 겹칠 때까지 반복
while start < end:
    # 합 구하기
    temp_sum = values[start] + values[end]

    # 절댓값이 0과 가까운지 확인 후 갱신
    if abs(answer_sum) > abs(temp_sum):
        answer_sum = temp_sum
        answer_pair = [values[start], values[end]]

    # 합이 0이면 반환
    if temp_sum == 0:
        break

    # 합이 0보다 크면 오른쪽 포인터 왼쪽 이동
    if temp_sum > 0:
        end -= 1
    # 합이 0보다 작다면 왼쪽 포인터 오른쪽 이동
    else:
        start += 1

# 정답 출력
print(' '.join(map(str, answer_pair)))
