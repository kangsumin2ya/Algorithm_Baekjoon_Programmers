def solution(sizes):
    answer = 0
    
    # 더 작은 값이 앞으로 오도록 정렬
    for size in sizes:
        size.sort()
    
    # 지갑 길이 초기화
    width, height = 0, 0
    
    # 가장 큰 값 찾기
    for size in sizes:
        if size[0] > width:
            width = size[0]
        if size[1] > height:
            height = size[1]
    
    # 크기 계산
    answer = width * height
    
    return answer