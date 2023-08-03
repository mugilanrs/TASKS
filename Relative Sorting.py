def SortArray(arr1, arr2):
    sorted_lst = []  # a empty list to and elements
    for x in arr2:  # arr2 will b the outer loop
        while x in arr1:  # arr1 is the inner loop
            sorted_lst.append(x)
            arr1.remove(x)

    return (sorted_lst + sorted(arr1))


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(SortArray(arr1, arr2))