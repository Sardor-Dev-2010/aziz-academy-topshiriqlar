import sys

def count_words(s):
    sozlar = s.split()
    soni = 0
    for soz in sozlar:
        soni += 1
    return soni

data = sys.stdin.read()
if data.strip():
    print(count_words(data.strip()))