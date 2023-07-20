#include <stdio.h>
#include <ctype.h>

int main() {
    char word[100];
    printf("Lütfen bir kelime girin: ");
    scanf("%s", word);

    int i = 0;
    while (word[i]) {
        word[i] = toupper(word[i]);
        i++;
    }

    printf("Kelimenin büyük harf hali: %s\n", word);

    return 0;
}
