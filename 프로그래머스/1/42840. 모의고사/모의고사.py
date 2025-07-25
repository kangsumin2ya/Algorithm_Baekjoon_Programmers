def solution(answers):
    answer = []
    
    # 문제 수 정의
    n = len(answers)
    
    # 문제 방식 생성
    first_ans = [1, 2, 3, 4, 5]
    second_ans = [2, 1, 2, 3, 2, 4, 2, 5]
    third_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 문제 수만큼 문제 풀이 생성
    first = (first_ans * ((n // len(first_ans)) + 1))[:n]
    second = (second_ans * ((n // len(second_ans)) + 1))[:n]
    third = (third_ans * ((n // len(third_ans)) + 1))[:n]
    
    # 점수 정의
    first_score = 0
    second_score = 0
    third_score = 0
    
    # 채점 --> 입력받은 변수가 answers인데 answer로 해서 틀림 & 문제 풀이랑 비교해야하는데 문제 풀이 방식과 비교해서 틀림...
    for fi, ai in zip(first, answers):
        if fi == ai:
            first_score += 1
    for si, ai in zip(second, answers):
        if si == ai:
            second_score += 1
    for ti, ai in zip(third, answers):
        if ti == ai:
            third_score += 1
            
    # 점수 비교 위해 모으기
    scores = [first_score, second_score, third_score]
    
    # 가장 큰값과 비교해 정답 리스트에 넣기
    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)
    
    # 답 리스트에 여러 값 있다면 오름차순 정렬
    if len(answer) > 1:
        answer.sort()
    
    return answer