import sys
x = int(sys.stdin.read().split()[0])
def ko_sat():
    return x + 1
def local_qil():
    x = 7
    return x
print(ko_sat())
print(local_qil())