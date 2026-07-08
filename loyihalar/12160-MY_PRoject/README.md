# 🎮 Tosh, Qaychi, Qog'oz — Konsol O'yini

Ushbu loyiha Python dasturlash tilida yaratilgan bo'lib, foydalanuvchiga kompyuterga qarshi klassik "Tosh, Qaychi, Qog'oz" o'yinini o'ynash imkoniyatini beradi. Dastur toza kod qoidalari (Clean Code), yuqori xatolarga chidamlilik (Robustness) va modulli tuzilma prinsiplari asosida ishlab chiqilgan.

## 🚀 Loyihaning asosiy vazifalari va imkoniyatlari
* **Xatolarga to'liq chidamlilik:** Dastur foydalanuvchi tomonidan bo'sh qiymat kiritilganda, tasodifiy harflar yozilganda yoki kutilmagan simvollar yuborilganda qulab tushmaydi, balki xatolikni foydalanuvchiga tushunarli tilda tushuntiradi.
* **Xavfsiz to'xtatish:** Terminalda `Ctrl + C` yoki `Ctrl + D` (EOF) tugmalari bosilganda dastur traceback xatolarisiz, madaniyatli tarzda o'yinni yakunlaydi.
* **Avtomatlashtirilgan mantiq:** Kompyuter o'z tanlovini `random` moduli orqali tasodifiy amalga oshiradi va g'olib maxsus mantiqiy algoritm yordamida aniqlanadi.
* **Hisob-kitob tizimi:** Har bir raunddan so'ng joriy hisob ko'rsatiladi va o'yin yakunida umumiy g'olib e'lon qilinadi.

## 🛠️ Texnik tuzilishi (Arxitektura)
Dastur kodining arxitekturasi **SOLID** prinsiplariga mos keladi:
1. `main()` — o'yinning asosiy sikli va boshqaruv markazi.
2. `foydalanuvchi_tanlovi_olish()` — ma'lumotlarni xavfsiz filtrlash va try-except bloki orqali inputni nazorat qilish.
3. `golibni_aniqla()` — o'yin qoidalarini tekshiruvchi sof mantiqiy funksiya.
4. `natijani_korsat()` — yakuniy natijalarni ekranga chiroyli formatda chiqaruvchi interfeys qismi.

## 💻 Ishga tushirish yo'riqnomasi

Dasturni kompyuteringizda ishga tushirish uchun quyidagi oddiy qadamlarni bajaring:

1. Kompyuteringizda Python (3.8 yoki undan yuqori versiya) o'rnatilganligini tekshiring.
2. Terminal yoki CMD (Buyruqlar satri) oynasini oching.
3. Loyiha fayli joylashgan papkaga o'ting:
   ```bash
   cd loyiha_papka_nomi
   ```
4. Dasturni quyidagi buyruq orqali ishga tushiring:
   ```bash
   python game.py
   ```

## 🎮 O'yin qoidalari
* O'yin boshlangach, terminalga `tosh`, `qaychi` yoki `qogoz` so'zlaridan birini kiritasiz.
* O'yinni istalgan vaqtda yakunlash uchun `chiqish` so'zini yozishingiz kifoya.
