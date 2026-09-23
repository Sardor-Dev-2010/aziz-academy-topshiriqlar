N = int(input())
mx = int(input())
for _ in range(N - 1):
    x = int(input())
    if x > mx:
        mx = x
print(mx)