sonlar = list(map(int, input().split()))
takror = len(sonlar) - len(set(sonlar))
print(takror)