sonlar = list(map(int, input().split()))
takrorlarsiz = sorted(set(sonlar))
print(*takrorlarsiz)