#include <stdio.h>

// Protótipo da função para calcular o tamanho de um array.
size_t arraySize(void *array, size_t elementSize, size_t arraySize);

// Protótipos das funções para imprimir arrays de diferentes tipos.
void intArray(void);
void floatArray(void);
void charArray(void);

int main() {
    
    // Chama as funções para imprimir os arrays.
    intArray();    // Vetor de Inteiros.
    floatArray();  // Vetor de Floats.
    charArray();   // Vetor de Caracteres.

    return 0;
}

void intArray(void) {

    printf("=====================\n");
    printf("  Array de Inteiros.\n");
    printf("=====================\n");

    int vetor[5] = {18, 23, 45, 19, 10};                            // Declaração de um array de inteiros.
    size_t len = arraySize(vetor, sizeof(vetor[0]), sizeof(vetor)); // Chama a função para calcular o tamanho do array de forma dinâmica.
    printf("Tamanho do array: %zu\n", len);

    for (size_t i = 0; i < len; i++) {
        printf("Index: %zu Conteúdo: %d\n", i, vetor[i]); // Imprime o índice e o conteúdo de cada elemento do array.
    }
    
    printf("=====================\n");
}

void floatArray(void) {

    printf("=====================\n");
    printf("  Array de Floats.\n");
    printf("=====================\n");

    float vetor[5] = {14.6, 19.5, 18.25, 9.9, 0.78}; // Declaração de um array de floats.
    size_t len = arraySize(vetor, sizeof(vetor[0]), sizeof(vetor)); // Chama a função para calcular o tamanho do array de forma dinâmica.

    for (size_t i = 0; i < len; i++) {
        printf("Index: %zu Conteúdo: %.2f\n", i, vetor[i]); // Imprime o índice e o conteúdo de cada elemento do array.
    }
    
    printf("=====================\n");
}

void charArray(void) {
    
    printf("=====================\n");
    printf("  Array de Caracteres.\n");
    printf("=====================\n");

    char vetor[5] = {'A', 'B', 'C', 'D', 'E'}; // Declaração de um array de caracteres.
    size_t len = arraySize(vetor, sizeof(vetor[0]), sizeof(vetor)); // Chama a função para calcular o tamanho do array de forma dinâmica.
    
    for (size_t i = 0; i < len; i++) {
        printf("Index: %zu Conteúdo: %c\n", i, vetor[i]); // Imprime o índice e o conteúdo de cada elemento do array.
    }

    printf("=====================\n");
}

// Função para calcular o tamanho do array.
size_t arraySize(void *array, size_t elementSize, size_t arraySize) {
    return arraySize / elementSize;
}
