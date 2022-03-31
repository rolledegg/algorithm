n,m = map(int,input().split()) # 행, 열
result = 0

for i in range(1,n+1):
    cards = list(map(int,input().split()))
    min= cards[0]
    for card in cards:
        if card < min:
            min = card

    result = max(min, result)
