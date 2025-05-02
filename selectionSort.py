def selectionSort(self, arr):
        #code here
        size = len(arr)
        for i in range(size):
            mini = i
            for j in range(i + 1, size):
                if arr[mini] > arr[j]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr
