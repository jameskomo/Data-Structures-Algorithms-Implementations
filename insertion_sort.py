def insertionSort(arr):
    indexing_length=range(1, len(arr))
    for i in indexing_length:
        value_to_sort=arr[i]
        while arr[i-1]>value_to_sort and i>0:
            arr[i], arr[i-1]=arr[i-1], arr[i]
    return arr

print(insertionSort([12,7,9,18,2,1,8]))
