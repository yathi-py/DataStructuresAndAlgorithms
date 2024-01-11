

def linear_search(arr, target, index=0):

    if index > len(arr)-1:
        return False

    if arr[index] == target:
        return True

    return linear_search(arr, target, index+1)

print(linear_search([1,2,3,4], 5))

def search_multiple(arr, target , index=0, output=[]):
    if index > len(arr)-1:
        return output

    if arr[index] == target:
        output.append(index)

    return search_multiple(arr,target,index+1, output)

print(search_multiple([5,1,2,3,4,5,5], 5))


# not optimal
def search_multiple_without_arg(arr, target, index=0):

    list = []
    if index > len(arr)-1:
        return list

    if arr[index] == target:
        list.append(index)

    list2 = search_multiple_without_arg(arr,target,index+1)

    return list+list2
print(search_multiple_without_arg([5,1,2,3,4,5,5], 5))


