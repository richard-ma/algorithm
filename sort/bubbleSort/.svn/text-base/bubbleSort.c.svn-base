/*
 * =====================================================================================
 *
 *       Filename:  bubbleSort.c
 *
 *    Description:  A recursion implementation of bubble Sort.
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
 *         Name:  r_bubblesort
 *  Description:  
 * =====================================================================================
 */
    void
r_bubblesort ( int *pa, int start, int end )
{
    int i, t;
    if (start == end) {
        return ;
    } else {
        for (i=end; i>start; i--) {
            if (pa[i] < pa[i-1]) {
                t = pa[i];
                pa[i] = pa[i-1];
                pa[i-1] = t;
            }
        }

        r_bubblesort(pa, start+1, end);
    }

    return;
}		/* -----  end of function r_bubblesort  ----- */
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

    r_bubblesort(a, 0, 4);

    for (i=0; i<5; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
