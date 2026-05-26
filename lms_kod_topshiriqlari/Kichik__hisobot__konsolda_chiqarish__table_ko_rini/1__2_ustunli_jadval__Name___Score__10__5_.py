n = int(input())
rows =  []
for i in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
print(f"{'Name':<10} | {'Score':<5}")
print("-" * 10 + "+" + "-" * 5)
for name, score in rows:
    print(f"{name:<10} | {score:>5}")