n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    d[k] = v
for k, v in d.items():
    print(f'{k}={v}')