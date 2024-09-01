import sys

input = sys.stdin.readline

# DFS 구현
def dfs(v, parent):
    visited[v] = 1
    # 연결 노드 확인
    for i in tree[v]:
        if not visited[i]:
            # 연결 끝까지 확인
            if not dfs(i, v):
                return False
        # 방문한 노드인데 부모 노드 아니라면 트리 아님
        elif i != parent:
            return False
    return True

# n, m 입력
n, m = map(int, input().split())

# 케이스 번호 초기화
case = 1


# 간선 정보 입력
while True:
    # 종료 조건
    if n == 0 and m == 0:
        break

    # 트리 저장 그래프 정의
    tree = [[] for _ in range(n + 1)]

    # 방문 처리 리스트 정의
    visited = [0] * (n + 1)

    # 간선 정보 입력
    for _ in range(m):
        a, b = map(int, input().split())
        # 정보 저장
        tree[a].append(b)
        tree[b].append(a)

    # 트리 개수 변수 정의
    count = 0

    # DFS 수행
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                count += 1

    # 결과 출력
    if count == 0:
        print(f'Case {case}: No trees.')

    elif count == 1:
        print(f'Case {case}: There is one tree.')

    else:
        print(f'Case {case}: A forest of {count} trees.')

    # 테스트 케이스 수 증가
    case += 1

    # n, m 입력
    n, m = map(int, input().split())
