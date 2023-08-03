def count_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a count array to store the occurrences of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element in the input array
    for num in arr:  # this create a cummulative sum of the count of the array
        count[num] += 1

    # Reconstruct the sorted array using the count array
    sorted_arr = []
    for i in range(max_element + 1):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr

# Example usage:
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = count_sort(input_array)
print("Sorted Array:", sorted_array)
