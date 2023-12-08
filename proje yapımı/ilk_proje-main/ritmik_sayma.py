def ritmik_sayma():
    bas=int(input("BAŞLANGIÇ NOKTASI:"))
    bit=int(input("BİTİŞ NOKTASI:"))
    fark=int(input(" KAÇAR KAÇR?:"))
    for x in range(bas,bit+1,fark):
        print(x)
