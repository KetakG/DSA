# Bubble sort
## In each iteration, it takes respective largest element to its respective position
## Time complexity is O(n2) and in-place sorting.
## It is stable algorithm since it doesn't change the order of equal elements.
## It can be slightly optimised for sorted algorithm.

array = [3,25,2,15,5,6]

def bubbleSort(arr):
    for i in range(len(arr)):
        ##Taking n-i for range in j because in every pass, last i elements are fixed.
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(array)
array = bubbleSort(array)
print(array)

##Optimising time complexity for sorted array
def optBubbleSort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swap == False:
            break
    return arr