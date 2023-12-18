from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = input().rstrip()

A = list(map(int, input().split()))

M = input().rstrip()

target_list = list(map(int, input().split()))

A.sort()

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a,left_value)

    return right_index - left_index

for i in range(len(target_list)):
    print(count_by_range(A, target_list[i], target_list[i]), end=' ')