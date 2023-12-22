import sys 

N = int(input())

# 탐색 시간 줄이기 위해 set으로 받음
n_list = set(map(int, input().split()))

M = int(input())

target_list = list(map(int, input().split()))

# target_list 각 원소별 탐색
for target in target_list:   
	print(1) if target in n_list else print(0)