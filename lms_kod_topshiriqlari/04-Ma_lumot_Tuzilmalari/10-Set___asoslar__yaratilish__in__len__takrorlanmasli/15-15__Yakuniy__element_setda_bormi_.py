sonlar = list(map(int, input().split()))
qidirilayotgan = int(input())
if qidirilayotgan in set(sonlar):
    print("Ha")
else:
    print("Yo'q")