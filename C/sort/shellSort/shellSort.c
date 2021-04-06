/*
 * =====================================================================================
 *
 *       Filename:  shellSort.c
 *
 *    Description:  Shell Sort
 *
 *        Version:  1.0
 *        Created:  07/27/2010 02:37:40 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Richard Ma (richard_ma), richard.ma.19850509@gmail.com
 *        Company:  Feng Huli Primary School
 *
 * =====================================================================================
 */

#include	<stdlib.h>
#include	<stdio.h>


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  shell_sort
 *  Description:  Shell Sort
 * =====================================================================================
 */
    void
shell_sort (int *array, int gap, int n)
{
    int i, j, temp;

    if (gap <= 0) {
        return;
    }

    for (i=gap; i<n; i++) {
        j = i - gap;
        temp = array[i];

        while ((j >= 0) && (array[j] > temp)) {
            array[j + gap] = array[j];
            j = j - gap;
        }
        array[j + gap] = temp;
    }

    shell_sort(array, (gap - 1) / 3, n);

    return;
}		/* -----  end of function shell_sort  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  main
 * =====================================================================================
 */
    int
main ( int argc, char *argv[] )
{
    int array[] = {5, 4, 3, 2, 1};
    int n = 5;
    int gap = 0;
    int i;
    while (gap * 3 + 1 <= n) {
        gap = gap * 3 + 1;
    }

    shell_sort(array, gap, n);

    for (i=0; i<n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
