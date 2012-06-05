#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define  MAX_SIZE 1024

/* 朴素的匹配算法 */
int basic_pattern(char *source, char *pattern) {
    int i, j, ans, flg, ls, lp;

    ls = strlen(source); lp = strlen(pattern);
    ans = -1;

    for (i = 0; i < ls; i++) {
        flg = 1;
        for (j = 0; j < lp; j++) {
            if (source[i] == pattern[j]) {
                i++;
                continue;
            } else {
                flg = 0;
                i += j;
                break;
            }
        }
        if (flg == 1) {
            ans = i - lp;
            break;
        }
    }

    return ans;
}

int main(int argc, const char *argv[]) {
    
    char source[MAX_SIZE], pattern[MAX_SIZE];
    scanf("%s", source);
    scanf("%s", pattern);

    /* basic pattern */
    int ans = basic_pattern(source, pattern);
    printf("%d\n", ans);

    return 0;
}
