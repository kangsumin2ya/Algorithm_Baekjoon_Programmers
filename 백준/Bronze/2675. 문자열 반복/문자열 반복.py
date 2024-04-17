import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = ''
    R, S = map(str, input().split())
    
    for s in S:
        answer += s*int(R)

    print(answer)