a = set(map(int, input().split()))
b = set(map(int, input().split()))
natija = sorted(a.union(b))
print(*natija)
