#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int any_dec (int n, int s_system)
{
    int i, ans;

    i = 0;
    ans = 0;
    while (n / 10 != 0 || n % 10 != 0) {
        ans += (n % 10) * (int)pow(s_system, i);
        n = n / 10; i++;
    }

    return ans;
}

int main (int argc, char const* argv[])
{
    int s_system, n;

    scanf("%d", &s_system);
    while (scanf("%d", &n) != EOF) {
        printf("%d\n", any_dec(n, s_system));
    }

    return 0;
}
