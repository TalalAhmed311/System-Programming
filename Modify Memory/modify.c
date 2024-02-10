#include <stdio.h>

int main() {
    int* addressToModify = (int*)0x7fffffffdbbc;

    printf("Original value at address %p: %d\n", (void*)addressToModify, *addressToModify);

    // Modify the value in memory
    *addressToModify = 20;

    printf("Modified value at address %p: %d\n", (void*)addressToModify, *addressToModify);

    return 0;
}
