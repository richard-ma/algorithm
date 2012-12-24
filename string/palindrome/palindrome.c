#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int palindrome (char *string)
{
    int ans, ps, pe;

    ans = 1;
    ps = 0; pe = strlen(string)-1;
    while (ps < pe) {
        if (string[ps] != string[pe]) {
            ans = 0; break;
        }
        ps++; pe--;
    }

    return ans;
}

int main (int argc, char const* argv[])
{
    char buf[256];

    while (scanf("%s", buf) != EOF) {
        if (palindrome(buf)) {
            printf("yes!!\n");
        } else {
            printf("no!!\n");
        }
    }

    return 0;
}
