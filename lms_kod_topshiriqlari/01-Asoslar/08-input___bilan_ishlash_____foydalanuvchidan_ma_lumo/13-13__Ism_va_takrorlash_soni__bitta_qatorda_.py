data = input().split()
ism = data[0]
n = int(data[1])
natija = (ism + " ") * (n - 1) + ism
print(natija)