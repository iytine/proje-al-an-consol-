def bmi():
    boy=int(input("Boyunuzu girin:"))
    kilo=int(input("Kilonuuz girin:"))
    if(boy/(kilo*kilo)<18.5):
        print("İdeal kilonun altında")
    elif boy/(kilo*kilo)>=18.5 and boy/(kilo*kilo)<25: 
        print("İdeal kilo")
    elif boy/(kilo*kilo)>=25 and boy/(kilo*kilo)<30:
        print("İdeal kilonun üstünde")
    else:
        print("İdeal kilonun çok üstünde")
