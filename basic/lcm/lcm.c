#include <stdio.h>
#include <stdlib.h>

int gcd (int a, int b)
{

    if (b == 0) {
        return a;
    }

    return gcd(b, a%b);
}

int lcm (int a, int b)
{
    return a * b / gcd(a, b);
}

int main (int argc, char const* argv[])
{
    int a, b;

    scanf("%d", &a);
    scanf("%d", &b);

    printf("%d\n", lcm(a, b));

    return 0;
}
