A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
only_a = A - (B | C)
only_b = B - (A | C)
only_c = C - (A | B)
natija = only_a | only_b | only_c
if not natija:
    print("BO'SH")
else:
    print(*sorted(natija))