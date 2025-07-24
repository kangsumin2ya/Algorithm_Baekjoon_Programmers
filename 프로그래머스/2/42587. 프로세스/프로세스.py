from collections import deque

def solution(priorities, location):
    # 실행한 프로세스 저장
    answer = []
    
    # 큐 정의 (인덱스, 우선순위 함께 저장)
    queue = deque((i, j) for i, j in enumerate(priorities))
    
    while queue:
        # 값 꺼내기
        process = queue.popleft()
        
        # 우선순위 높은 것 있으면 다시 큐 추가
        if queue and any(process[1] < q[1] for q in queue):
            queue.append(process)
        # 아니면 수행
        else:
            answer.append(process)
    
    # 실행 순서 찾기
    for a in answer:
        # 원하는 위치의 수라면
        if a[0] == location:
            # 인덱스의 1 더해주어야 순서
            return answer.index(a) + 1