def selectionSort(alist):
    for i in range(len(alist)):
        minPosition=i
        for j in range(i+1, len(alist)):
            if alist[minPosition]>alist[j]:
                minPosition=j
        alist[i],alist[minPosition]=alist[minPosition],alist[i]
    return alist
print(selectionSort([5,2,1,9,0,4,6]))


# ****************SELECTION SORT EXPLAINED******************

# The selection sort algorithm sorts an array by repeatedly..
# finding the minimum element (considering ascending order) from unsorted...
#  part and putting it at the beginning. 
# The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

# In every iteration of selection sort, the minimum element...
# (considering ascending order) from the unsorted subarray is picked...
#  and moved to the sorted subarray.