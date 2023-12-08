import yazitura
import sayitahmini
import taskagitmakas
import zar_atma
import amırallll
def oyun():
    print("╔════════════════════════════╗")
    print("║ ********OYUNLAR************║")
    print("║                            ║")
    print("║         1)YAZI-TURA        ║")
    print("║                            ║")
    print("║        2-SAYI TAHMİNİ      ║")
    print("║                            ║")
    print("║        3-TAŞ-KAĞIT-MAKAS   ║")
    print("║                            ║")
    print("║        4-ZAR SALLAMA       ║")
    print("║                            ║")
    print("║        5-Amiral Battı      ║")
    print("║                            ║")
    print("╚════════════════════════════╝")
    secim=input("Seçimini yap:")
    if(secim=='1'):
        yazitura.yazitura()
    elif(secim=='2'):
        sayitahmini.sayitahmini()
    elif secim=='3':
        taskagitmakas.tas_kagit_makas()
    elif secim=='4':
        zar_atma.zar()
    elif secim=='5':
        amırallll.amır()
