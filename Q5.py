def find_duplicates(arr):
    duplicates = set()
    result = []

    for num in arr:
        if num in duplicates:
            result.append(num)
        else:
            duplicates.add(num)

    return result


if __name__ == "__main__":
 
    arr = [1, 2, 3, 4, 2, 5, 6, 3, 7]

    duplicates = find_duplicates(arr)

    if len(duplicates) == 0:
        print("No duplicates found.")
    else:
        print("Duplicates found:", duplicates)
