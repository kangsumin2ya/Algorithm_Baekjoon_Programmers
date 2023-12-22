import sys

input = sys.stdin.readline

N = int(input())

n_list = list(map(int, input().split()))

M = int(input())

target_list = list(map(int, input().split()))

n_list.sort()

for i in range(M):

    is_exist = 0

    target = target_list[i]

    start = 0
    end = len(n_list) - 1

    while start <= end:
        mid_index = (start + end) // 2
        mid_value = n_list[mid_index]

        if mid_value < target:
            start = mid_index + 1

        elif mid_value > target:
            end = mid_index - 1

        else:
            is_exist = 1
            break

    print(is_exist)