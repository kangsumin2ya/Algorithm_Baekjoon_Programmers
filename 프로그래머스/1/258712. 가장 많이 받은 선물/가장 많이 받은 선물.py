def solution(friends, gifts):
    # 친구들 수 정의
    n = len(friends)
    
    # 받을 선물 수 저장할 리스트 초기화
    answer = [0] * n
    
    # 선물 주고 받은 내역 저장할 맵 정의
    gift_map = [[0] * n for _ in range(n)]
    
    # 선물지수 저장 변수 정의
    gift_index = [0] * n
    
    # 선물 주고 받은 횟수 계산
    for gift in gifts:
        # 주고 받은 사람 분리
        A, B = gift.split()
        # 인덱스 접근
        give_idx, take_idx = friends.index(A), friends.index(B)
        # 선물지수 계산
        gift_index[give_idx] += 1
        gift_index[take_idx] -= 1
        # 주고 받은 횟수 저장
        gift_map[give_idx][take_idx] += 1

    # 맵에 접근해 받을 선물 계산
    for i in range(n):
        for j in range(i+1, n):
            # i가 준 횟수가 더 많으면?
            if gift_map[i][j] > gift_map[j][i]:
                answer[i] += 1
            # j가 준 횟수가 더 많으면?
            elif gift_map[i][j] < gift_map[j][i]:
                answer[j] += 1
            # 횟수가 없거나 같다면? -> 선물지수 확인
            else:
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[j] += 1
                    
    # 받을 선물의 최댓값 출력
    return(max(answer))