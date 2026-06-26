
lst = []
while True:
    buyruq = input().split()
    if buyruq[0] == "stop":
        break
    elif buyruq[0] == "append":
        lst.append(int(buyruq[1]))
    elif buyruq[0] == "insert":
        lst.insert(int(buyruq[1]), int(buyruq[2]))
    elif buyruq[0] == "remove":
        x = int(buyruq[1])
        if x in lst:
            lst.remove(x)
    elif buyruq[0] == "pop":
        lst.pop(int(buyruq[1]))
print(lst)