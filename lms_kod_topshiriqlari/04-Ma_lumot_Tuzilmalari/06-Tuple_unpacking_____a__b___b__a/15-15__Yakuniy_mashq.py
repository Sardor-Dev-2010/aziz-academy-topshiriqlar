
n = int(input())
son = list(map(int, input().split()))
natija = son[0]
natija2 = son[-1]
qolgani = son[1: -1]
print(f"{natija}\n{qolgani}\n{natija2}")