A = set(input().strip().split())
B = set(input().strip().split())
name = A & B
print(len(name))
for names in sorted(name):
    print(names)
