def en_cok_tekrar_eden_harf(metin):
    harf_sayilari = {}
    
    for harf in metin:
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1
    
    en_cok_tekrar_eden = ''
    en_cok_tekrar_sayisi = 0
    
    for harf, sayi in harf_sayilari.items():
        if sayi > en_cok_tekrar_sayisi:
            en_cok_tekrar_eden = harf
            en_cok_tekrar_sayisi = sayi
    
    return en_cok_tekrar_eden, en_cok_tekrar_sayisi

metin = input("Bir metin girin: ")

en_cok_tekrar_eden, en_cok_tekrar_sayisi = en_cok_tekrar_eden_harf(metin)

print("En çok tekrar eden harf:", en_cok_tekrar_eden)
print("Tekrar sayısı:", en_cok_tekrar_sayisi)
