
n = input().split()
word = [x.lower()  for x in n if x.lower().startswith('a')]
if word:
    print(' '.join(word))
else:
    print("BO'SH")