# Sonlarni o'qib olamiz
sonlar = list(map(int, input().split()))

# Ularni kamayish tartibida saralaymiz
saralangan = sorted(sonlar, reverse=True)

# Eng katta 3 tasini ajratib olamiz
top_uchta = saralangan[:3]

# Natijani chiqaramiz
print(*top_uchta)