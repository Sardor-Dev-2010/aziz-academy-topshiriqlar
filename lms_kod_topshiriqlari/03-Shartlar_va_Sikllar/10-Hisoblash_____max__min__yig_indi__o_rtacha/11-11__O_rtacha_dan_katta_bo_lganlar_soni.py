
n = int(input())
son = list(map(int, input().split()))
total = sum(son)
ortacha = total / n
kattalar_soni = sum(1 for i in son if i > ortacha)

print(kattalar_soni)