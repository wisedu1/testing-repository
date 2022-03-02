package sort_algorithm;
/**
 * @author wisedu1
 */


public class ArrayHeap {
    private int[] arr;
    public ArrayHeap(int[] arr) {
        this.arr = arr;
    }

    private void swap(int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void sort() {
        int len = arr.length;
        // 初始化大顶堆
        buildMaxHeap(len);
        int lastIndex = len - 1;
        for (int i = lastIndex; i > 0; i--) {
            swap(0, i);
            len--;
            adjustHeap(0, len);
        }
    }

    // len / 2 取整的结果其实是第一个非叶子节点，换言之就是有孩子节点的节点
    private void buildMaxHeap(int len) {
        for (int i = (int) Math.floor(len / 2); i >= 0; i--) {
            adjustHeap(i, len);
        }
    }

    /**
     * 该方法作用是：以下标为 i 的元素为根节点，往下的部分调整为堆结构
     * len 的作用只是防止越界，数组的下标最多为 len - 1
     */
    private void adjustHeap(int i, int len) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        // 假定该节点是最大的节点
        int largest = i;

        // 左孩子节点大，记录新的最大节点下标
        if (left < len && arr[left] > arr[largest]) {
            largest = left;
        }

        // 右孩子节点大，记录新的最大节点下标
        // 这两步就是找到该节点和它的两个子节点中最大的节点
        if (right < len && arr[right] > arr[largest]) {
            largest = right;
        }

        // 不相等，说明子节点中存在比该节点大的节点，那么堆还未调整成功
        // 交换该节点和最大的子节点，那么父子关系交换，从新的子节点（原父节点）继续调整（递归操作），直到父节点大于等于两个子节点，则说明堆调整成功
        if (largest != i) {
            swap(i, largest);
            adjustHeap(largest, len);
        }
    }
}