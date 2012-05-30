#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1024

int next[MAX];

int get_next(char *target, int target_len)
{
    int i, j;
    i = 1; j = 0; next[1] = 0;

    while (i <= target_len) {
        if (j == 0 || target[i] == target[j]) {
            ++i; ++j; next[i] = j;
        } else {
            j = next[j];
        }
    }

    return 0;
}

int main (int argc, char const* argv[])
{
    char str[MAX], target[MAX];
    int str_len, target_len;

    scanf("%s", str);
    scanf("%s", target);

    str_len = strlen(str);
    target_len = strlen(target);

    return 0;
}
