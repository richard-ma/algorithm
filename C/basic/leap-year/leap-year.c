#include <stdio.h>
#include <stdlib.h>

int main (int argc, char const* argv[])
{
    int year;

    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("yes!!\n"); // year is a leap year.
    } else {
        printf("no!!\n");
    }

    return 0;
}
