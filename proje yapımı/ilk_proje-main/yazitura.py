def yazitura():
    import random
    yt=random.randint(1,2)
    tahmin=input("YAZI TURA?")
    if yt==1:
        print("YAZI")
    else:
        print("TURA")
    if yt==1:
        atilan="YAZI"
    else:
        atilan="TURA"
    if tahmin==atilan:
        print("KAZANDIN")
    else:
        print("KAYBETTİN")
    secim=input("DEVAM ETMEK İSTİYOR MUSUN İstiyorsa e:")
    if(secim=='e' or secim=='E'):
        yazitura()
    secim=input("DEVAM ETMEK İSTEMİYORMUSUN h:")
    if(secim=='h' or secim=='h'):
        import anamenu
        anamenu.Anamenu()
        
