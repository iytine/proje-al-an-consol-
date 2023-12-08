def carpim_tablosu():
    print("x'e y'lik çarpım tablosu giriniz:")
    x=int(input("x:"))
    y=int(input("y:"))
    for a in range (1,x+1):
        for b in range(1,y+1):
            print(a,"*",b,"=",a*b)

