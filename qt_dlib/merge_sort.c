#include <stdio.h>

int binary_search(int arr[], int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(data) / sizeof(data[0]);
    int target = 5;
    int result = binary_search(data, size, target);
    if (result != -1) {
        printf("Element found at index: %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
