n = int(input())
for i in range(n):
    row = input().split()
    name = row[0]
    status = "present" if int(row[1]) == 1 else "absent"
    print(f"{name}|{status}")