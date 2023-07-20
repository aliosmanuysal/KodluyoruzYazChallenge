def calculate_profit(cost, price):
    if cost >= price:
        return "Birim maliyet, birim satış fiyatından yüksek veya eşit olamaz. Kâr edilemez."
    
    profit_per_unit = price - cost
    break_even_point = cost / profit_per_unit
    if break_even_point.is_integer():
        return int(break_even_point)
    else:
        return int(break_even_point) + 1

cost = 100
price = 150

result = calculate_profit(cost, price)
print(f"Ürün satışında kâr edilmeye başlamak için {result} adet ürün satılmalıdır.")

