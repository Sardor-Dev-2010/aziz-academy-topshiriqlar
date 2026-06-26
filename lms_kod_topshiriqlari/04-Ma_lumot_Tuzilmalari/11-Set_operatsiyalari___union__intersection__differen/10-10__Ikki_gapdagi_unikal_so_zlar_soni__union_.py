s1 = input().strip().lower().split()
s2 = input().strip().lower().split()
set1 = set(s1)
set2 = set(s2)
natija = set1 | set2
print(len(natija))