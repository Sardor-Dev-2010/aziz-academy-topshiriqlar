import sys

def is_leap_year(y):
    if y % 400 == 0:
        return "Ha"
    elif y % 100 == 0:
        return "Yo'q"
    elif y % 4 == 0:
        return "Ha"
    else:
        return "Yo'q"

data = sys.stdin.read().split()
if data:
    print(is_leap_year(int(data[0])))