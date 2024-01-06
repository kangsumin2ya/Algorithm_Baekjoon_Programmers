import sys

input = sys.stdin.readline

N = input().replace('\n','')

sum = 0

if '0' not in N:
    print(-1)
else:
    for i in N:
        sum += int(i)

    if sum % 3 != 0:
        print(-1)

    else:
        sorted_N = sorted(N, reverse=True)
        answer = ''.join(sorted_N)
        print(answer)