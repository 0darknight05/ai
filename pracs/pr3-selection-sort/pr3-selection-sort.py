def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Assume the current position holds the minimum
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print array after each step
        print(f"Step {i+1}: {arr}")

    return arr


# -------------------------------
# Example usage
# -------------------------------
arr = [640, 235, 102, 722, 11]

print("Original array:", arr)

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)
