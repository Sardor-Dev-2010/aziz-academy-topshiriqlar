
k = input().split()
try:
    t = (int(k[0]), k[1], float(k[2]))
except:
    t = (int(k[0]), int(k[1]), k[2])
print(t)