import random

def sayitahmini():
    print("SAYI TAHMİNİ OYUNUNA HOŞ GELDİNİZ")
    print(" 1 2 2 ?  3 3 3  ?  57 76 43 8? !")
    zorluk = input("ZORLUK seviyesi zor,orta,kolay şeklinde yazınız:")
    
    if zorluk.lower() == "kolay":
        x = random.randint(1, 10)
        puan = 70
        can = 7
    elif zorluk.lower() == "orta":
        x = random.randint(1, 100)
        puan = 120
        can = 6
    elif zorluk.lower() == "zor":
        x = random.randint(1, 1000)
        puan = 200
        can = 5
        
    for a in range(1, can + 1):
        tahmin = int(input("tahminini gir:"))
        if tahmin == x:
            print("DOĞRUUU!!! PUANINIZ:", puan)
            break
        else:
            puan = (puan - puan /can)
            if tahmin > x:
                print("ÇOK BÜYÜK")
            else:
                print("ÇOK KÜÇÜK")


