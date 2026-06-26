
n = int(input())
sonlar = list(map(int, input().split()))
k = int(input())
son = sonlar[0]
masofa = abs(sonlar[0] - k)
for i in sonlar:
    yangi_masofa = abs(i - k)
    if yangi_masofa < masofa or (yangi_masofa == masofa and i < son):
        son = i
        masofa = yangi_masofa
print(son)