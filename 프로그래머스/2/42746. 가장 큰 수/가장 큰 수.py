def solution(numbers):
    answer = ''
    
    # 숫자를 문자열로 변경
    numbers = list(map(str, numbers))
    
    # 문자열 3번 반복 후 내림차순 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 문자열을 합해줌
    for num in numbers:
        answer += num
    
    # 숫자를 반환해야하니까 int형 변환 후 문자열화
    answer = str(int(answer))
    
    return answer