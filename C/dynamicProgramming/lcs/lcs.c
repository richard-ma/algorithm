#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  MAX_SIZE 256

int main(int argc, const char *argv[]) {
    
    char s1[MAX_SIZE], s2[MAX_SIZE], t[MAX_SIZE];
    int i, j, k, l, len1, len2, len;
    int a[MAX_SIZE + 1][MAX_SIZE + 1];

    scanf("%s", s1);
    scanf("%s", s2);

    len1 = strlen(s1);
    len2 = strlen(s2);

    for (i = 0; i <= len1; i++) {
        a[i][0] = 0;
    }

    for (i = 0; i <= len2; i++) {
        a[0][i] = 0;
    }

    for (i = 1; i <= len1; i++) {
        for (j = 1; j <= len2; j++) {
            if (s1[i] == s2[j]) {
                a[i][j] = a[i-1][j-1] + 1;
            } else {
                if (a[i-1][j] >= a[i][j-1]) {
                    a[i][j] = a[i-1][j];
                } else {
                    a[i][j] = a[i][j-1];
                }
            }
        }
    }

    for (k = 0; k <= len1; k++) {
        if (i == 0) {
            printf("   ");
        } else {
            printf("%c ", s1[k - 1]);
        }
        for (l = 0; l <= len2; l++) {
            printf("%d", a[k][l]);
        }
        printf("\n");
    }

    return 0;
}
