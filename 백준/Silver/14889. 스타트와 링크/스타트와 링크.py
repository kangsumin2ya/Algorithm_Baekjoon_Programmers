import sys

input = sys.stdin.readline

'''
[변수]
- 축구할 사람 N명(반드시 짝수) -> N/2명으로 팀 분리
- 사람 번호 : 1 ~ N번
- 능력치 : S_ij = i번 사람 & j번 사람 같은 팀일 때 더해지는 능력치
    - 속하는 사람들의 능력치를 모두 합하면 그 팀의 능력치가 됨

[조건]
- 스타트팀, 링크팀 능력치 차이 최소가 되도록 팀 분리
    - 이때의 최솟값 구하기

[풀이]
- N이 크기 않기 때문에 완전탐색(백트래킹)해도 될 것 같음 = DFS 활용
- S에서 i==j인 경우 자기 자신과의 능력치 -> 반드시 0 => 문제 풀이에 영향 X
- 문제에서 제시한 사람 번호 & S를 저장한 배열의 인덱스는 1 차이남
    - 번호 : 1부터 시작 / 인덱스 : 0부터 시작
- 이 문제는 N명을 2개 팀으로 나누면 됨 -> 2개의 조합 방법 찾기
    - 2개의 조합에 대한 능력치 합 계산
    - min()함수로 모든 조합 계산할 때까지 갱신

'''

# 입력
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 스타트팀 포함 여부 저장할 리스트 정의
visited = [False] * N

# 능력치 차이 최솟값 무한대로 초기화
min_diff = float('inf')


# dfs 정의
def dfs(depth, start):  # depth = 현재 스타트팀에 포함된 사람 수
    global min_diff

    # 만약 팀이 반으로 나눠지면 시작
    if depth == N // 2:
        start_team, link_team = [], []
        
        # 팀에 인덱스 추가
        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        # 각 팀 능력치 합 초기화
        start_sum, link_sum = 0, 0

        # 능력치 합하기
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                # 두 명 조합 만들고 Sij, Sji 모두 더함
                start_sum += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
                link_sum += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]

        # 능력치 차 최솟값 갱신
        min_diff = min(min_diff, abs(start_sum - link_sum))
        return

    # 팀 만들기 : depth가 N//2 될 때까지 팀 나누기
    for i in range(start, N):
        if not visited[i]:
            # 스타트팀에 추가
            visited[i] = True
            # 다음 멤버 찾기
            dfs(depth + 1, i + 1)
            # 탐색 후 빼기(백트래킹)
            visited[i] = False


# dfs 수행 (팀에 아무도 없을 때 0부터 시작)
dfs(0, 0)

# 출력
print(min_diff)
