/*
 * =====================================================================================
 *
 *       Filename:  countSort.c
 *
 *    Description:  Counting Sort
 *
 *        Version:  1.0
 *        Created:  08/04/2010 05:50:12 PM
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

#define	MAX_SIZE 100			/* The array max size. */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  countSort
 *  Description:  
 * =====================================================================================
 */
    void
countSort (int array[], int dest[], int size)
{
    int c[6], i;

    /* Init c array. */
    for (i=0; i<6; i++) c[i] = 0;

    for (i=0; i<size; i++) c[array[i]] = c[array[i]]+1;

    for (i=1; i<6; i++) c[i] = c[i] + c[i-1];

    for (i=size-1; i>=0; i--) {
        dest[c[array[i]] - 1] = array[i];
        c[array[i]] = c[array[i]] - 1;
    }

    return;
}		/* -----  end of function countSort  ----- */
/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
    int
main ( int argc, char *argv[] )
{
    int a[MAX_SIZE] = {2, 5, 4, 3, 2, 1, 1, 1, 5}, b[MAX_SIZE];
    int i, size = 9;

    countSort(a, b, size);

    for (i=0; i<size; i++) {
        printf("%d ", b[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
