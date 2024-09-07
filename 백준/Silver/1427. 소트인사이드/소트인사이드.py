# 입력 받기
N = input()

# 숫자의 각 자리수를 내림차순으로 정렬
sorted_N = sorted(N, reverse=True)

# 정렬된 숫자들을 다시 하나의 문자열로 합치고 출력
print(''.join(sorted_N))
