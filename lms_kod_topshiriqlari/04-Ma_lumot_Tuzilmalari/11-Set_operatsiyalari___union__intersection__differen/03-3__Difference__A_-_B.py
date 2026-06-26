a = set(map(int, input().split()))
b = set(map(int, input().split()))
natija = a.difference(b)
if not natija:
    print("BO'SH")
else:
    print(*sorted(natija))
    
