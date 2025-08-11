import sys

input = sys.stdin.readline


# DFS 구현
def dfs(node):
    # 삭제 노드 표현
    parent[node] = 51
    # 부모 노드가 지울 노드 번호와 똑같은 경우 계속 탐색해 삭제 노드로 표현
    for i in range(N):
        if parent[i] == node:
            dfs(i)


# 입력받기
N = int(input())
parent = list(map(int, input().split()))
delete_node = int(input())

# 노드 삭제
dfs(delete_node)

# 리프 노드 개수 저장 변수 초기화
count = 0

# 리프 노드 개수 세기
for i in range(N):
    # 삭제되지 않은 상태에서 자식 노드가 없다면 리프노드 개수 추가
    if parent[i] != 51 and i not in parent:
        count += 1

# 정답 출력
print(count)