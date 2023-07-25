def move_negatives_to_one_side(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
      
        while arr[left] < 0:
            left += 1

        while arr[right] >= 0:
            right -= 1

     
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
   
    arr = [2, -6, 8, -3, -1, 7, 9, -4]

    print("Original Array:")
    print(arr)

    move_negatives_to_one_side(arr)

    print("\nArray after moving negatives to one side:")
    print(arr)
