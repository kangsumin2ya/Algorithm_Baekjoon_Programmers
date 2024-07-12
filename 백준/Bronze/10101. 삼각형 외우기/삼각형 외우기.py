import sys

input = sys.stdin.readline

# 입력받기
angles = [int(input()) for _ in range(3)]

angles_sum = sum(angles)

# Equilateral
if all(angle == 60 for angle in angles):
    print('Equilateral')

elif angles_sum == 180:
    # Scalene
    if len(angles) == len(set(angles)):
        print('Scalene')
    # Isosceles
    else:
        print('Isosceles')
# Error
else:
    print('Error')