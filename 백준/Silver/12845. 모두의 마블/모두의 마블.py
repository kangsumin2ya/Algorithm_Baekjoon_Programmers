n = int(input())
cards = list(map(int, input().split()))

cards.sort(reverse=True)

level = cards[0]
total_gold = 0

for card in cards[1:]:
    total_gold += level + card

    if level >= card:
        pass
    else:
        level = card
print(total_gold)