# EREN AIRLINES A.S  ÇALIŞAN MAAŞ HESAPLAMA

print("    \n    EREN AIRLINES A.S ÇALIŞAN MAAŞ HESAPLAMA SİSTEMİNE HOŞGELDİNİZ  ")


# YÖNETİCİNİN NET MAAŞINI HESAPLAYAN FONKSİYON

def yonetecimaas(calisilangun, gunlukmaas, ekmesai, huzurhakki, kidem):
    print((calisilangun * gunlukmaas) + ekmesai + huzurhakki + kidem)


# YÖNETİCİNİN NET MAAŞI
# YÖNETİCİNİN GÜNLÜK MAAŞI = 3741 TL , EK MESAİ ÜCRETİ = 2500 TL , HUZUR HAKKI ÜCRETİ = 3200
# KIDEM ÜCRETİ = 5000 TL'DİR.

adsoyad = str(input("\nİSİM - SOYİSİM GİRİNİZ : "))
pozisyonsorgu = str(input("ÇALIŞTIĞINIZ POZİSYONU GİRİNİZ : "))

if pozisyonsorgu == "YÖNETİCİ":
    print("   YÖNETİCİ POZİSYONUNU SEÇTİNİZ ")
    calisilangun = int(input("AYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ : "))
    print("AYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun, "GÜN OLARAK GİRDİNİZ.\n")
    gunlukmaas = 3740
    print("SAYIN YÖNETİCİ", adsoyad, "GÜNLÜK MAAŞINIZ", gunlukmaas, "TL'DİR.\n")
    ekmesaisorgu = float(input("EK MESAİ YAPILAN GÜN SAYISINI GİRİNİZ : "))
    ekmesai = 2500 * ekmesaisorgu
    print("SAYIN YÖNETİCİ", adsoyad, "EK MESAİ ÜCRETİNİZ", ekmesai, "TL'DİR.\n")
    huzurhakki = 3200
    print("SAYIN YÖNETİCİ", adsoyad, "HUZUR HAKKI PRİMİNİZ", huzurhakki, "TL'DİR.\n")
    kidem = 5000
    print("SAYIN YÖNETİCİ", adsoyad, " KIDEM PRİMİNİZ", kidem, "TL'DİR.\n")
    print("EREN AIRLINES A.S YÖNETİCİ", adsoyad, "NET TL MAAŞI : ")
    yonetecimaas(calisilangun, gunlukmaas, ekmesai, huzurhakki, kidem)


# YÖNETİCİ ASİSTANININ NET MAAŞINI HESAPLAYAN FONKSİYON
def yoneticiasistanimaas(calisilangun1, gunlukmaas1, ekmesai1, huzurhakki1, kidem1):
    print(calisilangun1 * gunlukmaas1 + ekmesai1 + huzurhakki1 + kidem1)


# YÖNETİCİ ASİSTANININ NET MAAŞI
# YÖNETİCİ ASİSTANININ GÜNLÜK MAAŞI = 1727 TL , EK MESAİ ÜCRETİ = 1000 TL , HUZUR HAKKI ÜCRETİ = 1183 TL
# KIDEM ÜCRETİ = 2500 TL

if pozisyonsorgu == "YÖNETİCİ ASİSTANI":
    print("   YÖNETİCİ ASİSTANI POZİSYONUNU SEÇTİNİZ ")
    calisilangun1 = int(input("\nAYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ : "))
    print("\nAYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun1, "GÜN OLARAK GİRDİNİZ. ")
    gunlukmaas1 = 1727
    print("SAYIN YÖNETİCİ ASİSTANI", adsoyad, "GÜNLÜK MAAŞINIZ", gunlukmaas1, "TL'DİR. ")
    ekmesaisorgu1 = float(input("\nEK MESAİ YAPILAN GÜN SAYISINI GİRİNİZ : "))
    ekmesai1 = 1000 * ekmesaisorgu1
    print("\nSAYIN YÖNETİCİ ASİSTANI", adsoyad, "EK MESAİ ÜCRETİNİZ", ekmesai1, "TL'DİR. ")
    huzurhakki1 = 1183
    print("\nSAYIN YÖNETİCİ ASİSTANI", adsoyad, "HUZUR HAKKI PRİMİNİZ", huzurhakki1, "TL'DİR. ")
    kidem1 = 2500
    print("\nSAYIN YÖNETİCİ ASİSTANI", adsoyad, "KIDEM PRİMİNİZ", kidem1, "TL'DİR. \n")

    print("EREN AIRLINES A.S YÖNETİCİ ASİSTANI SAYIN", adsoyad, " NET TL MAAŞI : ")
    yoneticiasistanimaas(calisilangun1, gunlukmaas1, ekmesai1, huzurhakki1, kidem1)


# PROJE YÖNETİCİSİNİN NET MAAŞINI HESAPLAYAN FONKSİYON

def projeyoneticisimaas(calisilangun2, gunlukmaas2, ekmesai2, kidem2, performans2):
    print(calisilangun2 * gunlukmaas2 + ekmesai2 + kidem2 + performans2)


# PROJE YÖNETİCİSİNİN NET MAAŞI PROJE YÖNETİCİSİNİN GÜNLÜK MAAŞI = 1432 TL , EK MESAİ ÜCRETİ = 650 TL
#  KIDEM ÜCRETİ = 1700 , PERFORMANS ÜCRETİ = 1000 TL

if pozisyonsorgu == "PROJE YÖNETİCİSİ":
    print("   PROJE YÖNETİCİSİ POZİSYONUNU SEÇTİNİZ ")
    calisilangun2 = int(input("\nAYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ : "))
    print("\nAYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun2, "GÜN OLARAK GİRDİNİZ. ")
    gunlukmaas2 = 1432
    print("SAYIN PROJE YÖNETİCİSİ", adsoyad, "GÜNLÜK MAAŞINIZ", gunlukmaas2, "TL'DİR. ")
    ekmesaisorgu2 = float(input("\nEK MESAİ YAPILAN  GÜN SAYISINI GİRİNİZ : "))
    ekmesai2 = 650 * ekmesaisorgu2
    print("SAYIN PROJE YÖNETİCİSİ", adsoyad, "EK MESAİ ÜCRETİNİZ", ekmesai2, "TL'DİR. ")
    kidem2 = 1700
    print("\nSAYIN PROJE YÖNETİCİSİ", adsoyad, "KIDEM PRİMİNİZ", kidem2, "TL'DİR. ")
    performanssorgu = int(input("\nSAYIN PROJE YÖNETİCİSİ BİTİRDİĞİNİZ PROJE SAYISINI GİRİNİZ : "))
    performans2 = 1000 * performanssorgu
    print("\nSAYIN PROJE YÖNETİCİSİ", adsoyad, "PERFORMANS PRİMİNİZ", performans2, "TL'DİR. ")

    print("\nEREN AIRLINES A.S PROJE YÖNETİCİSİ SAYIN", adsoyad, " NET TL MAAŞI : ")
    projeyoneticisimaas(calisilangun2, gunlukmaas2, ekmesai2, kidem2, performans2)


# PROJE YÜRÜTÜCÜSÜNÜN NET MAAŞINI HESAPLAYAN FONKSİYON
def projeyurutucusumaas(calisilangun3, gunlukmaas3, ekmesai3, kidem3, performans3):
    print(calisilangun3 * gunlukmaas3 + ekmesai3 + kidem3 + performans3)


# PROJE YÜRÜTÜCÜSÜNÜN NET MAAŞI
# PROJE YÜRÜTÜCÜSÜNÜN GÜNLÜK MAAŞI = 1300 TL , EK MESAİ ÜCRETİ = 600 TL , KIDEM ÜCRETİ = 1634 TL
# PERFORMANS ÜCRETİ = 999 TL

if pozisyonsorgu == "PROJE YÜRÜTÜCÜSÜ":
    print("   PROJE YÜRÜTÜCÜSÜ POZİSYONUNU SEÇTİNİZ ")
    calisilangun3 = int(input("\nAYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ :"))
    print("\nAYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun3, "GÜN OLARAK GİRDİNİZ.")
    gunlukmaas3 = 1300
    print("\nSAYIN PROJE YÜRÜTÜCÜSÜ", adsoyad, " GÜNLÜK MAAŞINIZ", gunlukmaas3, "TL'DİR. ")
    ekmesaisorgu3 = float(input("\nEK MESAİ YAPILAN GÜN SAYISINI GİRİNİZ : "))
    ekmesai3 = 600 * ekmesaisorgu3
    print("\nSAYIN PROJE YÜRÜTÜCÜSÜ", adsoyad, "EK MESAİ ÜCRETİNİZ", ekmesai3, "TL'DİR. ")
    kidem3 = 1634
    print("\nSAYIN PROJE YÜRÜTÜCÜSÜ", adsoyad, "KIDEM PRİMİNİZ", kidem3, "TL'DİR. ")
    performanssorgu3 = int(input("\nSAYIN PROJE YÜRÜTÜCÜSÜ KONTROL EDİP RAPORLADIĞINIZ PROJE SAYISINI GİRİNİZ : "))
    performans3 = 999 * performanssorgu3
    print("\nSAYIN PROJE YÜRÜTÜCÜSÜ", adsoyad, " PERFORMANS PRİMİNİZ", performans3, "TL'DİR .")
    print("\nEREN AIRLINES A.S PROJE YÜRÜTÜCÜSÜ SAYIN", adsoyad, " NET TL MAAŞI :")
    projeyoneticisimaas(calisilangun3, gunlukmaas3, ekmesai3, kidem3, performans3)


# TEKNİK PERSONELİN NET MAAŞINI HESAPLAYAN FONKSİYON
def teknikpersonelmaas(calisilangun4, gunlukmaas4, ekmesai4, kidem4, performans4, yolyardim):
    print(calisilangun4 * gunlukmaas4 + ekmesai4 + kidem4 + performans4 + yolyardim)


# TEKNİK PERSONELİN GÜNLÜK MAAŞI = 975 TL , EK MESAİ ÜCRETİ = 400 TL , KIDEM ÜCRETİ = 1000 TL
# PERFORMANS ÜCRETİ = 339 TL , YOL YARDIM ÜCRETİ = 429 TL

if pozisyonsorgu == "TEKNİK PERSONEL":
    print("   TEKNİK PERSONEL POZİSYONUNU SEÇTİNİZ ")
    calisilangun4 = int(input("\nAYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ : "))
    print("AYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun4, "GÜN OLARAK GİRDİNİZ.")
    gunlukmaas4 = 975
    print("\nSAYIN TEKNİK PERSONEL", adsoyad, "GÜNLÜK MAAŞINIZ", gunlukmaas4, "TL'DİR. ")
    ekmesaisorgu4 = float(input("\nEK MESAİ YAPILAN GÜN SAYISINI GİRİNİZ : "))
    ekmesai4 = 400 * ekmesaisorgu4
    print("\nSAYIN TEKNİK PERSONEL", adsoyad, "EK MESAİ ÜCRETİNİZ", ekmesai4, "TL'DİR. ")
    kidem4 = 1000
    print("\nSAYIN TEKNİK PERSONEL", adsoyad, "KIDEM PRİMİNİZ", kidem4, "TL'DİR.")
    performanssorgu4 = int(input("ÇALIŞTIĞINIZ PROJE SAYISINI GİRİNİZ : "))
    performans4 = 339 * performanssorgu4
    print("\nSAYIN TEKNİK PERSONEL", adsoyad, "PERFORMANS PRİMİNİZ", performans4, "TL'DİR. ")
    yolyardim = 429
    print("\nSAYIN TEKNİK PERSONEL", adsoyad, "YOL YARDIM ÜCRETİNİZ", yolyardim, "TL'DİR. \n")
    print("EREN AIRLINES A.S TEKNİK PERSONEL", adsoyad, " NET TL MAAŞI :")
    teknikpersonelmaas(calisilangun4, gunlukmaas4, ekmesai4, kidem4, performans4, yolyardim)


# TEMİZLİK GÖREVLİSİNİN NET MAAŞINI HESAPLAYAN FONKSİYON
def temizlikpersonelimaas(calisilangun5, gunlukmaas5, kidem5, yolyardim5, giyimyardim5,
                          gidayardim5):
    print(
        calisilangun5 * gunlukmaas5 + kidem5 + yolyardim5 + giyimyardim5 + gidayardim5)


# TEMİZLİK GÖREVLİSİNİN GÜNLÜK MAAŞI = 650 TL , EK MESAİ ÜCRETİ = 200 TL , KIDEM ÜCRETİ = 300 TL
# YOL YARDIM ÜCRETİ = 429 TL , GİYİM YARDIM ÜCRETİ = 500 TL, GIDA YARDIM ÜCRETİ = 500 TL

if pozisyonsorgu == "TEMİZLİK GÖREVLİSİ":
    print("   TEMİZLİK GÖREVLİSİ POZİSYONUNU SEÇTİNİZ ")
    calisilangun5 = int(input("\nAYLIK ÇALIŞILAN GÜN SAYISINI GİRİNİZ : "))
    print("AYLIK ÇALIŞILAN GÜN SAYISINI", calisilangun5, "GÜN OLARAK GİRDİNİZ. ")
    gunlukmaas5 = 573
    print("\nSAYIN TEMİZLİK GÖREVLİSİ", adsoyad, "GÜNLÜK MAAŞINIZ", gunlukmaas5, "TL'DİR.")
    kidem5 = 305
    print("\nSAYIN TEMİZLİK GÖREVLİSİ", adsoyad, "KIDEM PRİMİNİZ", kidem5, "TL'DİR . ")
    yolyardim5 = 429
    print("\nSAYIN TEMİZLİK GÖREVLİSİ", adsoyad, "YOL YARDIM ÜCRETİNİ", yolyardim5, "TL'DİR. ")
    giyimyardim5 = 521
    print("\nSAYIN TEMİZLİK GÖREVLİSİ", adsoyad, "GİYİM YARDIMI ÜCRETİNİ", giyimyardim5, "TL'DİR. ")
    gidayardim5 = 511
    print("\nSAYIN TEMİZLİK GÖREVLİSİ", adsoyad, "GIDA YARDIM ÜCRETİNİ", gidayardim5, "TL'DİR.\n ")
    print("EREN AIRLINES A.S TEMİZLİK GÖREVLİSİ", adsoyad, " NET TL MAAŞI :")
    temizlikpersonelimaas(calisilangun5, gunlukmaas5, kidem5, yolyardim5, giyimyardim5,
                          gidayardim5)
