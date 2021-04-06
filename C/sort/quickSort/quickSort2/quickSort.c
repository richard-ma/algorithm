/*
 * =====================================================================================
 *
 *       Filename:  quickSort.c
 *
 *    Description:  Quick Sort (Randomize Version)
 *
 *        Version:  1.0
 *        Created:  07/28/2010 04:22:31 PM
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
 *         Name:  swap
 *  Description:  
 * =====================================================================================
 */
    void
swap (int *a, int *b)
{
    int t;

    t = *a;
    *a = *b;
    *b = t;

    return;
}		/* -----  end of function swap  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  quick_sort
 *  Description:  
 * =====================================================================================
 */
    void
quick_sort (int *array, int begin, int end)
{
    int r = end;
    int k = begin + 1;
    int mark;

    if (begin >= end) return;

    mark = rand() % (end - begin + 1) + begin;
    swap(&array[begin], &array[mark]);

    while (k < r) {
        if (array[begin] > array[k]) {
            k++;
        } else {
            swap(&array[k], &array[r]);
            r--;
        }
    }

    if (array[k] < array[begin]) {
        swap(&array[k], &array[begin]);
        quick_sort(array, begin, k-1);
        quick_sort(array, r, end);
    } else {
        swap(&array[--k], &array[begin]);
        quick_sort(array, begin, k-1);
        quick_sort(array, r, end);
    }

    return;
}		/* -----  end of function quick_sort  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
    int
main ( int argc, char *argv[] )
{
    int i;
    int array[] = {5, 4, 6, 3, 2, 1};

    quick_sort(array, 0, 5);

    for (i=0; i<6; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
