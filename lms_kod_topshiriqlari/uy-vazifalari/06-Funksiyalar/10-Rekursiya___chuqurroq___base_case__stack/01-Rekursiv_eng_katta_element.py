def eng_katta(sonlar):
    if len(sonlar) == 1:
        return sonlar[0]
    qolgani = eng_katta(sonlar[1:])
    if sonlar[0] > qolgani:
        return sonlar[0]
    return qolgani

sonlar = list(map(int, input().split()))
print(eng_katta(sonlar))