# Foydalanuvchining yoshiga qarab kirish ruxsatini tekshirish
# Kurs: IT Dasturlash
# Mavzu: Mantiqiy operatorlar: and, or, not
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
malumot = input().split()
yosh = int(malumot[0])
if yosh > 18 or yosh < 7:
    if yosh > 18 and len(malumot) > 1:
        ortacha_ball = int(malumot[1])
        if ortacha_ball > 80:
            print("Kirish ruxsati berildi. Maxsus imtiyozlar berildi")
        else:
            print("Kirish ruxsati berildi")
    else:
        print("Kirish ruxsati berildi")
elif yosh >= 7 and yosh <= 18:
    print("Kirish ruxsati berildi")
else:
    print("Kirish ruxsati berilmadi")