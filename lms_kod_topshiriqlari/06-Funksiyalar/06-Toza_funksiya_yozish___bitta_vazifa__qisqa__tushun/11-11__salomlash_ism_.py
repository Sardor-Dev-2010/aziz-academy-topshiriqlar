import sys
def salomlash(ism):
    return 'Salom, ' + ism + '!'
data = sys.stdin.read().split()
if data:
    print(salomlash(data[0]))