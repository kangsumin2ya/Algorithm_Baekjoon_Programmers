from collections import deque

def solution(begin, target, words):
    
    # 변환 불가능하면 바로 0 반환
    if target not in words:
        return 0
    # 가능하면 탐색 진행
    return bfs(begin, target, words)


def bfs(begin, target, words):
    # 시작 단어, 0단계 초기화
    queue = deque([(begin, 0)])
    
    # 큐 빌때까지 반복
    while queue:
        now, step = queue.popleft()
        
        # target과 같으면 정답 반환
        if now == target:
            return step
        
        # 단어 확인해서 변경 가능 여부 확인
        for word in words:
            count = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    count += 1
            # 한번만 바꿀 수 있으니까 확인
            if count == 1:
                queue.append([word, step + 1])