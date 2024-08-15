import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 강의 길이 입력
lectures = list(map(int, input().split()))

# 이분 탐색 초기값 정의
start = max(lectures)
end = sum(lectures)
answer = 0

# 이분 탐색 수행
while start <= end:
    # 중앙값 정의
    mid = (start + end) // 2
    # 블루레이 개수 변수 정의
    count = 1
    # 지금 블루레이에 담긴 강의 길이 합
    lectures_sum = 0
    # 블루레이 개수 세기
    for lecture in lectures:
        # 현재 블루레이에 담을 수 있다면 담기
        if lectures_sum + lecture <= mid:
            lectures_sum += lecture
        # 담을 수 없다면 다음 블루레이에 넣기
        else:
            count += 1
            lectures_sum = lecture

    # 블루레이 크기가 적절한 값인지 확인
    if count > M:
        # 블루레이가 더 많이 필요하니까 블루레이 크기 증가
        start = mid + 1
    else:
        # 블루레이 크기가 M 이내면 블루레이 크기 저장하고 크기 감소
        answer = mid
        end = mid - 1

print(answer)
