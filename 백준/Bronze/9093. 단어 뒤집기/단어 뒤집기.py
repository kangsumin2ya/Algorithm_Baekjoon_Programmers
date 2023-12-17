from collections import deque

t = int(input())

for _ in range(t):
    answer = []
    sentence = deque(map(str, input().split()))

    for word in sentence:
        alphabet = deque(word)
        alphabet.reverse()

        answer.append(''.join(alphabet))

    print(' '.join(answer))