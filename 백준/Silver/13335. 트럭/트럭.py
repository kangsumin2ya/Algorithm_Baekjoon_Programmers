import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())

truck_weights = list(map(int, input().split()))

on_bridge = [0] * w
time = 0

while on_bridge:
    time += 1
    on_bridge.pop(0)

    if truck_weights:
        if sum(on_bridge) + truck_weights[0] <= L:
            on_bridge.append(truck_weights.pop(0))
        else:
            on_bridge.append(0)

print(time)