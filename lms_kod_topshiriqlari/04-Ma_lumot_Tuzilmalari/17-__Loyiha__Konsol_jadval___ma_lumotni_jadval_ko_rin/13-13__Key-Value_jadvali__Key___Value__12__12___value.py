n = int(input())
tokens = []
while len(tokens) < n * 2:
    tokens.extend(input().split())

print(f"{'Key':<12} | {'Value':>12}")
print("-" * 12 + "+" + "-" * 12)

for i in range(n):
    k = tokens[i*2]
    v = int(tokens[i*2 + 1])
    print(f"{k:<12} | {v:>11}")