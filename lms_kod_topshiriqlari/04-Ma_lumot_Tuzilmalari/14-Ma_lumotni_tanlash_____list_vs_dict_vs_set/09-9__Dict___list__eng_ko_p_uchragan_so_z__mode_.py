sozlar = input().split()
hisob = {}

for s in sozlar:
    s_kichik = s.lower()
    hisob[s_kichik] = hisob.get(s_kichik, 0) + 1

max_miqdor = -1
eng_soz = ""

# Kalitlarni saralab olamiz (alifbo tartibi uchun)
kalitlar = sorted(list(hisob.keys()))

for k in kalitlar:
    if hisob[k] > max_miqdor:
        max_miqdor = hisob[k]
        eng_soz = k

print(f"{eng_soz} {max_miqdor}")