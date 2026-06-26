# Task 14 fixed
n_line = input().split()
if not n_line:
    n = 0
else:
    n = int(n_line[0])

tokens = []
while len(tokens) < n * 2:
    tokens.extend(input().split())

print(f"{'Name':<10} | {'Score':>5}")
print("-" * 10 + "+" + "-" * 5)

top_n = ""
top_s = -1

for i in range(n):
    name = tokens[i*2]
    score = int(tokens[i*2+1])
    print(f"{name:<10} | {score:>5}")
    
    if score > top_s or (score == top_s and (top_n == "" or name < top_n)):
        top_s = score
        top_n = name

print(f"TOP: {top_n} {top_s}")