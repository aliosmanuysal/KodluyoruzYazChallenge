def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    user_input = int(input("Bir sayı girin: "))
    if is_prime(user_input):
        print(f"{user_input} bir asal sayıdır.")
    else:
        print(f"{user_input} bir asal sayı değildir.")
except ValueError:
    print("Geçersiz bir sayı girdiniz. Lütfen bir tamsayı girin.")
