
n = int(input())
son = list(map(int, input().split()))
natija = son[-(n // 2):]
print(natija)
