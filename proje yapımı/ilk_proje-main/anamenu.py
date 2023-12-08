import hesapmakinesi
import sekilcizdirme
import takvim
import ritmik_sayma
import oyunlar
import not_
import çarpım_tablosu
import bmi
import döviz
import termometre
def Anamenu():
    print("╔═══════════════════════╗")  #şekli oluşturmak için alt tuşuna basılı tut ascii karşılığına bas
    print("║   PYTHON ÇALIŞMALARI  ║")
    print("║ 1-HESAP MAKİNESİ      ║")
    print("║ 2-OYUNLAR             ║")
    print("║ 3-ŞEKİL ÇİZDİRME      ║")
    print("║ 4-TAKVİM              ║")
    print("║ 5-RİTMİK SAYMA        ║")
    print("║ 6-NOT HESAPLAMA       ║")
    print("║ 7-ÇARPIM TABLOSU      ║")
    print("║ 8-BMI HESAPLAMA       ║")
    print("║ 9-DÖVİZ UYGULAMASI    ║")
    print("║ 10-SICAKLIK ÇEVİRME   ║")
    print("║ 11-AŞK ÖLÇER ♥        ║")
    print("║ 12-Yazı yazma hızı    ║")
    print("║        ölçer          ║")
    print("║ 13-ÇIKIŞ (e)          ║")
    print("║    Seçimini yap       ║")
    print("╚═══════════════════════╝")
    secim = input("Seçiminiz:")
    if (secim == '1'):
        hesapmakinesi.hesapmakinesi()
        Anamenu()
    if (secim == '2'):
        oyunlar.oyun()
        Anamenu()
    if(secim == '3'):
        sekilcizdirme.ana()
        Anamenu()
    if(secim=='4'):
        takvim.takvim()
        Anamenu()
    if(secim=='5'):
          ritmik_sayma.ritmik_sayma()
          Anamenu()
    if(secim=='6'):
        not_.ortalama()
        Anamenu()
    if(secim=='7'):
        çarpım_tablosu.carpim_tablosu()
        Anamenu()
    if(secim=='8'):
        bmi.bmi()
        Anamenu()
    if(secim=='9'):
        döviz.doviz()
        Anamenu()
    if(secim=='10'):
        termometre.termometre()
        Anamenu()
    if(secim=='11'):
        isim1 = input("İsminiz: ")
        isim2 = input("Sevgilinizin ismi: ")
        # len fonksiyonu ile isimlerin uzunluklarını alıyoruz
        ask = len(isim1) + len(isim2)
        if len(isim1) > len(isim2):
            ask -= 5
        else:
            ask += 3
            ask *= 52
            ask = ask / (100 + len(isim2))
        if ask>10:
            ask = 10
        else:
            # round fonksiyonu ile sonucumuzu yuvarlıyoruz
            ask = round(ask)
        print(isim1, "ve ",isim2," aşk puanı ",ask)
        Anamenu()
    if(secim=='12'):
        import time
        import datetime
        print("Yazma Hızı için son 3 saniye")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("Go!")
        time.sleep(0.2)
        before = datetime.datetime.now()
        text=input("yazınız:")
        after = datetime.datetime.now()
        speed = after - before
        seconds = round(speed.total_seconds(),2)
        letter_per_second = round(len(text) / seconds,1)
        print("Yazı Yazdığınız saniye : {} saniye.".format(seconds))
        print("{} Puanınız .".format(letter_per_second))
        Anamenu()
    if (secim == '13' or secim == 'e' or secim == 'E'):
        print("Çıkış yapılıyor...")

