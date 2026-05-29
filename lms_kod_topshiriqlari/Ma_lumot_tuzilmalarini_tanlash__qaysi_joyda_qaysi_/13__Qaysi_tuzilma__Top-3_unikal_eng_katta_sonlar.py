# Task 13
data = input().split()
sonlar = []
for x in data:
    sonlar.append(int(x))

unikal = set(sonlar)
# Kamayish tartibida saralaymiz
saralangan = sorted(list(unikal), reverse=True)

# Top 3 ni olamiz
top_3 = saralangan[:3]

print(*top_3)