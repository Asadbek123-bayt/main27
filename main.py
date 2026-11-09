import random

def avto_safar_tahlili(haydovchi, masofa_km, olar_har_100km, benzin_narxi):
    kerakli_benzin = (masofa_km / 100) * olar_har_100km
    jami_xarajat = kerakli_benzin * benzin_narxi

    print(f"🚖 Haydovchi: {haydovchi} | Reys masofasi: {masofa_km} km")
    print(f"📊 Sarf koʻrsatkichi: 100 km ga {olar_har_100km} litr")
    print(f"⛽ Jami kerakli yoqilgʻi: {kerakli_benzin:.1f} litr")
    print(f"💰 Yoqilgʻi uchun umumiy xarajat: {int(jami_xarajat):,} soʻm")

    if masofa_km > 300:
        print("⚠️ Maslahat: Yoʻl uzoq, har 2 soatda toʻxtab dam olish tavsiya etiladi!")
    print("-" * 50 + "\n")

def batareya_holati_auditi(telefon_modeli, foiz, zaryadda_mi):
    print(f"📱 Qurilma: {telefon_modeli}")
    print(f"🔋 Batareya quvvati: {foiz}%")

    if zaryadda_mi:
        print("⚡ Qurilma quvvatlanmoqda (Zaryad olmoqda)...")
        if foiz == 100:
            print("🛑 Batareya toʻldi! Tokdan uzish tavsiya etiladi.")
    else:
        if foiz <= 20:
            print("🚨 Quvvat juda kam! Zaryadlovchi qurilmaga ulang (Ekonom rejim faol).")
        elif 21 <= foiz <= 80:
            print("🟢 Quvvat yetarli. Qurilmadan bemalol foydalanishingiz mumkin.")
        else:
            print("🔥 Quvvat alo darajada! Uzoq vaqtga yetadi.")
    print("-" * 50 + "\n")

def kutubxona_jarima_hisobi(talaba, kitob_nomi, kechikkan_kunlar):
    print(f"📚 Kutubxona nazorati: {talaba}")
    print(f"📖 Olingan kitob: \"{kitob_nomi}\"")

    kunlik_jarima_tarifi = 2000

    if kechikkan_kunlar <= 0:
        print("✅ Rahmat! Kitob oʻz vaqtida yoki barvaqt qaytarildi. Jarima yoʻq.")
    else:
        jami_jarima = kechikkan_kunlar * kunlik_jarima_tarifi
        print(f"🚨 Kitobni topshirish {kechikkan_kunlar} kunga kechikkan!")
        print(f"💸 Kunlik tarif: {kunlik_jarima_tarifi:,} soʻm")
        print(f"💰 Jami toʻlanadigan jarima summasi: {jami_jarima:,} soʻm")
    print("-" * 50 + "\n")

def parol_xavfsizlik_tahlili(parol):
    print(f"🔑 Parol tahlil qilinmoqda: {parol}")

    uzunlik_yoki = len(parol) >= 8
    raqam_bor = any(harf.isdigit() for harf in parol)
    katta_harf_bor = any(harf.isupper() for harf in parol)

    if uzunlik_yoki and raqam_bor and katta_harf_bor:
        print("🟢 Xavfsizlik darajasi: JUDA KUCHLI 🔥")
        print("✅ Tizim ushbu parolni qabul qildi.")
    else:
        print("🔴 Xavfsizlik darajasi: ZAIF / XAVFLI 🚨")
        print("❌ Rad etildi! Kamchiliklar:")
        if not uzunlik_yoki: print("   - Uzunlik kamida 8 ta belgidan iborat boʻlsin.")
        if not raqam_bor: print("   - Kamida 1 ta raqam (0-9) qatnashishi kerak.")
        if not katta_harf_bor: print("   - Kamida 1 ta katta harf (A-Z) boʻlishi shart.")
    print("-" * 50 + "\n")

def futbol_ochko_kalkulyatori(jamoa_nomi, galaba, durang, maglubiyat):
    jami_ochko = (galaba * 3) + (durang * 1)
    jami_oyinlar = galaba + durang + maglubiyat

    print(f"⚽ Jamoa: {jamoa_nomi} | Turnir jadvali")
    print(f"🏃‍♂️ Jami oʻynalgan oʻyinlar: {jami_oyinlar} ta")
    print(f"✅ Gʻalaba: {galaba} | 🤝 Durang: {durang} | ❌ Magʻlubiyat: {maglubiyat}")
    print(f"🏆 Toʻplangan jami ochko: {jami_ochko} ochko")

    if jami_oyinlar > 0:
        samaradorlik = (galaba / jami_oyinlar) * 100
        print(f"📈 Gʻalaba qozonish koʻrsatkichi: {samaradorlik:.1f}%")
    print("-" * 50 + "\n")

def restoran_hisobini_bolish(stol_raqami, umumiy_chek, odam_soni, xizmat_foizi=10):
    print(f"🍽️ Restoran №{stol_raqami}-stol hisob-kitobi:")

    xizmat_haqi = umumiy_chek * (xizmat_foizi / 100)
    yakuniy_chek = umumiy_chek + xizmat_haqi
    har_bir_odamga = yakuniy_chek / odam_soni

    print(f"💵 Taomlar qiymati: {umumiy_chek:,} soʻm")
    print(f"⚡ Xizmat haqi ({xizmat_foizi}%): {int(xizmat_haqi):,} soʻm")
    print(f"💰 Jami toʻlov (Chiqim): {int(yakuniy_chek):,} soʻm")
    print(f"👥 Davradagilar soni: {odam_soni} kishi")
    print(f"💳 Har bir kishi toʻlaydigan ulush: {int(har_bir_odamga):,} soʻmdan")
    print("-" * 50 + "\n")

def promokod_va_bonus_tizimi(mahsulot_narxi, promokod):
    print(f"🛍️ Savatcha tekshirilmoqda. Mahsulot narxi: {mahsulot_narxi:,} soʻm")

    kuponlar = {"PYTHON20": 20, "SUPERXARID": 15, "YANGIYL": 30}

    toza_kod = promokod.strip().upper()

    if toza_kod in kuponlar:
        chegirma_foizi = kuponlar[toza_kod]
        chegirma_summasi = mahsulot_narxi * (chegirma_foizi / 100)
        yakuniy_narx = mahsulot_narxi - chegirma_summasi
        print(f"🔥 Promo-kod muvaffaqiyatli qoʻllandi: {toza_kod} (-{chegirma_foizi}%)")
        print(f"📉 Chegirma summasi: {int(chegirma_summasi):,} soʻm")
        print(f"💵 Toʻlov uchun yakuniy summa: {int(yakuniy_narx):,} soʻm")
    else:
        print("❌ Kiritilgan promo-kod xato yoki muddati oʻtgan!")
        print(f"💵 Toʻlov summasi oʻzgarmadi: {mahsulot_narxi:,} soʻm")
    print("=" * 50 + "\n")

avto_safar_tahlili("Alijon", 450, 8.5, 11000)

batareya_holati_auditi("Samsung S24", 15, zaryadda_mi=False)

kutubxona_jarima_hisobi("Sardor", "Mukammal Dasturlash", 5)

parol_xavfsizlik_tahlili("Py2026")
parol_xavfsizlik_tahlili("SecuredPass2026")

futbol_ochko_kalkulyatori("Nasaf", 12, 4, 2)

restoran_hisobini_bolish(8, 450000, 4)

promokod_va_bonus_tizimi(250000, "python20")
