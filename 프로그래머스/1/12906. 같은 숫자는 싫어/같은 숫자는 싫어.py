from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = []
    
    answer.append(arr.popleft())
    while arr :
        element = arr.popleft()
        if element != answer[-1]:
            answer.append(element)
        else:
            pass
    return answer