# def solution(nums):
#     # 중복 제거 위해 dictionary 변환
#     answer = list(dict.fromkeys(nums))
#     print(answer)
    
#     if (len(nums) // 2) <= len(answer):
#         return (len(nums) // 2)
    
#     return len(answer)

# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))

def solution(nums):
    # 중복 제거
    num = set(nums)
    
    # 가져갈 수 있는 폰켓몬 수와 종류수 중에서 더 큰 수를 출력
    answer = min((len(nums) // 2), len(num))
    return answer