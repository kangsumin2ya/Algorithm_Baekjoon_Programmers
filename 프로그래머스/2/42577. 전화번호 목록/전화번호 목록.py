def solution(phone_book):
    # 해시맵 생성
    hash_map = {}
    
    # 해시맵에 전화번호 넣기
    for phone in phone_book:
        hash_map[phone] = 1
    
    # 접두어가 해시맵에 있는지 찾기
    for phone in phone_book:
        start_num = ""
        
        # 숫자 하나씩 증가시켜서 찾기
        for num in phone:
            start_num += num
            
            # 접두어 찾기 (자기 자신 제외)
            if start_num in hash_map and start_num != phone:
                return False
    
    return True