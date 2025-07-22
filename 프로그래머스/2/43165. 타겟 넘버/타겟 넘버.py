
def solution(numbers, target):
    # 정답 변수 초기화
    answer = 0
    
    # 스택 (index, current_sum)
    stack = [(0,0)]
    
    while (stack) :
        index, current_sum = stack.pop()
        
        # 끝이라면
        if index == len(numbers):
            # 타겟 넘버인 경우 개수 추가
            if current_sum == target :
                answer +=1
            continue
        
        # 끝날 때까지 반복
        stack.append((index+1, current_sum + numbers[index]))
        stack.append((index+1, current_sum - numbers[index]))
        
    # 정답 반환
    return answer

# def dfs(index, current_sum):
#     # 종료 조건: 모든 숫자를 다 사용했을 때
#     if index == len(numbers):
#         return 1 if current_sum == target else 0

#     # 현재 숫자를 더하거나 뺀 두 가지 경우 모두 탐색
#     return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

# def solution(numbers, target):
#     # DFS 시작
    
#     answer = dfs(0, 0) 
#     return answer