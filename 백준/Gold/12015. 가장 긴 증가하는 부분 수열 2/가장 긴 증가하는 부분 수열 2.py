import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 수열 A 입력
A = list(map(int, input().split()))

# 정답 저장 리스트 정의 (인덱스 계산 편리 위해 초기값 0)
answer = [0]

# 이분 탐색 LIS 방법 적용
for a in A:
    # 지금까지 저장된 수열의 마지막 값이 a보다 작다면 증가하는 중 = 추가
    if answer[-1] < a:
        answer.append(a)
    # 아니면 들어갈 위치를 이분탐색으로 확인
    else:
        left, right = 0, len(answer)    # 정답 리스트 내에서 탐색

        # 이분탐색 정의
        while left < right:
            mid = (left + right) // 2

            if answer[mid] < a:
                left = mid + 1      # a가 크면 왼쪽 이동
            else:
                right = mid      # a가 작으면 오른쪽 이동

        # 찾은 위치에 값 추가
        answer[right] = a

# 결과 출력
print(len(answer) - 1)