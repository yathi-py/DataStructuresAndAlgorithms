
def binary_search(arr, target, start, end):

    if start>end:
        return -1

    mid = start + (end-start)//2

    if arr[mid] == target:
        return mid

    if target > arr[mid]:
        return binary_search(arr,target, mid+1, end)

    return binary_search(arr,target,start,mid-1)

arr = [1,2,3,4,5,6,7]

print(binary_search(arr, 100, 0, len(arr)-1))