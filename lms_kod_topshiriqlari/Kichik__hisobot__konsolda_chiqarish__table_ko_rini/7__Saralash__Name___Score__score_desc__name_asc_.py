n_line = input().split()
if not n_line:
    n = 0
else:
    n = int(n_line[0])

tokens = []
while len(tokens) < n * 2:
    tokens.extend(input().split())

data = []
for i in range(n):
    name = tokens[i*2]
    score = int(tokens[i*2 + 1])
    data.append([name, score])

# Bubble sort: score DESC, name ASC
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][1] < data[j+1][1] or (data[j][1] == data[j+1][1] and data[j][0] > data[j+1][0]):
            data[j], data[j+1] = data[j+1], data[j]

print(f"{'Name':<10} | {'Score':>5}")
print("-" * 10 + "+" + "-" * 5)

for row in data:
    print(f"{row[0]:<10} | {row[1]:>5}")