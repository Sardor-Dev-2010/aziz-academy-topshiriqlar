a = set(map(int, input().split()))
b = set(map(int, input().split()))
natija = a.intersection(b)
if not natija:
    print("BO'SH")
else:
    sorted_natija = sorted(natija)
    print(*sorted_natija)
