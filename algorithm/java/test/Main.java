package test;

import sort_algorithm.ArrayHeap;

import java.util.Arrays;

/**
 * @author wisedu1
 */
public class Main {
    public static void main(String[] args) {
        int[] test = {10, 5, 7, 1, 2, 8, 11, 20, 9, 9, 9, 2};
        ArrayHeap heap = new ArrayHeap(test);
        heap.sort();
        System.out.println(Arrays.toString(test));
    }
}
