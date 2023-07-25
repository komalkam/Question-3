def find_kth_largest_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None

    sorted_arr = sorted(arr)
    kth_largest = sorted_arr[-k]
    kth_smallest = sorted_arr[k - 1]
    return kth_largest, kth_smallest


if __name__ == "__main__":
  
    arr = [7, 3, 9, 1, 5, 2, 8, 4, 6]
    k = 3

    result = find_kth_largest_smallest(arr, k)

    if result is not None:
        kth_largest, kth_smallest = result
        print(f"{k}th largest number:", kth_largest)
        print(f"{k}th smallest number:", kth_smallest)
    else:
        print("Invalid value of k.")
