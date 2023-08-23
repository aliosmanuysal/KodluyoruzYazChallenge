import math

try:
    # Kullanıcıdan bir sayı girişi alınır
    sayi = float(input("Bir sayı girin: "))
    
    # Karekökünü alınır
    karekok = math.sqrt(sayi)
    
    # Eğer karekökün tam sayı değeri, karekökünden gelen değere eşitse
    if karekok == int(karekok):
        print("Sayının karekökü:", karekok)
    else:
        print("Sayı tam olarak karekökten çıkmıyor.")
except ValueError:
    print("Geçersiz bir sayı girdiniz.")
