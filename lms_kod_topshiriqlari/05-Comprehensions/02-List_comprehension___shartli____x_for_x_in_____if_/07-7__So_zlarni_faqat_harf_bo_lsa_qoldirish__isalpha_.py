
token = list(map(str, input().split()))
word = [t for t in token if t.isalpha()]
if word:
    print(' '.join(word))
else:
    print("BO'SH")