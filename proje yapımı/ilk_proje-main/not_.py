def ortalama():
    print("╔═════════════════════════════════╗")
    print("║         NOT HESAPLAMA           ║")
    print("╚═════════════════════════════════╝")
    
    sınav1 = int(input("1. sınav notunuzu giriniz:"))
    sınav2 = int(input("2. sınav notunuzu giriniz:"))
    ortalama = (sınav1 + sınav2)/2
    if (sınav1 > 100 or sınav1 <0) or (sınav2 > 100 or sınav2 <0):
        print ("notlar 0 ile 100 arasında olmak zorunda")
    else:
        if ortalama >= 90: print("harikasın aa")
        elif ortalama >=70 : print("notun fena değil")
        elif ortalama >=50 : print("notun fena değil")
        else:
            print("maalesef")
        input()
    
