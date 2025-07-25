import heapq

def solution(scoville, K):
    answer = 0
    
    # 힙큐 정의 -> heapify는 제자리 정렬 --> 아래처럼 하면 None 반환
    # scoville_heapq = heapq.heapify(scoville)
    heapq.heapify(scoville)
    
    # 힙에 아무것도 없을 때까지 반복
    while scoville:
        # 모든 스코빌 지수가 K를 넘지 않으면 아래를 수행 -> 이런 조건 말고 그냥 최소 값이 K만 넘으면 다 넘는거니까 그걸 확인하도록 수정
        # if all(s < K for s in scovilee_heapq):
        # 최소가 K를 넘는지 확인
        min_num1 = heapq.heappop(scoville)
        
        # 넘으면 바로 정답 반환
        if min_num1 >= K:
            return answer
        
        else:
            # 두번째로 작은 것 뺴기       
            min_num2 = heapq.heappop(scoville)      
            # 섞기
            mix_num = min_num1 + min_num2 * 2       
            # 힙에 다시 넣기
            heapq.heappush(scoville, mix_num)            
            # 섞기 횟수 추가
            answer += 1
        
        
        # 만약 모든 스코빌 지수가 K를 넘으면 횟수 반환 
        # if all(s >= K for s in scovilee_heapq):
        #     return answer
        # 힙에 남은 1개 원소가 K를 넘지 못하면 -1 반환
            if len(scoville) == 1 and scoville[0] < K:
                return -1
        
    
    