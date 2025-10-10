def solution(clothes):
    
    # 해시맵 정의
    hash_map = {}
    
    # 해시맵에 넣기
    for cloth in clothes:
        if cloth[1] not in hash_map:
            hash_map[cloth[1]] = [cloth[0]]
        else:
            hash_map[cloth[1]] += [cloth[0]]
            
    # 곱하기 위해 1로 초기화
    answer = 1
    
    # 조합수 = 각 가짓수 곱하면 됨
    for _, values in hash_map.items():
        answer *= (len(values) + 1)
        
    return answer - 1