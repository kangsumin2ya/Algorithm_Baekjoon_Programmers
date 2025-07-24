def solution(citations):
    # h 값
    answer = 0
    
    # 인용 횟수 정렬
    citations.sort()
    
    # 시작점, 끝점 정의
    start, end = 0, citations[-1]

    
    # 이분탐색
    while start <= end :
        # 중간값 정의
        mid = (start + end) // 2
        
        # h번 이상 인용된 논문 개수 계산
        count = 0
        
        for citation in citations:
            if citation >= mid:
                count += 1
                
        # h 값을 더 키워도 됨
        if count >= mid :
            answer = mid
            start = mid + 1
        
        # 아니면 줄여야 함
        else:
            end = mid - 1
            
    return answer