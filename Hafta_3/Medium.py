def count_words(text):
    words = text.split()  # Metni boşluklardan böler ve kelimeleri bir liste olarak saklar
    num_words = len(words)  # Kelime sayısını liste uzunluğuyla hesaplar
    return num_words

user_input = input("Bir metin girin: ")
word_count = count_words(user_input)
print("Girilen metindeki kelime sayısı:", word_count)
