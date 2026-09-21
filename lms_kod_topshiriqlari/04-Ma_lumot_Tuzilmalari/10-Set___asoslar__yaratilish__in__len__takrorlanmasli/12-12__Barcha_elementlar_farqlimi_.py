sonlar = list(map(int, input().split()))
if len(sonlar) == len(set(sonlar)):
    print("Ha")
else:
    print("Yo'q")