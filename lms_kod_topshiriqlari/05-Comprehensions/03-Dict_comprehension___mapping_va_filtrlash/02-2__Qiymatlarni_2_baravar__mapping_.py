n = int(input())
natija = {key: int(value) * 2 for i in range(n) for key, value in [input().split()]}
print(natija)