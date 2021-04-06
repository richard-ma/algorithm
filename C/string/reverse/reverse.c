#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int reverse (char *string, int length)
{
    int i, j;
    char t;

    i = 0; j = length - 1;
    while (i < j) {
        t = string[i]; string[i] = string[j]; string[j] = t;
        i++; j--;
    }
    return 0;
}

int main (int argc, char const* argv[])
{
    char buf[256];

    while (scanf("%s", buf) != EOF) {
        reverse(buf, strlen(buf));
        printf("%s\n", buf);
    }

    return 0;
}
