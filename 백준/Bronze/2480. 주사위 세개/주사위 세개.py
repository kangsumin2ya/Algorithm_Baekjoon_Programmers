import sys

input = sys.stdin.readline

list_n = list(map(int, input().split()))

if list_n[0] == list_n[1] == list_n[2]:
    answer = 10000 + list_n[0] * 1000

else:
    if list_n[0] == list_n[1] :
        answer = 1000 + list_n[0] * 100
    elif list_n[1] == list_n[2]:
        answer = 1000 + list_n[1] * 100
    elif list_n[2] == list_n[0]:
        answer = 1000 + list_n[2] * 100
    else:
        answer = max(list_n) * 100

print(answer)