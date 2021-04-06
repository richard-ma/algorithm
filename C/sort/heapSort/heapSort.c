/*
 * =====================================================================================
 *
 *       Filename:  heapSort.c
 *
 *    Description:  Heap Sort
 *
 *        Version:  1.0
 *        Created:  07/27/2010 05:22:49 PM
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
 *         Name:  parent
 *  Description:  
 * =====================================================================================
 */
    int
parent (int i)
{
    return (int)(i / 2);
}		/* -----  end of function parent  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  left
 *  Description:  
 * =====================================================================================
 */
    int
left (int i)
{
    return (2 * i);
}		/* -----  end of function left  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  right
 *  Description:  
 * =====================================================================================
 */
    int
right (int i)
{
    return (2 * i + 1);
}		/* -----  end of function right  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  max_heapify
 *  Description:  
 * =====================================================================================
 */
    void
max_heapify (int *array, int i, int size)
{
    int l = left(i);
    int r = right(i);
    int largest, temp;

    if (l < size && array[l] > array[i]) {
        largest = l;
    } else if (r < size && array[r] > array[i]) {
        largest = r;
    } else {
        largest = i;
    }

    if (largest != i) {
        temp = array[i]; array[i] = array[largest]; array[largest] = temp;
        max_heapify(array, largest, size);
    }

    return;
}		/* -----  end of function max_heapify  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  build_max_heap
 *  Description:  
 * =====================================================================================
 */
    void
build_max_heap (int *array, int size)
{
    int i;

    for (i=size; i>=0; i--) {
        max_heapify(array, i, size);
    }

    return;
}		/* -----  end of function build_max_heap  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  heap_sort
 *  Description:  
 * =====================================================================================
 */
    void
heap_sort (int *array, int size)
{
    int i, temp;
    build_max_heap(array, size);

    for (i=size - 1; i>=1; i--) {
        temp = array[0]; array[0] = array[i]; array[i] = temp;
        size--;
        max_heapify(array, 0, size);
    }

    return;
}		/* -----  end of function heap_sort  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  print
 *  Description:  
 * =====================================================================================
 */
    void
print (int *array, int size)
{
    int i;
    for (i = 0; i<size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return;
}		/* -----  end of function print  ----- */

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
    int
main ( int argc, char *argv[] )
{
    int array[] = {3, 2, 1, 4, 5};
    int n = 5;

    heap_sort(array, n);
    print(array, n);

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
