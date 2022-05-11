def selectionSort(array, size):
    print(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        print(array)
data = [21, 6, 3, 57, 13, 9, 14, 18, 2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)