import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
logs = []
def add_log(msg):
    logs.append(msg)
for i in range(n):
    add_log(lines[1 + i])
print(len(logs))
for w in logs:
    print(w)