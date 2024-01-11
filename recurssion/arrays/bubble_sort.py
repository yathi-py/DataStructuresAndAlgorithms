

def bubble_sort(arr, r, c):

    if r == 0:
        return arr

    if c < r:

        if arr[c] > arr[c+1]:
            arr[c], arr[c+1] = arr[c+1], arr[c]

        bubble_sort(arr,r,c+1)

    else:
        bubble_sort(arr,r+1, 0)

arr = [5,4,3,2,1]
print(bubble_sort(arr, 0, len(arr)-1))



