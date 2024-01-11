

def rotated_binary(arr, tar, s , e):

    if s>=e:
        return -1

    m = s + (e-s)//2

    if arr[m] == tar:
        return m

    if arr[s] < arr[m]:
        if tar >= arr[s] and tar < arr[m]:
            return rotated_binary(arr, tar, s , m-1)
        else:
            return rotated_binary(arr, tar, m+1, e)

    if tar >= arr[m] and tar<= arr[e]:
        return rotated_binary(arr,tar, m+1, e)

    return rotated_binary(arr, tar, s, m-1)

arr = [4,5,1,2,3]
print(rotated_binary(arr, 2, 0 , len(arr)-1))