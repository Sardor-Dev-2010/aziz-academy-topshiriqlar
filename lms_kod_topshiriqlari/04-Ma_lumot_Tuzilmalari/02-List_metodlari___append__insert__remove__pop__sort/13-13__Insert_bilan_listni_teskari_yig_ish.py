n = int(input())
sonlar = list(map(int, input().split()))
son = []
for i in range(n):
    son.insert(0, sonlar[i])
print(son)
    