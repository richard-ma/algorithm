#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#define MAX 1000000

int map[MAX];

int prime_eratosthenes (void)
{
    int i, j;

    memset(map, 0, sizeof(int) * MAX);
    map[0] = -1; map[1] = -1;

    for (i = 2; i < MAX; i++) {
        if (map[i] == -1) continue;

        for (j = i*2; j < MAX; j+=i) {
            map[j] = -1;
        }
    }

    return 0;
}

int main (int argc, char const* argv[])
{
    int start, end;
    int i;

    scanf("%d", &start);
    scanf("%d", &end);

    prime_eratosthenes();

    for (i = start; i <= end; i++) {
        if (map[i] == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
