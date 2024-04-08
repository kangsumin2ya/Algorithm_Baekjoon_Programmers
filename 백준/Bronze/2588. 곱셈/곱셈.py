import sys

input = sys.stdin.readline

n1 = int(input())
n2 = int(input())

n3 = n1 * (n2 % 10)

print(n3)

n4 = n1 * ((n2 % 100)//10)

print(n4)

n5 = n1 * (n2 // 100)

print(n5)

n6 = n5 * 100 + n4 * 10 + n3

print(n6)