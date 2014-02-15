#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int reverse (char *ans, int length)
{
    int i, j;
    char t;

    i = 0; j = strlen(ans) - 1;
    while (i < j) {
        t = ans[i]; ans[i] = ans[j]; ans[j] = t;
        i++; j--;
    }

    return 0;
}

int dec_any (int n, int t_system, char *ans)
{
    int pos;

    pos = 0;
    while (n / t_system != 0) {
        ans[pos] = n % t_system + '0';
        n = n / t_system;
        pos++;
    }
    // last position
    ans[pos] = n % t_system + '0';
    pos++;
    ans[pos] = '\0';

    reverse(ans, pos);

    return 0;
}

int main (int argc, char const* argv[])
{
    int t_system, n;
    char ans[1024];

    scanf("%d", &t_system);
    while (scanf("%d", &n) != EOF) {
        dec_any(n, t_system, ans);

        printf("%s\n", ans);
    }

    return 0;
}
