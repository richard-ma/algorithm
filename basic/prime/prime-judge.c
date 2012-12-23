#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int prime_judge (int n)
{
    int i;

    if (n == 0 || n == 1) {
        return 0; // not prime
    }

    for (i = 2; i < ((int)sqrt(n) + 1); i++) {
        if (n % i == 0) {
            return 0; // not prime
        }
    }

    return 1; // yes!! n is a prime number.
}

int main (int argc, char const* argv[])
{
    int n;

    scanf("%d", &n);

    if (prime_judge(n)) {
        printf("yes!!\n");
    } else {
        printf("no!!\n");
    }

    return 0;
}
