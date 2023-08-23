from math import factorial

def kombinasyon(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

n = 30  # Toplam öğrenci sayısı
r = 4   # Seçilecek öğrenci sayısı

farkli_sekiller = kombinasyon(n, r)
print(f"{n} öğrenci arasından {r} farklı kişi seçilebilir: {farkli_sekiller} farklı şekilde.")
