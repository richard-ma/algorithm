#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int c_idx(int row, int col, int max_col) {
    return row * max_col + col;
}

int lcs(char *source1, char *source2,  char *target) {
    int len1, len2;
    int i, j, p_cnt, z, array_len;
    char *p1, *p2;
    len1 = strlen(source1) + 1; len2 = strlen(source2) + 1;
    array_len = len1 * len2;

    printf("%d\n", len1);
    printf("%d\n", len2);

    int *c = (int *)malloc(array_len * sizeof(int));

    for (i = 0; i < len1; i++) {
        c[c_idx(0, len1-1, len2)] = 0;
    }

    for (i = 0; i < len2; i++) {
        c[c_idx(0, len2-1, len2)] = 0;
    }

    for (i = 1; i < len1; i++) {
        for (j = 1; j < len2; j++) {
            if (source1[i] == source2[j]) {
                c[c_idx(i, j, len2)] = c[c_idx(i-1, j-1, len2)] + 1;
            } else {
                if (c[c_idx(i-1, j, len2)] >= c[c_idx(i, j-1, len2)]) {
                    c[c_idx(i,j,len2)] = c[c_idx(i-1, j, len2)];
                } else {
                    c[c_idx(i,j,len2)] = c[c_idx(i, j-1, len2)];
                }
            }
        }
    }
    
    for (z = 0, p_cnt=1; z < len1 * len2; z++, p_cnt++) {
        printf("%d", c[z]);
        if (p_cnt % len1 == 0) {
            printf("\n");
        }
    }

    free(c);
}

int main(int argc, const char *argv[]) {
    
    char s1[256], s2[256], t[256];

    scanf("%s", s1);
    scanf("%s", s2);

    lcs(s1, s2, t);

    return 0;
}
