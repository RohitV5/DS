"""
Collection of sorting algorithms.
Includes: Bubble, Selection, Insertion, Merge, Quick, Heap sort.
"""
class Sorting:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Sorting.merge_sort(L)
            Sorting.merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
    @staticmethod
    def quick_sort(arr):
        def _quick_sort(arr, low, high):
            if low < high:
                pi = Sorting.partition(arr, low, high)
                _quick_sort(arr, low, pi-1)
                _quick_sort(arr, pi+1, high)
        _quick_sort(arr, 0, len(arr)-1)
        return arr
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    @staticmethod
    def heap_sort(arr):
        n = len(arr)
        def heapify(arr, n, i):
            largest = i
            l = 2*i + 1
            r = 2*i + 2
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        for i in range(n//2-1, -1, -1):
            heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)
        return arr
# Example usage:
# arr = [5,2,9,1]
# print(Sorting.quick_sort(arr)) 