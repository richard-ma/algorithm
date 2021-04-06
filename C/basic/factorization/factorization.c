#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{
    int i, n;

    while (scanf("%d", &n) != EOF) {
        if (n == 1) {
            printf("%d\n", 1);
        }

        while (n != 1) {
            for (i = 2; i <= n; i++) {
                if (n % i == 0) {
                    printf("%d\n", i);
                    break;
                }
            }
            n = n / i;
        }
    }

    return 0;
}
