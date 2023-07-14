from datetime import date

def yas_hesapla(dogum_tarihi):
    bugun = date.today()
    yas = bugun.year - dogum_tarihi.year
    if bugun.month < dogum_tarihi.month or (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
        yas -= 1
    return yas

gun = int(input("Doğum gününüzü girin: "))
ay = int(input("Doğum ayınızı girin: "))
yil = int(input("Doğum yılınızı girin: "))

dogum_tarihi = date(yil, ay, gun)
yas = yas_hesapla(dogum_tarihi)
print("Yaşınız:", yas)
