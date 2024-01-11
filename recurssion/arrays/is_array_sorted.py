

def is_sorted(arr, i=0):

    if i >= len(arr)-1:
        return True
    return arr[i] < arr[i+1] and is_sorted(arr, i+1)

print(is_sorted([1,4,3,4,5,6]))