import itertools

def kombinasyon_bul(sayilar, hedef):
    sonuclar = []
    
    for i in range(1, len(sayilar) + 1):
        kombinasyonlar = itertools.combinations(sayilar, i)
        for kombinasyon in kombinasyonlar:
            if sum(kombinasyon) == hedef:
                sonuclar.append(kombinasyon)
    
    return sonuclar

sayilar_str = input("Tam sayı dizisini virgülle ayırarak girin: ")
sayilar = [int(s.strip()) for s in sayilar_str.split(",")]
hedef = int(input("Hedef sayıyı girin: "))

kombinasyonlar = kombinasyon_bul(sayilar, hedef)

print("Hedef sayıya ulaşan kombinasyonlar:")
for kombinasyon in kombinasyonlar:
    print(kombinasyon)
    
    