def solution(land):

    N = len(land)
    
    for i in range(1, N):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
            
    return max(land[-1])