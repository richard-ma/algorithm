#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 1024

int next[MAX];

int kmp_table(const char *t, int t_len)
{
    int pos = 2, cnd = 0;

    next[0] = -1; next[1] = 0;

    while (pos < t_len) {
        if (t[pos-1] == t[cnd]) {
            ++cnd; next[pos] = cnd; ++pos;
        } else if (cnd > 0) {
            cnd = next[cnd];
        } else {
            next[pos] = 0; ++pos;
        }
    }

    return 0;
}

int kmp(const char *s, int s_len, const char *t, int t_len)
{
    int m = 0, i = 0;

    while (m + i < s_len) {
        if (t[i] == s[m+i]) {
            if (i == t_len - 1) {
                return m;
            }
            ++i;
        } else {
            m = m + i - next[i];
            if (next[i] > -1) {
                i = next[i];
            } else {
                i = 0;
            }
        }
    }

    return s_len;
}

int main (int argc, char const* argv[])
{
    int s_len, t_len;
    char s[MAX], t[MAX];
    memset(next, 0, sizeof(int) * MAX);

    scanf("%s", s);
    scanf("%s", t);

    s_len = strlen(s); t_len = strlen(t);

    kmp(s, s_len, t, t_len);

    return 0;
}
