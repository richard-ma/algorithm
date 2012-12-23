#include <stdio.h>
#include <stdlib.h>

int gcd (int a, int b)
{

    if (b == 0) {
        return a;
    }

    return gcd(b, a%b);
}

int main (int argc, char const* argv[])
{
    int a, b;

    scanf("%d", &a);
    scanf("%d", &b);

    printf("%d\n", gcd(a, b));

    return 0;
}
