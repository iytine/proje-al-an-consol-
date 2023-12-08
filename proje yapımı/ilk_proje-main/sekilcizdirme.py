import turtle
def ana():
    print("╔══════════════════════╗")
    print("║     ŞEKİL ÇİZDİRME   ║")
    print("║        1-kareçiz     ║")
    print("║        2-Beşken      ║")
    print("║        3-Üçgen(güzel)║")
    print("║        4-üçgen       ║")
    print("║ ...DİĞERLERİ....     ║")
    print("║    /\       ____     ║")
    print("║   /  \     |    |    ║")
    print("║  /____\    |____|    ║")
    print("║    ____              ║")
    print("║   /    \     /\      ║")
    print("║  /      \   /  \     ║")
    print("║  \      /   \  /     ║")
    print("║   \____/     \/      ║")
    print("║                      ║")
    print("║                      ║")
    print("╚══════════════════════╝")
    secim=int(input(" seçiminizi yapınız:"))
    if secim==1:
        print("kare çizme seçtiniz")
        import turtle
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
    if secim==2:
        print("Beşgen çizme seçtiniz")
        import turtle
        for a in range(6):
            turtle.forward(150)
            turtle.left(60)
    if secim==3:
        print("Üçgen çizme seçtiniz")
        import turtle
        
        # Turtle kütüphanesinden bir nesne oluşturuyoruz.
        ucgen = turtle.Turtle()
        # Kalem nesnesine renk veriyoruz
        ucgen.pencolor("red")
        #Kalem nesnesine kalınlık veriyoruz.
        ucgen.pensize(2)
        # Kalem nesnesine çizim hızı veriyoruz
        ucgen.speed(7)
        # Döngü ile çizgi uzunluğu ve açısına göre çizim yaptırıyoruz.
        for i in range(41):
            ucgen.forward(300)
            ucgen.right(123)
        turtle.done()
    if secim==4:
        print("üçgen şekiller çizme seçtiniz")
        import turtle
        kalem=turtle.Turtle()
        kalem.pencolor("red")
        kalem.pensize(5)
        for i in range(3):
            kalem.forward(200)
            kalem.left(120)
        turtle.done()
    else:
        for x in range(secim):
            turtle.forward(100)
            turtle.right(360/secim)

