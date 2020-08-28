def quickSort(list):
    #Eucladian Algorithm Concept/Inductive Proofs
    if len(list)<2:
        return list
    else:
        #Removing Last Item in List to use as Pivot
        pivot=list.pop()
        # Getting all items lower than pivot without excluding the Pivot because it was popped
        less_pivot=[i for i in list if i<=pivot]
        # Getting all items greater than pivot without excluding the Pivot because it was popped
        greater_pivot=[i for i in list if i>pivot]
        
    #Concatenating the less_pivot list+pivot item+greater items list
    return quickSort(less_pivot)+[pivot]+quickSort(greater_pivot)

print(quickSort([2,4,1,3,8,6,5]))

