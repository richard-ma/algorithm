/*
 * =====================================================================================
 *
 *       Filename:  selectionSort.c
 *
 *    Description:  A recursion implementation of Selection Sort.
 *
 *        Version:  1.0
 *        Created:  07/17/2010 05:03:10 PM
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
 *         Name:  r_selectsort
 *  Description:  
 * =====================================================================================
 */
    void
r_selectsort ( int *pa, int start, int end )
{
    int i, t, min;
    if (start == end) {
        return ;
    } else {
        min = start;
        for (i=start+1; i<=end; i++) {
            if (pa[i] < pa[min]) {
                min = i;
            }
        }
        t = pa[min];
        pa[min] = pa[start]; 
        pa[start] = t;

        r_selectsort(pa, start+1, end);
    }

    return;
}		/* -----  end of function r_selectsort  ----- */
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
    int a[] = {5, 4, 3, 2, 1};

    r_selectsort(a, 0, 4);

    for (i=0; i<5; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
