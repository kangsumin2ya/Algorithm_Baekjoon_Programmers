whole = [int(i) for i in range(1, 31)]

attend = [int(input()) for _ in range(28)]

absent = []


for w in whole:
    if w not in attend:
        absent.append(w)

for a in absent:
    print(a)