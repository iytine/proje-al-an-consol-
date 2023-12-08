def tas_kagit_makas():
    import random
    item=["t","k","m"]
    npc=random.choice(item)
    print("TAŞ KAĞIT MAKAS TURNUVASINA HOŞGELDİN")
    print("TAŞ için 't' KAĞIT için 'k' MAKAS için 'm'")
    secim=input("SEÇİMİ YAP:")
    i=0
    j=0
    for x in range(4):
        if(secim.lower()==npc):
            print("BERABERE")
        elif((secim.lower()=='t' and npc=='m')or(secim.lower()=='k'and npc=='m')or(secim.lower()=='k'and npc=='t')):
            print(" TEBRİKLER SAYI ALDINIZ")
            i=i+1
        else:
            print("MAALESEF BU ELİ VERDİNİZ")
            j=j+1
        secim=input("SEÇİMİ YAP:")
    if(i>j):
        print("TEBRİKLER ŞAMPİYON")
    elif(i<j):
        print(" KISMET DEĞİLMİŞ")
    else:
        print("KAYBEDEBİLİRDİN BUNA DA ŞÜKÜR")

