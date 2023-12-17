N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
target_list = list(map(int, input().split()))

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

result = []
for target in target_list:
    lower = lower_bound(A, target)
    upper = upper_bound(A, target)
    result.append(str(upper - lower))

print(' '.join(result))