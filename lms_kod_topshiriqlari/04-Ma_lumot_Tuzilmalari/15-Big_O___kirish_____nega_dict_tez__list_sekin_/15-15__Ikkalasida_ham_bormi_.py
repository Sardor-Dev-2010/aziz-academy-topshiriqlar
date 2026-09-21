a = set(map(int, input().split()))
b = set(map(int, input().split()))
target = int(input())
if target in a and target in b:
    print("Ha")
else:
    print("Yo'q")