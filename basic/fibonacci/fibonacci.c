#include <stdio.h>
#include <stdlib.h>

int fibonacci (int n)
{
    int ans1, ans2, ans, i;

    if (n == 1 || n == 2) return 1;

    ans1 = 1; ans2 = 1;
    for (i = 0; i < n-2; i++) {
        ans = ans1 + ans2;
        ans1 = ans2;
        ans2 = ans;
    }
    
    return ans;
}

int main (int argc, char const* argv[])
{
    int n;

    scanf("%d", &n);

    printf("%d\n", fibonacci(n));

    return 0;
}
