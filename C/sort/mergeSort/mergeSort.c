/*
 * =====================================================================================
 *
 *       Filename:  mergeSort.c
 *
 *    Description:  Merge Sort
 *
 *        Version:  1.0
 *        Created:  07/26/2010 01:13:19 PM
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
 *         Name:  merge
 *  Description:  merge
 * =====================================================================================
 */
    void
merge (int array[], int low, int mid, int high)
{
    int i,k;
    int *temp = (int*) malloc((high - low + 1) * sizeof(int));
    int begin1 = low;
    int end1 = mid;
    int begin2 = mid + 1;
    int end2 = high;
    
    for (k=0; begin1<=end1 && begin2<=end2; k++) {
        if (array[begin1] < array[begin2]) {
            temp[k] = array[begin1++];
        } else {
            temp[k] = array[begin2++];
        }
    }

    while (begin1 <= end1) temp[k++] = array[begin1++];
    while (begin2 <= end2) temp[k++] = array[begin2++];

    for (i=0; i<(high - low + 1); i++) {
        array[low+i] = temp[i];
    }
    
    free(temp);

    return;
}		/* -----  end of function merge  ----- */


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  merge_sort
 *  Description:  merge Sort
 * =====================================================================================
 */
    void
merge_sort (int array[], int first, int last)
{
    int mid = 0;
    if (first < last) {
        mid = (first + last) / 2;
        merge_sort(array, first, mid);
        merge_sort(array, mid+1, last);
        merge(array, first, mid, last);
    }

    return ;
}		/* -----  end of function merge_sort  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  main function
 * =====================================================================================
 */
    int
main ( int argc, char *argv[] )
{
    int i;
    int array[] = {5, 4, 3, 2, 1};

    merge_sort(array, 0, 4);

    for (i=0; i<5; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
