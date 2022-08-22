# Selection sort
## It takes respective smallest elements to its position.
## It makes less memory writes than other many sorting algo. Cycle sort is optimal in terms of memory writes.
## Time complexity is O(n2) and in-place sorting.
## This is basis for heap sort.
## It is unstable algorithm since it might change the order of equal elements.

array = [3,25,2,15,5,6]

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr

print(array)
array = selectionSort(array)
print(array)