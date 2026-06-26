A = list(map(int, input().split()))
B = list(map(int, input().split()))
juft = {(a, b) for a in A for b in B}
print(len(juft))
for a, b in sorted(juft):
    print(f"{a},{b}")