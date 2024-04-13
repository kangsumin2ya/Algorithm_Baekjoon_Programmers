import sys

input = sys.stdin.readline

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(input())

for i in alphabet:
    word = word.replace(i, '0')

print(len(word)-1)