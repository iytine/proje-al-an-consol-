import calendar
def takvim():
    sene=int(input("yılı gir:"))
    ay=int(input("Ayı gir:"))
    print(calendar.month(sene,ay))
