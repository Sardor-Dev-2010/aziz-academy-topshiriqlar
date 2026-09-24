import sys
sys.stdin.read()
logs = [1, 2, 3]
def reset():
    global logs
    logs = []
reset()
print(len(logs))