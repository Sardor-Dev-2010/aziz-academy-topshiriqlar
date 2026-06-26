tokens = input().split()

k = int(tokens[0])
idx = 1
sozlamalar = {}

for _ in range(k):
    if idx >= len(tokens):
        tokens.extend(input().split())
    kalit = tokens[idx]
    qiymat = int(tokens[idx+1])
    sozlamalar[kalit] = qiymat
    idx += 2

if idx >= len(tokens):
    tokens.extend(input().split())
q_soni = int(tokens[idx])
idx += 1

for _ in range(q_soni):
    if idx >= len(tokens):
        tokens.extend(input().split())
    sorov = tokens[idx]
    print(sozlamalar.get(sorov, 0))
    idx += 1