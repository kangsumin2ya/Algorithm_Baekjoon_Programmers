def solution(numbers):
    
    # numbers.sort()
    # max1 = max(numbers)
    # numbers.pop()
    # max2 = max(numbers)
    
    numbers.sort()
    
    answer = numbers[-1] * numbers[-2]
    
    return answer