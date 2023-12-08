def termometre():
    print("SICAKLIK ÇEVİRİCİ: 'C'=DERECE, 'K'=KELVİN 'F'= FAHRENHEIT")
    secim=input("ÇEVİRMEK İSTEDĞİNİZ BİRİMİ GİRİNİZ:")
    derece=int(input("sıcaklığı gir:"))
    secim2=input("HANGİ BİRİME ÇEVİRECEĞİNİZİ GİRİNİZ:")
    derece2=0
    if(secim=='C' and secim2=='K'):
        derece2=derece+273
    elif(secim=='K' and secim2=='C'):
        derece2=derece-273
    elif(secim=='C' and secim2=='F'):
        derece2=derece*9/5+32
    elif(secim=='F' and secim2=='C'):
        derece2=5/9*(derece-32)
    elif(secim=='K' and secim2=='F'):
        derece2=1.8*(derece-273)+32
    elif(secim=='F' and secim2=='K'):
        derece2=(derece-32)/1.8+273
    print(derece,secim,"=",derece2,secim2)
