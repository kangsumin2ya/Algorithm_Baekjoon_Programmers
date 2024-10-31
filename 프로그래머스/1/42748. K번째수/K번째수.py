def solution(array, commands):
    answer = []
    
    # 명령어에 하나씩 접근
    for command in commands:
        # 변수 맵핑
        i, j, k = command[0], command[1], command[2]
        # 리스트 구하기
        temp = [array[n] for n in range(i-1, j)]
        # 정렬
        temp.sort()
        # k번째 숫자 리스트에 추가
        answer.append(temp[k-1])
            
    
    return answer