"""
Tosh, Qaychi, Qog'oz o'yini dasturi.
Ushbu dastur foydalanuvchi va kompyuter o'rtasidagi o'yinni boshqaradi.
Xatolarga chidamlilik va toza kod qoidalari asosida yozilgan.
"""

import random
import sys

# O'yin qoidalari va variantlari constant (o'zgarmas) sifatida
VARIANTLAR = ["tosh", "qaychi", "qogoz"]


def foydalanuvchi_tanlovi_olish() -> str:
    """
    Foydalanuvchidan o'yin elementini yoki chiqish buyrug'ini qabul qiladi.
    Bo'sh kiritish (EOF) va tasodifiy xatolarni try-except orqali ushlaydi.
    """
    while True:
        try:
            tanlov = input("Tosh, Qaychi yoki Qogoz? (yoki chiqish): ").strip().lower()
            
            # Agar foydalanuvchi hech narsa yozmay Enter bossa yoki bo'sh kiritsa
            if not tanlov:
                print("⚠️  Siz bo'sh qiymat kiritingiz. Iltimos, qaytadan urining.")
                continue
                
            if tanlov == "chiqish":
                return "chiqish"
                
            if tanlov in VARIANTLAR:
                return tanlov
                
            print(f"❌ Noto'g'ri kiritish! Faqat quyidagilarni kiritish mumkin: {', '.join(VARIANTLAR)}.")
            
        except (KeyboardInterrupt, EOFError):
            # Foydalanuvchi Ctrl+C yoki Ctrl+D (EOF) bossa dastur qulamasligi uchun
            print("\n\n🚪 Dastur foydalanuvchi tomonidan kutilmaganda to'xtatildi.")
            return "chiqish"


def golibni_aniqla(user: str, computer: str) -> str:
    """
    Foydalanuvchi va kompyuter tanlovini solishtirib, g'olibni aniqlaydi.
    Natija: 'user', 'computer' yoki 'durang' qaytaradi.
    """
    if user == computer:
        return "durang"
        
    # Foydalanuvchi yutish shartlari jadvallari
    yutish_shartlari = {
        "tosh": "qaychi",
        "qaychi": "qogoz",
        "qogoz": "tosh"
    }
    
    if yutish_shartlari[user] == computer:
        return "user"
        
    return "computer"


def natijani_korsat(user_score: int, comp_score: int) -> None:
    """O'yin yakunlanganda yakuniy hisobotni ekranga chiroyli chiqaradi."""
    print("\n" + "="*30)
    print("🏁 O'YIN YAKUNLANDI!")
    print(f"📊 Yakuniy hisob -> Siz: {user_score} | Kompyuter: {comp_score}")
    
    if user_score > comp_score:
        print("🏆 Tabriklaymiz! Siz umumiy o'yinda yutdingiz! 🎉")
    elif comp_score > user_score:
        print("🤖 Kompyuter g'olib bo'ldi. Keyingi safar omad tilaymiz! 👍")
    else:
        print("🤝 Do'stlik g'alaba qozondi! Durang!")
    print("="*30)


def main() -> None:
    """Dasturning asosiy boshqaruv funksiyasi (O'yin sikli)."""
    user_score = 0
    comp_score = 0
    
    print("=== Tosh, Qaychi, Qog'oz o'yiniga xush kelibsiz! ===")
    print("O'yinni tugatish uchun 'chiqish' deb yozing.\n")

    while True:
        user_choice = foydalanuvchi_tanlovi_olish()
        
        if user_choice == "chiqish":
            break
            
        comp_choice = random.choice(VARIANTLAR)
        print(f"🤖 Kompyuter tanladi: {comp_choice.capitalize()}")
        
        natija = golibni_aniqla(user_choice, comp_choice)
        
        if natija == "durang":
            print("🤝 Durang!")
        elif natija == "user":
            print("🎉 Siz yutdingiz!")
            user_score += 1
        else:
            print("💻 Kompyuter yutdi!")
            comp_score += 1
            
        print(f"📈 Joriy hisob -> Siz: {user_score} | Kompyuter: {comp_score}\n")
        
    natijani_korsat(user_score, comp_score)


if __name__ == "__main__":
    main()
