from collections import deque

# 테스트 케이스 수 입력
num_cases = int(input())

for _ in range(num_cases):
    # 문서의 개수와 목표 문서의 위치 입력
    N, M = map(int, input().split())
    # 각 문서의 중요도 입력
    documents = list(map(int, input().split()))

    queue = deque((i, importance) for i, importance in enumerate(documents))
    order = 0

    while queue:
        current_doc = queue.popleft()
        if any(current_doc[1] < doc[1] for doc in queue):
            queue.append(current_doc)
        else:
            order += 1
            if current_doc[0] == M:
                print(order)
                break